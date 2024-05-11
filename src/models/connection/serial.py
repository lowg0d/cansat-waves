from typing import List, Tuple

import serial
import serial.tools.list_ports as list_port_tool


class SerialModel:
    def __init__(self, root, _timeout: int = 1) -> None:
        self.root = root
        self.ser = serial.Serial(timeout=_timeout)

        self.is_connected = False
        self.port_list: List[str] = []  # update to set ?

    def update_ports(self) -> None:
        self.port_list = [port.device for port in list_port_tool.comports()]

    # ===============================================================#

    def open_serial(self) -> Tuple[bool, str]:
        try:
            self.ser.open()
            self.is_connected = True
            return True, "Connected"

        except serial.SerialException as exc:
            if "PermissionError" in str(exc):
                return (
                    False,
                    f"Device Already Connected Or Has Been Disconnected. {exc}",
                )

            else:
                self.root.app.show_error("Error Openning The Serial Port.", str(exc))
                return False, "Unknown Error Openning The Serial Port."

    def close_serial(self) -> None:
        self.ser.close()
        self.is_connected = False

    # ===============================================================#

    def write(self, data: str) -> None:
        try:
            b_data = str(data).encode("utf-8")
            self.ser.write(b_data)

        except serial.SerialException as exc:
            self.root.app.show_error("Error Sending Data To The Serial Port", str(exc))

    def read(self) -> str:
        try:
            rcv_data = str(self.ser.readline().decode("utf-8"))
            return rcv_data

        except serial.serialutil.SerialException:  # type:ignore
            return "UnPlugged"

        except UnicodeDecodeError:
            return "DecodeError"

        except Exception as exc:
            self.root.app.show_error("Unknown Read Error", str(exc))
            return str(exc)
