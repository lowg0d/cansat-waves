from kore import RecentNotificationsWidget


class CustomRecentNotificationsWidget(RecentNotificationsWidget):
    def __init__(self, root, dnd_state: bool):
        super().__init__(root, dnd_state)
        self.FADE_ANI_DURATION = 100
        self.BOTTOM_MARGIN = -72
        self.INITIAL_MARGIN = -72
        self.MAX_HEIGHT = 400
        self.WIDTH = 310
        self.SPACING = 5
        self.RIGHT_MARGIN = 5
        self.MAX_MSG_LENGTH = 23
        self.MAX_NOTIFICATIONS = 10
        self.FIXED_HEIGHT = 28
        self.STYLE = """
            QFrame{
                border-radius: 5px; 
                padding-left: 5px;
                padding-right: 5px;
                color: #bebebe;
                background-color:#252528;
            }
            QLabel{
                background-color:transparent;  
                padding: 3px;
                padding: 3px;
            }
        """
        self.TOP_LABEL_STYLE = """
            QLabel{
                padding:0px;margin:0px;font: 900 10pt "Aux Mono";color:#eeeeed;
            }
                """
        self.DND_BTN_STYLE = """
            QToolButton {
                background-color: transparent;
                border:0px;
                height:10px;
                width:10px;
                border-radius:4px;
                padding:4px;
                margin-right:1px
            } 
            QToolButton:checked{
                background-color:#627254;
            }"""
        self.MESSAGE_STYLE = """
            QLabel{
                background-color: transparent;
                color:#bebebe;
                font: 9pt "Aux Mono";
            }"""
        self.TIME_LABEL_STYLE = (
            "QLabel{color: #bebebe;background-color: transparent;font: 9pt 'Aux Mono';}"
        )
        self.CLOSE_BUTTON_STYLE = """QToolButton{
                color: #99bebebe;
                background: transparent;
                font: 800 9pt "Aux Mono";
                border:0px;
            }QToolButton:hover{
                color: #bebebe;
            }"""
        self.FRAME_STYLE = """
            QFrame{
                background-color: #&color;
                border: 1px solid #99&color;
                border-radius: 5px;
            }
            QLabel{border:none;}"""

        self.DND_ICON_PATH = "./src/ui/assets/icons/bell-off-dark.svg"
