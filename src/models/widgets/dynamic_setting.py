import re
from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QFileDialog, QLabel, QToolTip, QWidget

from src.ui import Ui_SettingsForm


class SettingForm(QWidget):

    def __init__(self, root, key: str, metadata: dict):
        """
        Initialize a setting widget within a configuration UI.

        Args:
            root: The parent widget or main application window.
            metadata: A dict containing the metadata of the setting.
        """
        super().__init__(root)
        self.root = root
        self.config = root.config
        self.log = self.root.log

        self.ui = Ui_SettingsForm()
        self.ui.setupUi(self)

        self.ui.name.setText(metadata["name"])
        self.ui.description.setText(self.__transform_link(metadata["description"]))
        self.ui.description.setOpenExternalLinks(True)

        self.need_restart = metadata.get("restart", False)
        self.key = "settings." + key
        self.initial_value = self.config.get(self.key, "settings")

        _type = metadata.get("custom_type", None)
        if not _type:
            _type = type(self.initial_value).__name__

        self.function_map = {
            "str": self.__setup_string,
            "int": self.__setup_int,
            "bool": self.__setup_toggle,
            "float": self.__setup_float,
            "ThemeChanger": self.__setup_theme,
            "FolderSelect": self.__setup_folder_select,
        }

        self.__hide_controls()
        self.__choose_type(_type)

    # -------------------------------------------------------------- #

    def __hide_controls(self) -> None:
        self.ui.profile.hide()
        self.ui.restart.hide()
        self.ui.numbers_2.hide()
        self.ui.numbers.hide()
        self.ui.toggle.hide()
        self.ui.string.hide()
        self.ui.button.hide()
        self.ui.combo.hide()

    # -------------------------------------------------------------- #

    def __setup_theme(self) -> None:
        self.ui.combo.show()
        theme_list = self.root.themes.themes
        theme_list = [theme.replace(".qss", "") for theme in theme_list]
        self.ui.combo.addItems(theme_list)
        self.ui.combo.currentIndexChanged.connect(self.__update_theme)

        try:
            index = theme_list.index(self.initial_value)
        except:
            index = 0

        self.ui.combo.setCurrentIndex(index)
        self.__update_theme(custom_time=0)

    def __update_theme(self, index=0, custom_time=200) -> None:
        current_theme = self.ui.combo.currentText()
        self.root.themes.apply_theme(current_theme, custom_time)
        self.config.put(self.key, current_theme, "settings")

    def __setup_folder_select(self) -> None:
        self.ui.button.show()
        simplified_path = self.__simplify_path(self.initial_value)
        self.ui.button.setText(simplified_path)
        self.ui.button.setToolTip(str(self.initial_value))
        self.ui.button.clicked.connect(self.__select_folder)

    def __select_folder(self) -> None:
        dir_ = self.config.get(self.key, "settings")
        options = QFileDialog.Options()  # type: ignore
        new_value = QFileDialog.getExistingDirectory(
            self, "Select Folder", options=options, dir=dir_
        )

        if new_value:
            self.config.put(self.key, new_value, "settings")
            simplified_path = self.__simplify_path(new_value)
            self.ui.button.setText(new_value)
            self.ui.button.setToolTip(simplified_path)

        self.__toggle_restart_visibility(new_value)

    # -------------------------------------------------------------- #

    def __choose_type(self, _type: str) -> None:
        setup_function = self.function_map.get(_type, None)
        if not setup_function:
            self.log.error(f"Type Not Valid '{_type}' in {self.ui.name.text()}")
            return

        setup_function()

    def __setup_string(self) -> None:
        self.ui.string.show()
        self.ui.string.setToolTip(self.initial_value)
        self.ui.string.setText(self.__simplify_string(self.initial_value))
        self.ui.string.textChanged.connect(self.__update_string)

    def __setup_int(self) -> None:
        self.ui.numbers.show()
        self.ui.int_2.setValue(self.initial_value)
        self.ui.int_2.valueChanged.connect(self.__update_integer)

    def __setup_toggle(self) -> None:
        self.ui.toggle.show()
        self.ui.off.setChecked(not self.initial_value)
        self.ui.on.setChecked(self.initial_value)

        self.__enable_toggle(self.__update_toggle_on, self.__update_toggle_off)

    def __setup_float(self) -> None:
        self.ui.numbers_2.show()
        self.ui.float_2.setValue(self.initial_value)
        self.ui.float_2.valueChanged.connect(self.__update_float)

    # -------------------------------------------------------------- #

    def __update_string(self) -> None:
        new_value = self.ui.string.text()
        self.config.put(self.key, new_value, "settings")
        self.__toggle_restart_visibility(new_value)

    def __update_integer(self) -> None:
        new_value = self.ui.int_2.value()
        self.config.put(self.key, new_value, "settings")
        self.__toggle_restart_visibility(new_value)

    def __update_toggle_on(self) -> None:
        self.__toggle_on()
        self.__update_toggle(True)

    def __update_toggle_off(self) -> None:
        self.__toggle_off()
        self.__update_toggle(False)

    def __update_toggle(self, new_value) -> None:
        self.config.put(self.key, new_value, "settings")
        self.__toggle_restart_visibility(new_value)

    def __update_float(self) -> None:
        new_value = self.ui.float_2.value()
        self.config.put(self.key, new_value, "settings")
        self.__toggle_restart_visibility(new_value)

    # -------------------------------------------------------------- #

    def __enable_toggle(self, on_function, off_function) -> None:
        self.ui.off.clicked.connect(off_function)
        self.ui.on.clicked.connect(on_function)

    def __toggle_on(self) -> None:
        self.ui.off.setChecked(False)
        self.ui.on.setChecked(True)

    def __toggle_off(self) -> None:
        self.ui.off.setChecked(True)
        self.ui.on.setChecked(False)

    # -------------------------------------------------------------- #

    def __toggle_restart_visibility(self, new_value: Any) -> None:
        if self.need_restart:
            self.ui.restart.setVisible(new_value != self.initial_value)

    # -------------------------------------------------------------- #

    def __simplify_path(self, path: str = "") -> str:
        simplified_path = "/".join(path.split("/")[-3:])
        simplified_path = (
            f"{simplified_path[:13]}..."
            if len(simplified_path) > 13
            else simplified_path
        )
        return simplified_path

    def __simplify_string(self, string: str) -> str:
        string = f"{string[:13]}..." if len(string) > 13 else string
        return string

    def __transform_link(self, input_string: str) -> str:

        # Define the pattern for markdown links
        pattern = r"\[([^\]]+)\]\((https?://[^\)]+)\)"

        # Function to replace markdown link with HTML anchor tag
        def replace_with_html(match):
            link_text, url = match.groups()
            return f'<a style="color:#5E81AC" href="{url}">{link_text}</a>'

        # Replace all matches in the input string
        return re.sub(pattern, replace_with_html, input_string)
