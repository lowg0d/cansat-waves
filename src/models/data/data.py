import logging

from PySide6.QtCore import QDateTime, QObject, QThread, Signal


class ReaderThread(QThread):
    unplugged = Signal()
    notification = Signal(str, str)

    def __init__(self, root) -> None:
        super().__init__()

        self.root = root
        self.serial = root.serial

        self.unplugged_flag = False
        self.unknown_header_flag = False

        self.unplugged.connect(self.root.handle_thread_stop)

    def run(self):
        while self.serial.is_connected:
            if self.serial.ser.isOpen():
                data = self.serial.read()

                if data == "DecodeError":
                    self.notification.emit("Skipping Corrupted Packet.", "E")
                    continue

                # ===============================================================#

                elif data == "UnPlugged":
                    self.serial.ser.close()

                # ===============================================================#

                else:
                    self.process_data(data)

            # ===============================================================#

            else:
                if not self.unplugged_flag:
                    self.unplugged_flag = True
                    self.unplugged.emit()
                    self.notification.emit(f"Device Unplugged", "E")
                    self.wait()

    def process_data(self, data: str):
        now = QDateTime.currentDateTime().toString("dd.MM.yyyy,hh.mm.ss.zz")
        if len(data) > 2:
            if data.startswith(self.root.packet_header):
                if self.unknown_header_flag:
                    self.unknown_header_flag = False

                # Get Value Chain
                formatted_data = data.replace(self.root.packet_header, "")
                value_chain = formatted_data.strip().split(self.root.split_char)
                print_val = data if not self.root.write_as_list else str(value_chain)

                self.root.s_record.emit(value_chain, now)
                self.root.s_value_chain.emit(value_chain)
                self.root.s_write.emit(print_val)

            # ===============================================================#

            elif data.startswith(self.root.msg_header):
                data = (
                    data.replace(self.root.msg_header, "")
                    .replace("\n", "")
                    .replace("\r", "")
                )
                self.notification.emit(f"{data}", "M")
                self.root.s_record.emit(["MESSAGE", data], now)

            # ===============================================================#

            else:
                if not self.unknown_header_flag:
                    self.unknown_header_flag = True
                    header_preview = data[:10] + "..." if len(data) > 10 else data

                    ## Emit error signal for unknown packet signature header.
                    self.notification.emit(
                        f"Unknown Packet Signature Header: '{header_preview}'", "E"
                    )


class DataModel(QObject):
    s_value_chain = Signal(list)
    s_write = Signal(str)
    s_record = Signal(list, str)

    def __init__(self, root) -> None:
        super().__init__()
        self.root = root
        self.config = root.config
        self.serial = root.serial
        self.log = logging.getLogger("data")

        self.packet_header = self.config.get(
            "settings.packet_signature_header", "settings"
        )
        self.msg_header = self.config.get(
            "settings.message_signature_header", "settings"
        )
        self.split_char = self.config.get("settings.split_char", "settings")
        self.write_as_list = self.config.get("settings.write_as_list", "settings")

        self.unknown_header_flag = False
        self.handling_flag = False

        self.reader_thread = ReaderThread(self)
        self.reader_thread.notification.connect(self.root.notifications.new)

    def start_thread(self) -> None:
        self.reader_thread.start()
        self.log.debug(f"Reader thread started !")

    def stop_thread(self) -> None:
        self.reader_thread.terminate()
        self.log.debug(f"Reader thread stopped !")

    def handle_thread_stop(self) -> None:
        self.root.conn.close_conn()
        self.log.warning(f"Unplug detected")
