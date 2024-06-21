from typing import List

from qtpy.QtCore import QSize, Qt, Signal
from qtpy.QtGui import QBrush, QColor, QCursor, QIcon, QPainter, QPen
from qtpy.QtWidgets import (
    QAbstractItemView,
    QListWidget,
    QListWidgetItem,
    QStyledItemDelegate,
    QVBoxLayout,
    QWidget,
)

from ert.gui.tools.plot.plot_api import EnsembleObject


class EnsembleSelectionWidget(QWidget):
    ensembleSelectionChanged = Signal()

    def __init__(self, ensembles: List[EnsembleObject]):
        QWidget.__init__(self)
        self.__dndlist = EnsembleSelectListWidget(ensembles)

        self.__ensemble_layout = QVBoxLayout()
        self.__ensemble_layout.setSpacing(0)
        self.__ensemble_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__ensemble_layout.addWidget(self.__dndlist)
        self.setLayout(self.__ensemble_layout)
        self.__dndlist.ensembleSelectionListChanged.connect(
            self.ensembleSelectionChanged.emit
        )

    def get_selected_ensembles(self) -> List[EnsembleObject]:
        return self.__dndlist.get_checked_ensembles()


class EnsembleSelectListWidget(QListWidget):
    ensembleSelectionListChanged = Signal()
    MAXIMUM_SELECTED = 5
    MINIMUM_SELECTED = 1

    def __init__(self, ensembles: List[EnsembleObject]):
        super().__init__()
        self._ensemble_count = 0
        self.setObjectName("ensemble_selector")

        for i, ensemble in enumerate(ensembles):
            it = QListWidgetItem(f"{ensemble.experiment_name} : {ensemble.name}")
            it.setData(Qt.ItemDataRole.UserRole, ensemble)
            it.setData(Qt.ItemDataRole.CheckStateRole, i == 0)
            self.addItem(it)
            self._ensemble_count += 1

        self.viewport().setMouseTracking(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setItemDelegate(CustomItemDelegate())
        self.itemClicked.connect(self.slot_toggle_plot)
        self.setToolTip(
            "Toggle up to 5 plots or reorder by drag & drop\nOrder determines draw order and color"
        )

    def get_checked_ensembles(self) -> List[EnsembleObject]:
        return [
            self.item(index).data(Qt.ItemDataRole.UserRole)
            for index in range(self._ensemble_count)
            if self.item(index).data(Qt.ItemDataRole.CheckStateRole)
        ]

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        if self.itemAt(event.pos()):
            self.setCursor(QCursor(Qt.PointingHandCursor))
        else:
            self.setCursor(QCursor(Qt.ArrowCursor))

    def dropEvent(self, e):
        super().dropEvent(e)
        self.ensembleSelectionListChanged.emit()

    def slot_toggle_plot(self, item: QListWidgetItem):
        count = len(self.get_checked_ensembles())
        selected = item.data(Qt.ItemDataRole.CheckStateRole)

        if selected and count > self.MINIMUM_SELECTED:
            item.setData(Qt.ItemDataRole.CheckStateRole, False)
        elif not selected and count < self.MAXIMUM_SELECTED:
            item.setData(Qt.ItemDataRole.CheckStateRole, True)

        self.ensembleSelectionListChanged.emit()


class CustomItemDelegate(QStyledItemDelegate):
    def __init__(self):
        super().__init__()
        self.swap_pixmap = QIcon("img:reorder.svg").pixmap(QSize(20, 20))

    def sizeHint(self, option, index):
        return QSize(-1, 30)

    def paint(self, painter, option, index):
        painter.setRenderHint(QPainter.Antialiasing)

        pen_color = QColor("black")
        background_color = QColor("lightgray")
        selected_background_color = QColor("lightblue")

        rect = option.rect.adjusted(2, 2, -2, -2)
        painter.setPen(QPen(pen_color))

        if index.data(Qt.ItemDataRole.CheckStateRole):
            painter.setBrush(QBrush(selected_background_color))
        else:
            painter.setBrush(QBrush(background_color))

        painter.drawRect(rect)

        text_rect = rect.adjusted(4, 4, -4, -4)
        painter.drawText(text_rect, Qt.AlignHCenter, index.data())

        cursor_x = option.rect.left() + self.swap_pixmap.width() - 14
        cursor_y = int(option.rect.center().y() - (self.swap_pixmap.height() / 2))
        painter.drawPixmap(cursor_x, cursor_y, self.swap_pixmap)
