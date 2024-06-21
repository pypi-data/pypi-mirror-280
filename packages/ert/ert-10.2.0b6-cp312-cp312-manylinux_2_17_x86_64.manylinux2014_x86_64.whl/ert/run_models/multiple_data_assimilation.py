from __future__ import annotations

import functools
import logging
from queue import SimpleQueue
from typing import TYPE_CHECKING, List
from uuid import UUID

import numpy as np

from ert.analysis import ErtAnalysisError, SmootherSnapshot, smoother_update
from ert.config import ErtConfig, HookRuntime
from ert.enkf_main import sample_prior
from ert.ensemble_evaluator import EvaluatorServerConfig
from ert.run_context import RunContext
from ert.run_models.run_arguments import ESMDARunArguments
from ert.storage import Ensemble, Storage

from ..config.analysis_config import UpdateSettings
from ..config.analysis_module import ESSettings
from .base_run_model import BaseRunModel, ErtRunError, StatusEvents
from .event import RunModelStatusEvent, RunModelUpdateBeginEvent

if TYPE_CHECKING:
    from ert.config import QueueConfig

logger = logging.getLogger(__file__)


class MultipleDataAssimilation(BaseRunModel):
    """
    Run multiple data assimilation (MDA) ensemble smoother with custom weights.
    """

    default_weights = "4, 2, 1"
    _simulation_arguments: ESMDARunArguments

    def __init__(
        self,
        simulation_arguments: ESMDARunArguments,
        config: ErtConfig,
        storage: Storage,
        queue_config: QueueConfig,
        es_settings: ESSettings,
        update_settings: UpdateSettings,
        status_queue: SimpleQueue[StatusEvents],
    ):
        self.weights = self.parse_weights(simulation_arguments.weights)
        self.es_settings = es_settings
        self.update_settings = update_settings
        if simulation_arguments.starting_iteration == 0:
            # If a regular run we also need to account for the prior
            number_of_iterations = len(self.weights) + 1
        else:
            number_of_iterations = len(
                self.weights[simulation_arguments.starting_iteration - 1 :]
            )

        super().__init__(
            simulation_arguments,
            config,
            storage,
            queue_config,
            status_queue,
            phase_count=2,
            number_of_iterations=number_of_iterations,
            start_iteration=simulation_arguments.starting_iteration,
        )

    def run_experiment(
        self, evaluator_server_config: EvaluatorServerConfig
    ) -> RunContext:
        self.setPhaseCount(self.number_of_iterations + 1)

        log_msg = f"Running ES-MDA with normalized weights {self.weights}"
        logger.info(log_msg)
        self.setPhaseName(log_msg)

        restart_run = self._simulation_arguments.restart_run
        target_ensemble_format = self._simulation_arguments.target_ensemble

        if restart_run:
            id = self._simulation_arguments.prior_ensemble_id
            try:
                ensemble_id = UUID(id)
                prior = self._storage.get_ensemble(ensemble_id)
                experiment = prior.experiment
                self.set_env_key("_ERT_EXPERIMENT_ID", str(experiment.id))
                self.set_env_key("_ERT_ENSEMBLE_ID", str(prior.id))
                assert isinstance(prior, Ensemble)
                prior_context = RunContext(
                    ensemble=prior,
                    runpaths=self.run_paths,
                    initial_mask=np.array(self.active_realizations, dtype=bool),
                    iteration=prior.iteration,
                )
                if self.start_iteration != prior.iteration + 1:
                    raise ValueError(
                        f"Experiment misconfigured, got starting iteration: {self.start_iteration},"
                        f"restart iteration = {prior.iteration + 1}"
                    )
            except (KeyError, ValueError) as err:
                raise ErtRunError(
                    f"Prior ensemble with ID: {id} does not exists"
                ) from err
        else:
            experiment = self._storage.create_experiment(
                parameters=self.ert_config.ensemble_config.parameter_configuration,
                observations=self.ert_config.observations.datasets,
                responses=self.ert_config.ensemble_config.response_configuration,
                simulation_arguments=self._simulation_arguments,
                name=self._simulation_arguments.experiment_name,
            )

            prior = self._storage.create_ensemble(
                experiment,
                ensemble_size=self._simulation_arguments.ensemble_size,
                iteration=0,
                name=target_ensemble_format % 0,
            )
            self.set_env_key("_ERT_EXPERIMENT_ID", str(experiment.id))
            self.set_env_key("_ERT_ENSEMBLE_ID", str(prior.id))
            prior_context = RunContext(
                ensemble=prior,
                runpaths=self.run_paths,
                initial_mask=np.array(self.active_realizations, dtype=bool),
                iteration=prior.iteration,
            )
            sample_prior(
                prior_context.ensemble,
                prior_context.active_realizations,
                random_seed=self.random_seed,
            )
            self._evaluate_and_postprocess(prior_context, evaluator_server_config)
        enumerated_weights = list(enumerate(self.weights))
        weights_to_run = enumerated_weights[prior.iteration :]

        for iteration, weight in weights_to_run:
            is_first_iteration = iteration == 0

            self.send_event(
                RunModelUpdateBeginEvent(
                    iteration=iteration, run_id=prior_context.run_id
                )
            )
            if is_first_iteration:
                self.run_workflows(HookRuntime.PRE_FIRST_UPDATE, self._storage, prior)
            self.run_workflows(HookRuntime.PRE_UPDATE, self._storage, prior)

            self.send_event(
                RunModelStatusEvent(
                    iteration=iteration,
                    run_id=prior_context.run_id,
                    msg="Creating posterior ensemble..",
                )
            )
            posterior_context = RunContext(
                ensemble=self._storage.create_ensemble(
                    experiment,
                    name=target_ensemble_format % (iteration + 1),  # noqa
                    ensemble_size=prior_context.ensemble.ensemble_size,
                    iteration=iteration + 1,
                    prior_ensemble=prior_context.ensemble,
                ),
                runpaths=self.run_paths,
                initial_mask=(
                    prior_context.ensemble.get_realization_mask_with_parameters()
                    * prior_context.ensemble.get_realization_mask_with_responses()
                    * prior_context.ensemble.get_realization_mask_without_failure()
                ),
                iteration=iteration + 1,
            )
            self.update(
                prior_context,
                posterior_context,
                weight=weight,
            )
            self.run_workflows(
                HookRuntime.POST_UPDATE, self._storage, prior_context.ensemble
            )

            self._evaluate_and_postprocess(posterior_context, evaluator_server_config)
            prior_context = posterior_context

        self.setPhaseName("Post processing...")

        self.setPhase(self.number_of_iterations + 1, "Experiment completed.")

        return prior_context

    def update(
        self,
        prior_context: "RunContext",
        posterior_context: "RunContext",
        weight: float,
    ) -> SmootherSnapshot:
        next_iteration = prior_context.iteration + 1

        phase_string = f"Analyzing iteration: {next_iteration} with weight {weight}"
        self.setPhase(self.currentPhase() + 1, phase_string)
        try:
            return smoother_update(
                prior_context.ensemble,
                posterior_context.ensemble,
                analysis_config=self.update_settings,
                es_settings=self.es_settings,
                parameters=prior_context.ensemble.experiment.update_parameters,
                observations=prior_context.ensemble.experiment.observation_keys,
                global_scaling=weight,
                rng=self.rng,
                progress_callback=functools.partial(
                    self.send_smoother_event,
                    prior_context.iteration,
                    prior_context.run_id,
                ),
            )
        except ErtAnalysisError as e:
            raise ErtRunError(
                "Update algorithm failed for iteration:"
                f"{next_iteration}. The following error occured {e}"
            ) from e

    @staticmethod
    def parse_weights(weights: str) -> List[float]:
        """Parse weights string and scale weights such that their reciprocals sum
        to 1.0, i.e., sum(1.0 / x for x in weights) == 1.0. See for example Equation
        38 of evensen2018 - Analysis of iterative ensemble
        smoothers for solving inverse problems.
        """
        if not weights:
            raise ValueError(f"Must provide weights, got {weights}")

        elements = weights.split(",")
        elements = [element.strip() for element in elements if element.strip()]

        result: List[float] = []
        for element in elements:
            try:
                f = float(element)
                if f == 0:
                    logger.info("Warning: 0 weight, will ignore")
                else:
                    result.append(f)
            except ValueError as e:
                raise ValueError(f"Warning: cannot parse weight {element}") from e
        if not result:
            raise ValueError(f"Invalid weights: {weights}")

        length = sum(1.0 / x for x in result)
        return [x * length for x in result]

    @classmethod
    def name(cls) -> str:
        return "Multiple Data Assimilation (ES MDA) - Recommended"
