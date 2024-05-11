import logging
from typing import Optional

from PySide6.QtCore import QTimer


class ConnModel:
    def __init__(self, root) -> None:
        self.root = root
        self.config = root.config
        self.serial = root.serial
        self.log = logging.getLogger("connection")

        self.last_ports = set()
        self.current_port: str = ""
        self.reconnect_port: str = ""

        self.reconnect_enabled = self.config.get("conn.auto_reconnect")
        self.last_bauds = self.config.get("conn.last_selected_bauds")
        self.last_port = self.config.get("conn.last_selected_port")
        bauds_dict = self.config.get("conn.bauds")
        port_update_interval = self.config.get("conn.port_detection_interval")

        self.root.ui.bauds.addItems(bauds_dict.keys())
        self.root.ui.bauds.setCurrentText(self.last_bauds)

        self.new_port_detect_timer = QTimer()
        self.new_port_detect_timer.timeout.connect(self.port_detector)
        self.new_port_detect_timer.start(port_update_interval)
        self.port_update()

    def _setup_connections(self) -> None:
        self.root.ui.bauds.currentIndexChanged.connect(self.on_bauds_changed)
        self.root.ui.ports.currentIndexChanged.connect(self.on_port_changed)
        self.root.ui.reconnectButton.clicked.connect(self.toggle_auto_reconnect)
        self.root.ui.reconnectButton.setChecked(self.reconnect_enabled)
        self.root.ui.connectButton.clicked.connect(self.conn_switch)

    # ===============================================================#

    def port_detector(self) -> None:

        if self.serial.port_list != self.last_ports:
            self.last_ports = self.serial.port_list
            self.port_update()
            self.log.debug(f"New ports detected: '{self.last_ports}'")

            if self.reconnect_enabled and self.reconnect_port in self.serial.port_list:
                index = self.serial.port_list.index(self.reconnect_port)
                self.root.ui.ports.setCurrentIndex(index)
                self.log.debug(f"Reconnecting To: '{self.reconnect_port}'")
                self.conn_switch()

        else:
            self.serial.update_ports()

    def port_update(self) -> None:
        self.serial.update_ports()
        self.root.ui.ports.clear()

        if self.serial.port_list:

            # Add available ports to the combobox
            self.root.ui.ports.addItems(self.serial.port_list)

            if self.last_port:
                if self.last_port in self.serial.port_list:
                    index = self.serial.port_list.index(self.last_port)
                    # Set index to the last used port
                    self.root.ui.ports.setCurrentIndex(index)

            else:
                # Set index to the first port
                self.root.ui.ports.setCurrentIndex(0)

    # ===============================================================#

    def conn_switch(self) -> None:
        if self.serial.is_connected:
            self.close_conn()

        else:
            self.current_port = self.root.ui.ports.currentText()
            self.open_conn()

    def close_conn(self) -> None:
        self.new_port_detect_timer.start()
        self.root.terminal.terminal_clearer.stop()
        self.root.data.stop_thread()

        self.serial.close_serial()

        self.root.ui.connectButton.setChecked(False)
        self.root.ui.connectButton.setText(f"CONNECT")
        self.root.terminal.write(
            f"<b style='color:#7f4045;'>DISCONNECTED FROM: [ {self.current_port} ]</b>"
        )
        self.current_port = ""
        self.log.debug(f"Disconnected !")

    def open_conn(self) -> None:
        self.serial.ser.port = self.current_port
        self.serial.ser.baudrate = int(self.root.ui.bauds.currentText())

        ## Open the serial port.
        success, msg = self.serial.open_serial()
        if not success:
            self.root.ui.connectButton.setChecked(False)
            self.raise_connection_error(msg)
            return

        self.reconnect_port = self.current_port

        self.new_port_detect_timer.stop()
        self.root.terminal.terminal_clearer.start()
        self.root.data.start_thread()
        self.root.record.reset_blackbox()

        self.root.ui.connectButton.setChecked(True)
        self.root.ui.connectButton.setText(f"CONNECTED: [ {self.current_port} ]")
        self.root.terminal.write(
            f"<b style='color:#627254;'>CONNECTED TO: [ {self.current_port} ]</b>"
        )
        self.log.debug(f"Connected !")

    # ===============================================================#

    def send_data(self, data: Optional[str] = "") -> None:
        if data == None:
            data = self.root.ui.terminalInput.text()
            self.root.ui.terminalInput.setText("")

        if self.serial.is_connected:
            if len(str(data)) > 0:
                self.serial.write(data)
                self.root.terminal.write(
                    f"<ins style='color:#8cb854';>[ Sended -> ]:</ins> '{data}'"
                )

        else:
            self.root.notifications.new("Not Connected", "E")

    # ===============================================================#

    def raise_connection_error(self, message) -> None:
        message = f" '{message}'" if message else ""
        self.root.app.show_error(
            "Error Connecting To Serial Port.", f"Error Message: {message}"
        )

    # ===============================================================#

    def toggle_auto_reconnect(self) -> None:
        self.reconnect_enabled = not self.reconnect_enabled

        self.root.ui.reconnectButton.setChecked(self.reconnect_enabled)
        self.config.put("conn.auto_reconnect", self.reconnect_enabled)
        if not self.reconnect_enabled:
            self.reconnect_port = self.root.ui.ports.currentText()

    def on_bauds_changed(self) -> None:
        new_bauds = self.root.ui.bauds.currentText()
        self.root.config.put("conn.last_selected_bauds", new_bauds)

    def on_port_changed(self) -> None:
        new_port = self.root.ui.ports.currentText()
        if new_port:
            self.root.config.put("conn.last_selected_port", str(new_port))
