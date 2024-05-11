import os

from kore import Kore, NotificationManager
from PySide6.QtCore import QAbstractAnimation, QSize
from qframelesswindow import StandardTitleBar

from src.models import (
    ConnModel,
    CustomNotificationWidget,
    CustomRecentNotificationsWidget,
    DataModel,
    RecordModel,
    SerialModel,
    SettingForm,
    TerminalModel,
)
from src.models.visualization.visualization import VisualizationModel
from src.ui import Ui_MainWindow


class Window(Kore):
    def __init__(self, app):
        super().__init__(app)

        ## add a custom title bar
        self.setTitleBar(StandardTitleBar(self))

        # setup the ui
        self.setupUi(Ui_MainWindow)
        self.ui: Ui_MainWindow
        self.setStyleSheet("")

        self.small_mode_toggled = False
        self.dropdown_enabled = True

        ## configure Ui
        self._custom_setup()

        ## Load Models
        self.serial = SerialModel(self)
        self.terminal = TerminalModel(self)
        self.record = RecordModel(self)
        self.data = DataModel(self)
        self.conn = ConnModel(self)
        self.visualization = VisualizationModel(
            self, self.ui.graphLayout, self.ui.stateLabel
        )

        # self.visualization.set_state("TETAS", "627254")

        self._setup_connections()

        ## Generate Dynamic Settings
        self.dynamic_settings.generate(self.ui.settingsLayout, SettingForm)

        ## start animation
        self.show()
        self.fade_animation(self.ui.centralwidget, duration=500)

    def open_recording_folder(self):
        folder = self.config.get("settings.record_path", "settings")
        folder = os.path.abspath(folder)
        os.system(f"explorer {folder}")

    def _setup_connections(self):
        self.ui.autoScrollButton.clicked.connect(self.terminal.toggle_autoscroll)
        self.ui.clearButton.clicked.connect(self.terminal.clear)

        self.ui.notificationsButton.clicked.connect(
            self.notifications.toggle_recent_notification_panel
        )
        self.ui.openJsonSettingsButton.clicked.connect(self.open_file)
        self.ui.restartAppButton.clicked.connect(self.restart_window)

        self.ui.smallModeButton.clicked.connect(self._toggle_small_mode)
        self.ui.connectionPanelButton.clicked.connect(self.toggle_dropdown)

        self.data.s_write.connect(self.terminal.write)
        self.data.s_record.connect(self.record.write)
        self.ui.recordButton.clicked.connect(self.record.toggle_record)
        self.ui.openRecordingFolder.clicked.connect(self.open_recording_folder)

        self.conn._setup_connections()

    def _custom_setup(self):
        ## Window
        self.ui.versionLabel.setText(f"v{self.app.version}-comp")
        self.ui.statusLabel.setText("")

        # modify splitter ratio
        self.ui.splitter.setSizes([6000, 100])

        ## Set Pages And DropDown
        self.setup_pages(
            {
                self.ui.goToSettingsButton: self.ui.settingsPage,
                self.ui.goToHomeButton: self.ui.mainPage,
            },
            self.ui.mainPages,
            main_stacked=True,
        )

        self.dropdown_ani = self.setup_collapsible(
            container=self.ui.connectionManagementFrame, duration=200
        )

        ## notifications
        self.notifications = NotificationManager(
            self,
            self.config.get("notifications.do_not_disturb"),
            self.config.get("notifications.durations"),
            self.config.get("notifications.levels"),
            notification_widget=CustomNotificationWidget,
            recent_notifications_widget=CustomRecentNotificationsWidget,
        )

    def _on_full_screen_toggle(self):
        super()._on_full_screen_toggle()
        if self.full_screen:
            self.ui.titleBarFrame.hide()
            self.titleBar.hide()
            self.ui.line.hide()
            self.fade_animation(self.ui.centralwidget, duration=500)
        else:
            self.ui.titleBarFrame.show()
            self.titleBar.show()
            self.ui.line.show()
            self.fade_animation(self.ui.centralwidget, duration=500)

    def _toggle_small_mode(self) -> None:
        self.small_mode_toggled = not self.small_mode_toggled
        if self.small_mode_toggled:
            self.ui.mainPageContainerFrame.hide()

            self.setFixedWidth(281)

            h = self.height()
            if h < 700 or h > 1000:
                self.resize(QSize(281, 600))

            self.ui.smallModeButton.setChecked(True)
        else:
            self.ui.mainPageContainerFrame.show()

            self.setMinimumWidth(750)
            self.setMaximumWidth(16777215)
            self.resize(QSize(1080, self.height()))

            self.small_mode_was_toggled = False

    def toggle_dropdown(self) -> None:
        self.dropdown_enabled = not self.dropdown_enabled
        if self.dropdown_enabled:
            self.dropdown_ani.setDirection(QAbstractAnimation.Direction.Forward)
            self.dropdown_ani.start()

        else:
            self.dropdown_ani.setDirection(QAbstractAnimation.Direction.Backward)
            self.dropdown_ani.start()
