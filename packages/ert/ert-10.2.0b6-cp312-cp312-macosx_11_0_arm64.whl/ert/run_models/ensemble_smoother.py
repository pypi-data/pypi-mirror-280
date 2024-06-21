from __future__ import annotations

import functools
import logging
from queue import SimpleQueue
from typing import TYPE_CHECKING

import numpy as np

from ert.analysis import ErtAnalysisError, smoother_update
from ert.config import ErtConfig, HookRuntime
from ert.enkf_main import sample_prior
from ert.ensemble_evaluator import EvaluatorServerConfig
from ert.run_context import RunContext
from ert.run_models.run_arguments import ESRunArguments
from ert.storage import Storage

from ..config.analysis_config import UpdateSettings
from ..config.analysis_module import ESSettings
from .base_run_model import BaseRunModel, ErtRunError, StatusEvents
from .event import RunModelStatusEvent, RunModelUpdateBeginEvent

if TYPE_CHECKING:
    from ert.config import QueueConfig


logger = logging.getLogger(__file__)


class EnsembleSmoother(BaseRunModel):
    def __init__(
        self,
        simulation_arguments: ESRunArguments,
        config: ErtConfig,
        storage: Storage,
        queue_config: QueueConfig,
        es_settings: ESSettings,
        update_settings: UpdateSettings,
        status_queue: SimpleQueue[StatusEvents],
    ):
        super().__init__(
            simulation_arguments,
            config,
            storage,
            queue_config,
            status_queue,
            phase_count=2,
            number_of_iterations=2,
        )
        self.es_settings = es_settings
        self.update_settings = update_settings
        self.support_restart = False

    @property
    def simulation_arguments(self) -> ESRunArguments:
        args = self._simulation_arguments
        assert isinstance(args, ESRunArguments)
        return args

    def run_experiment(
        self, evaluator_server_config: EvaluatorServerConfig
    ) -> RunContext:
        log_msg = "Running ES"
        logger.info(log_msg)
        self.setPhaseName(log_msg)
        ensemble_format = self.simulation_arguments.target_ensemble
        experiment = self._storage.create_experiment(
            parameters=self.ert_config.ensemble_config.parameter_configuration,
            observations=self.ert_config.observations.datasets,
            responses=self.ert_config.ensemble_config.response_configuration,
            simulation_arguments=self._simulation_arguments,
            name=self._simulation_arguments.experiment_name,
        )

        self.set_env_key("_ERT_EXPERIMENT_ID", str(experiment.id))
        prior = self._storage.create_ensemble(
            experiment,
            ensemble_size=self._simulation_arguments.ensemble_size,
            name=ensemble_format % 0,
        )
        self.set_env_key("_ERT_ENSEMBLE_ID", str(prior.id))
        prior_context = RunContext(
            ensemble=prior,
            runpaths=self.run_paths,
            initial_mask=np.array(self.active_realizations, dtype=bool),
            iteration=0,
        )

        sample_prior(
            prior_context.ensemble,
            prior_context.active_realizations,
            random_seed=self.random_seed,
        )

        self._evaluate_and_postprocess(prior_context, evaluator_server_config)

        self.send_event(
            RunModelUpdateBeginEvent(iteration=0, run_id=prior_context.run_id)
        )

        self.setPhaseName("Running ES update step")
        self.run_workflows(
            HookRuntime.PRE_FIRST_UPDATE, self._storage, prior_context.ensemble
        )
        self.run_workflows(
            HookRuntime.PRE_UPDATE, self._storage, prior_context.ensemble
        )

        self.send_event(
            RunModelStatusEvent(
                iteration=0,
                run_id=prior_context.run_id,
                msg="Creating posterior ensemble..",
            )
        )
        posterior_context = RunContext(
            ensemble=self._storage.create_ensemble(
                experiment,
                ensemble_size=prior.ensemble_size,
                iteration=1,
                name=ensemble_format % 1,
                prior_ensemble=prior,
            ),
            runpaths=self.run_paths,
            initial_mask=(
                prior_context.ensemble.get_realization_mask_with_parameters()
                * prior_context.ensemble.get_realization_mask_with_responses()
                * prior_context.ensemble.get_realization_mask_without_failure()
            ),
            iteration=1,
        )
        try:
            smoother_update(
                prior_context.ensemble,
                posterior_context.ensemble,
                analysis_config=self.update_settings,
                es_settings=self.es_settings,
                parameters=prior_context.ensemble.experiment.update_parameters,
                observations=prior_context.ensemble.experiment.observation_keys,
                rng=self.rng,
                progress_callback=functools.partial(
                    self.send_smoother_event, 0, prior_context.run_id
                ),
            )

        except ErtAnalysisError as e:
            raise ErtRunError(
                f"Analysis of experiment failed with the following error: {e}"
            ) from e

        self.run_workflows(
            HookRuntime.POST_UPDATE, self._storage, prior_context.ensemble
        )

        self._evaluate_and_postprocess(posterior_context, evaluator_server_config)

        self.setPhase(2, "Experiment completed.")

        return posterior_context

    @classmethod
    def name(cls) -> str:
        return "Ensemble smoother"
