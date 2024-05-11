import numpy as np
import pyqtgraph as pg
from PySide6.QtGui import QFont

FONT = QFont("Aux Mono", 9)
TICKOFFSET = -32


class MonoAxePlotWidget(pg.PlotItem):
    """_summary_

    Args:
        color (str): the color of the graph line.
        title (str): the title of the graph.
        name (str): the name of the value, in this case the same as title is ok.
        pen_width (float): thw thickness of the line.
        datapoints (int): the amount of data points shown.
    """

    # TODO: fix bug when Y axis changes range a margin appears
    def __init__(
        self,
        color: str,
        title: str,
        name: str,
        pen_width: float,
        datapoints: int,
        antialias: bool,
    ):
        super().__init__(title=title, enableMenu=True)

        self.color = f"#{color.lstrip('#')}"
        self.initGraph(name, pen_width, datapoints, antialias)

    def initGraph(self, name, pen_width, datapoints, antialias_enabled):
        self.x_vals = np.linspace(0, 1, datapoints)
        self.y_vals = np.zeros(datapoints)

        self.graph_plot = self.plot(
            x=self.x_vals,
            y=self.y_vals,
            name=name,
            pen=pg.mkPen(self.color, width=pen_width),
            antialias=antialias_enabled,
            connect="all",
        )

        self.setupAxes()
        self.getViewBox().disableAutoRange(axis="x")
        self.getViewBox().setMouseEnabled(x=False, y=False)
        self.getViewBox().setContentsMargins(0, 0, 0, 0)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

    def setupAxes(self):
        axis_pen = pg.mkPen("#a5a5a5")
        for side in ["bottom", "left", "top", "right"]:
            axis = self.getAxis(side)
            axis.setPen(axis_pen)
            axis.setTickFont(FONT)
            axis.label.setFont(FONT)
            if side == "left":
                axis.setStyle(tickTextOffset=TICKOFFSET)
        self.titleLabel.item.setFont(FONT)

        self.hideButtons()
        self.showGrid(x=True, y=True, alpha=0.35)

    def update(self, value: float):
        self.y_vals = np.roll(self.y_vals, -1)
        self.y_vals[-1] = value

        self.graph_plot.setData(x=self.x_vals, y=self.y_vals)

        # Reapply margin settings after setData
        self.setXRange(self.x_vals[0], self.x_vals[-1], padding=0.0, update=True)

    def clear(self):
        self.y_vals.fill(0)
        self.graph_plot.clear()
        self.update(0.0)
