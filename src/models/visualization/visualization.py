import logging

import pyqtgraph as pg

from .dashboard import DashboardModel


class VisualizationModel:
    def __init__(self, root, graph_container, state_label) -> None:
        self.log = logging.getLogger("visualization")
        self.root = root
        self.ui = root.ui

        self.graph_layout: pg.GraphicsLayout
        self.graph_container = graph_container
        self.state_label = state_label

        self.setup_pyqtgraph()

        self.dash = DashboardModel(self)

    def set_state(self, name: str, color: str) -> None:
        self.state_label.setStyleSheet(
            f"""
                background-color: #4D{color};
                border: 1.5px solid #{color};
            """
        )

        self.state_label.setText(name)

    # ===============================================================#

    """
    def to_connected(self) -> None:
        self.info_update.widget_update_timer.start()
        self.info_update.data_stale_timer.start()
        self.last_update_time = QDateTime.currentDateTime()

    def to_disconnected(self) -> None:
        self.info_update.widget_update_timer.stop()
        self.info_update.data_stale_timer.stop()

        self.info_update.last_state = 80085
        self.info_update.default_data_flag = False
        self.last_value_chain: List[float | str] = []

        self.set_state("N/A", self.state_color)
        self.info_update.clear_labels()
        self.info_update.clear_graphs()
        self.info_update.clear_time_label()
        self.info_update.value_chain = ["default"]
    """

    # ===============================================================#

    def setup_pyqtgraph(self):
        pg.setConfigOptions(
            background="transparent",
            segmentedLineMode="on",
            exitCleanup=True,
            antialias=True,
            useOpenGL=False,
            useCupy=True,
            useNumba=True,
        )

        main_layout = pg.GraphicsLayoutWidget()
        if True:
            main_layout.setAntialiasing(True)

        self.graph_layout = main_layout.addLayout(  # type:ignore
            colspan=1, rowspan=1, border=(0, 0, 0, 0)
        )

        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.graph_layout.setSpacing(10)
        self.graph_container.addWidget(main_layout)
