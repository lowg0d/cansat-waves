import csv
import logging
import os

from PySide6.QtCore import QDateTime


class RecordModel:
    def __init__(self, root) -> None:
        self.root = root
        self.config = root.config
        self.log = logging.getLogger("record")

        self.record_enabled = False
        self.cloud_backup = self.config.get("cloud_backup")
        self.record_path = self.config.get("settings.record_path", "settings")

        self.record_f = os.path.join(self.record_path, "default.csv")
        self.blackbox_f = os.path.join(self.record_path, "last_conn.csv")

        os.makedirs(self.record_path, exist_ok=True)

    def reset_blackbox(self) -> None:
        open(self.blackbox_f, "w", encoding="utf-8")
        self.log.debug("BlackBox reset !")

    def new_record(self) -> None:
        current_datetime = QDateTime.currentDateTime()
        date = current_datetime.toString("dd.MM.yyyy")
        rec_id = 0
        file_name = f"{date}-{rec_id}"

        ## Generate a unique filename.
        while os.path.exists(os.path.join(self.record_path, f"{file_name}.csv")):
            rec_id += 1
            file_name = f"{date}-{rec_id}"

        self.recording_file = os.path.join(self.record_path, f"{file_name}.csv")

        self.log.debug(f"New record: {self.recording_file}")

    # ===============================================================#

    def write(self, data: list, now: str) -> None:
        date, time = now.split(",")
        data.append(date)
        data.append(time)
        if self.record_enabled:

            try:
                with open(
                    self.recording_file, "a", newline="", encoding="utf-8"
                ) as recording_file:
                    writer = csv.writer(recording_file, delimiter=",")
                    writer.writerow(data)

            except Exception as e:
                self.log.error(f"Error writing to record: '{e}'")

        self.write_blackbox(data)

    def write_blackbox(self, data: list) -> None:
        try:
            with open(self.blackbox_f, "a", newline="", encoding="utf-8") as blackbox_f:
                writer = csv.writer(blackbox_f, delimiter=",")
                writer.writerow(data)

        except Exception as e:
            self.log.error(f"Error writing to blackbox record: '{e}'")

    # ===============================================================#

    def toggle_record(self) -> None:
        self.record_enabled = not self.record_enabled

        if self.record_enabled:
            self.new_record()

        self.log.debug(f"Recordings toggled: '{self.record_enabled}'")
