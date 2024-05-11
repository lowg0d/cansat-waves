import json
import logging
import os
from turtle import color

from PySide6.QtCore import QObject, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QPushButton

MAX_LABEL_CHARS = 10

from .graphs import MonoAxePlotWidget


class DashboardModel(QObject):
    def __init__(self, root) -> None:
        super().__init__()
        self.root = root
        self.ui = root.ui
        self.config = root.root.config
        self.log = logging.getLogger("dashboard")

        # =============================================================== #

        self.dashboard_folder = self.config.get("dashboard_folder")

        self.button_container = self.ui.buttonTlmContainer
        self.big_label_container = self.ui.bigTlmContainer
        self.main_container = self.ui.mainTlmContainer
        self.second_container = self.ui.secondTlmContainer
        self.graph_container = self.root.graph_layout

        self.data: dict = {}
        self.labels_map: dict = {}

        # =============================================================== #

        self.dashboards = []
        self._update_dashboards()
        self._setup_dashboard("test")

    def _update_dashboards(self):
        os.makedirs(self.dashboard_folder, exist_ok=True)
        self.dashboards = [
            f for f in os.listdir(self.dashboard_folder) if f.endswith(".json")
        ]
        self.config.put("settings.dashboard", self.dashboards, "settings")

    def _setup_dashboard(self, dashbaord):
        path = os.path.join(self.dashboard_folder, f"{dashbaord}.json")
        with open(path, "r") as _f:
            self.data = json.loads(_f.read())

        self._generate_display_blocks()

    def _generate_display_blocks(self) -> None:
        self._setup_buttons()
        self._setup_labels()
        self._setup_graphs()

    # =============================================================== #

    def _setup_buttons(self) -> None:
        data = self.data.get("buttons", [])
        max_cols = self.data.get("max_cols", 2)
        amount = len(data)

        if amount > 0:
            rows = self._calculate_rows(amount, max_cols)
            row, col = 0, 0

            for metadata in data:
                widget = self.gen_button(metadata)
                self.button_container.addWidget(widget, row, col)

                row += 1
                if row >= rows:
                    row = 0
                    col += 1

    def gen_button(self, data: dict) -> QPushButton:
        ## get properties from the data.
        name = data.get("name", "not_set")
        color = data.get("color", "ffffff")
        payload = data.get("payload", "0")

        ## create button and connect it to send function.
        button_widget = QPushButton(parent=self.root.root, text=name)
        button_widget.clicked.connect(lambda: self.btn_click(payload))

        ## customize style, and properties.
        button_widget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button_widget.setFixedHeight(32)
        button_widget.setStyleSheet(
            "QPushButton {"
            + f"""
                    background-color: #4D{color};
                    border: 2px solid #{color};
                """
            "}"
            + """
                QPushButton:hover {"""
            + f"""
                    border: 2px solid #99{color};
                    background-color: #33{color};
                """
            "}"
            + """
                QPushButton:pressed {"""
            + f"""
                    border: 2px solid #E6{color};
                    background-color: #E6{color};
                """
            "}"
        )

        ## add the widget to the map and return it.
        return button_widget

    def btn_click(self, sender, cmd: str = "0"):
        self.root.root.conn.send_data(cmd)

    # =============================================================== #

    def _setup_labels(self) -> None:
        big_data = self.data["labels"]["big"]
        main_data = self.data["labels"]["main"]
        second_data = self.data["labels"]["second"]

        self._setup_label_kind(self.big_label_container, big_data)
        self._setup_label_kind(self.main_container, main_data)
        self._setup_label_kind(self.second_container, second_data)

    def _setup_label_kind(self, layout, data) -> None:
        max_cols = self.data.get("max_cols", 2)
        amount = len(data)
        if amount > 0:
            rows = self._calculate_rows(amount, max_cols)
            row, col = 0, 0

            for label_data in data:
                widget = self._gen_label(label_data)

                layout.addLayout(widget, row, col)

                row += 1
                if row >= rows:
                    row = 0
                    col += 1

    def _gen_label(self, data: dict) -> QHBoxLayout:
        name = (
            data["name"][:MAX_LABEL_CHARS] + "..."
            if len(data["name"]) > MAX_LABEL_CHARS
            else data["name"]
        )

        unit = data["unit"]
        show_unit = True

        ## Set the default value and unit based on unit type.
        if unit == "format_seconds":
            default_value = "00:00:00"
            unit_to_print = " "
            show_unit = False
        elif unit == "tlm_rate":
            unit_to_print = " ms"
            default_value = "N/A"
        elif unit == "sensor":
            unit_to_print = " "
            default_value = "N/A"
        else:
            unit_to_print = f"{unit}"
            default_value = "N/A"

        name_label = QLabel(f"""{name}: """)

        ## Create the unit and telemetry labels.
        unit_label = QLabel(f"{unit_to_print}")
        tlm_label = QLabel(f"""<b>{default_value}</b>""")

        ## Create the layout and add the labels.
        group_layout = QHBoxLayout()
        group_layout.addWidget(name_label, alignment=Qt.AlignmentFlag.AlignLeft)
        group_layout.addStretch(1)
        group_layout.addWidget(tlm_label, alignment=Qt.AlignmentFlag.AlignRight)

        ## Add the unit label if it should be shown.
        if show_unit:
            group_layout.addWidget(unit_label, alignment=Qt.AlignmentFlag.AlignRight)

        group_layout.addSpacing(10)

        ## add the widget to the map and return it.
        self.labels_map[tlm_label] = data["value_index_in_chain"]
        return group_layout

    # =============================================================== #

    def _setup_graphs(self):
        data = self.data.get("graphs", [])
        amount = len(data)

        if amount > 0:
            for data in data:
                widget = self.graph(data)
                row = data["row"]
                col = data["col"]
                widget.setContentsMargins(0, 0, 0, 0)
                self.graph_container.addItem(widget, row, col)

    def graph(self, data: dict) -> MonoAxePlotWidget:
        title = data["title"]
        unit = data.get("unit", "")
        unit = f" ({unit})" if unit else ""
        color1 = data.get("color_1", "9980FA")
        value_index = data.get("value_index_in_chain_1", 0)

        widget = MonoAxePlotWidget(
            title=f"{title}{unit}",
            name=title,
            color=color1,
            pen_width=1,
            datapoints=100,
            antialias=False,
        )

        widget.update(0.0)

        return widget

    # =============================================================== #

    def _calculate_rows(self, amount: int, max_cols: int) -> int:
        try:
            max_per_column = int(round(amount / 3.5))
            num_columns = min((amount + max_per_column - 1) // max_per_column, max_cols)
            num_rows = (amount + num_columns - 1) // num_columns
            return num_rows

        except:
            return 1
