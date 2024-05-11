from PySide6.QtCore import QTime, QTimer


class TerminalModel:
    def __init__(self, root) -> None:
        self.root = root

        self.autoscroll_enabled = root.config.get("terminal.auto_scroll")
        self.max_lines = root.config.get("terminal.max_lines")
        terminal_clear_interval = root.config.get("terminal.terminal_clear_interval")

        self.terminal_clearer = QTimer()
        self.terminal_clearer.setInterval(terminal_clear_interval)
        self.terminal_clearer.timeout.connect(self._check_line_amount)

        self.root.ui.autoScrollButton.setChecked(self.autoscroll_enabled)

    def write(self, data: str, custom_prefix: str = "") -> None:
        time_stamp = QTime.currentTime().toString("hh:mm:ss.zzz")

        message_prefix = (
            f"[{time_stamp}]:"
            if custom_prefix == ""
            else f"[{time_stamp} {custom_prefix}]:"
        )
        message = f"<b>{message_prefix}</b> {data}"
        self.root.ui.terminal.append(message)

        # Autoscroll to the latest message
        if self.autoscroll_enabled:
            scrollbar = self.root.ui.terminal.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())

    def toggle_autoscroll(self) -> None:
        self.autoscroll_enabled = not self.autoscroll_enabled
        self.root.ui.autoScrollButton.setChecked(self.autoscroll_enabled)
        self.root.config.put("terminal.auto_scroll", self.autoscroll_enabled)

    def clear(self) -> None:
        self.root.ui.terminal.clear()

    def _check_line_amount(self) -> None:
        if self.root.ui.terminal.document().blockCount() > self.max_lines:
            self.clear()
