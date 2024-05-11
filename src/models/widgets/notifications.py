from kore import NotificationWidget


class CustomNotificationWidget(NotificationWidget):
    def __init__(
        self,
        root,
        message: str,
        duration: int,
        timestamp: bool,
        background: str,
        permanent: bool,
        timestamp_msg: str,
        color: str,
    ):
        super().__init__(  # type:ignore
            root,
            message,
            duration,
            timestamp,
            background,
            permanent,
            timestamp_msg,
            color,
        )

        self.RIGHT_MARGIN = 5
        self.BOTTOM_MARGIN = 72
        self.SPACING = 2
        self.WIDTH = 310
        self.LABEL_FIXED_WIDTH = 270
        self.FADE_DURATION = 200

        self.FRAME_STYLE = """
            QFrame{
                border-radius: 5px; 
                padding-left: 2px;
                padding-right: 2px;
                color: #&color;
                border-style: outset;
                background-color: #&bg;
                border:3px solid #99&bg;
            } 
            QLabel{
                border:none;
            }
        """
        self.MESSAGE_STYLE = """
            QLabel{
                color: #&color;
                background-color: transparent;
                font: 900 10pt "JetBrains Mono";
            }
        """
        self.CLOSE_BTN_STYLE = """
            QToolButton{
                color: #99&color;
                background: transparent;
                font: 800 9pt "JetBrains Mono";
                border:0px;
            }
            QToolButton:hover{
                color: #&color;
            }
        """
        self.TIMESTAMP_STYLE = """
            QLabel{
                color: #99&color;
                background-color: transparent;
                font:  8pt "JetBrains Mono";
            }
        """
