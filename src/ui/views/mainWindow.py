# type: ignore
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)
from ..assets import src

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 600)
        MainWindow.setMinimumSize(QSize(1080, 600))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u" /* Global Styling */\n"
"QMainWindow {\n"
"	background-color: #18181B;\n"
"	font: 9pt \"Aux Mono\";\n"
"}\n"
"\n"
"QWidget{\n"
"	background-color: #18181B;\n"
"	color: #bebebe;\n"
"	border: none;\n"
"	font:900  9pt \"Aux Mono\";\n"
"}\n"
"\n"
"QToolTip {\n"
"	border-radius: 5px;\n"
"	background-color:#252528;\n"
"    padding: 4px 6px; \n"
"	font: 8pt \"Aux Mono\";\n"
"}\n"
"QLineEdit{\n"
"	color: #908f8f;\n"
"}\n"
"QLineEdit:focus{\n"
"	color: #bebebe;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #18181B;\n"
"    border: 1px solid #18181B;\n"
"    color: #bebebe;\n"
"    font:  10pt \"Aux Mono\";\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QMenu::item {\n"
"    background-color: transparent;\n"
"    color: #bebebe;\n"
"	border-radius: 5px;\n"
"	padding: 2px 70px 2px 70px;\n"
"}\n"
"QMenu::item:selected {\n"
"    background-color: #3b3b3e;\n"
"}\n"
"\n"
"#terminalInput,\n"
"QTextBrowser{\n"
"	font: 9pt \"Aux Mono\";\n"
"}\n"
"\n"
"/* buttons */\n"
"\n"
"QPushButton{\n"
"	background-color:#252528;"
                        "\n"
"	border-style: outset;\n"
"	qproperty-iconSize: 16px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#settingsPageSideBarContainer QPushButton{\n"
"	background-color:#18181B;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#settingsPageSideBarContainer QPushButton:hover,\n"
"QPushButton:hover{\n"
"	background-color:#3b3b3e;\n"
"}\n"
"\n"
"#settingsPageSideBarContainer QPushButton:pressed,\n"
"QPushButton:pressed{\n"
"	background-color:#1e1e20;\n"
"}\n"
"#connectionManagementFrame QPushButton:checked,\n"
"#topButtons QPushButton:checked{\n"
"	background-color:#7662D0;\n"
"	border: 2px solid #997662D0;\n"
"}\n"
"#dasboardMainButtons QPushButton:checked{\n"
"	border:none;\n"
"	border-right:2px solid #7662D0;\n"
"	border-bottom:2px solid #7662D0;\n"
"}\n"
"\n"
"/* COMBO BOX */\n"
"\n"
"QComboBox{\n"
"	background-color:#252528;\n"
"	border-style: outset;\n"
"	qproperty-iconSize: 16px;\n"
"	border-radius: 5px;\n"
"}\n"
"QComboBox:hover {\n"
"	background-color:#515153;\n"
"}\n"
"QComboBox QListView {\n"
"    background-color: "
                        "#212124;\n"
"	outline: none;\n"
"	border-radius: 5px;\n"
"	border:none;\n"
"}\n"
"QComboBox QListView:item {\n"
"    min-height: 27px;\n"
"    padding: 2px 10px;\n"
"	margin:3px;\n"
"	border-radius: 5px;\n"
"}\n"
"QComboBox QListView:item:hover {\n"
"    background-color:#515153;\n"
"	outline: none;\n"
"	border:none;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/chevron-down-dark.svg);\n"
"	width: 14px;\n"
"	height: 14px;\n"
"	padding-right: 10px;\n"
"}\n"
"QComboBox:drop-down {\n"
"    border: 0px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* labels */\n"
"\n"
"#settingsInfoLabel {\n"
"	color: #383838;\n"
"	font: 7pt \"Aux Mono\";\n"
"}\n"
"#settingsScrollContainer QLabel{\n"
"	font: 10pt \"Aux Mono\";\n"
"	color: #6e6e6e;\n"
"}\n"
"#stateLabel {\n"
"	border-radius: 5px;\n"
"	background-color:#252528;\n"
"}\n"
"#scrollTlmContainer QFrame,\n"
"#tlmFramesContainer QFrame {\n"
"	border-radius: 5px;\n"
"	background-color:#252528;\n"
"}\n"
"\n"
"/* Status Bar */\n"
"\n"
"#customStatusBarFrame QL"
                        "abel{\n"
"	color: #383838;\n"
"	font: 900 7pt \"Aux Mono\";\n"
"	margin-bottom: 2px;\n"
"}\n"
"#line, #line_2, #line_3, #line_4, #line_5,\n"
"#line_6, #line_7, #line_8, #line_9, #line_10{\n"
"    border: 0px;\n"
"    background-color: #383838;\n"
"}\n"
"\n"
"/* Scrollbar */\n"
"\n"
"QScrollBar {\n"
"    border: 0;\n"
"    width: 10px;\n"
"    background-color: #18181B; \n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #252528;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    border-radius: 5px; \n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"}\n"
"QScrollBar::handle::vertical:hover {\n"
"    background-color: #3b3b3e; \n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    height: 0; \n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical,\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"/* SETTING FORM */\n"
"\n"
"#SettingsForm QFrame{\n"
"	border-"
                        "radius:5px;\n"
"	background-color:#252528;\n"
"}\n"
"#SettingsForm #container QFrame{\n"
"	border:none;\n"
"}\n"
"/* information */\n"
"\n"
"#SettingsForm #profile QLabel{\n"
"	background-color:#3b3b3e;\n"
"	border: 2px solid #212124;\n"
"}\n"
"#SettingsForm #name{\n"
"	color: #bebebe;\n"
"	font: 900 12pt \"Aux Mono\";\n"
"}\n"
"#SettingsForm #description{\n"
"	color: #6e6e6e;\n"
"	font: 400 10pt \"Aux Mono\";\n"
"}\n"
"#SettingsForm #restart{\n"
"	color: #a53d3d;\n"
"	font: 800 9pt \"Aux Mono\";\n"
"}\n"
"\n"
"/*controls*/\n"
"\n"
"#SettingsForm QPushButton{\n"
"	font: 700 10pt \"Aux Mono\";\n"
"	color: #bebebe;\n"
"	background-color:#3b3b3e;\n"
"	border-radius: 0px;\n"
"	padding: 0px 4px 0px 4px;\n"
"}\n"
"#SettingsForm QPushButton:hover {\n"
"	background-color:#515153;\n"
"}\n"
"#SettingsForm QPushButton:pressed {\n"
"	background-color:#1e1e20;\n"
"}\n"
"#SettingsForm #button{\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#SettingsForm QComboBox{\n"
"	font: 700 10pt \"Aux Mono\";\n"
"	color: #bebebe;\n"
"	backgro"
                        "und-color:#3b3b3e;\n"
"	border-radius: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"#SettingsForm QComboBox:hover {\n"
"	background-color:#515153;\n"
"}\n"
"#SettingsForm QComboBox QListView {\n"
"    background-color: #212124;\n"
"	outline: none;\n"
"	border-radius: 5px;\n"
"	border:none;\n"
"}\n"
"#SettingsForm QComboBox QListView:item {\n"
"    min-height: 27px;\n"
"    padding: 2px 10px;\n"
"	margin:3px;\n"
"	border-radius: 5px;\n"
"}\n"
"#SettingsForm QComboBox QListView:item:hover {\n"
"    background-color:#515153;\n"
"	outline: none;\n"
"	border:none;\n"
"}\n"
"#SettingsForm QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/chevron-down-dark.svg);\n"
"	width: 14px;\n"
"	height: 14px;\n"
"	padding-right: 10px;\n"
"}\n"
"#SettingsForm QComboBox:drop-down {\n"
"    border: 0px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"#SettingsForm QLineEdit{\n"
"	font: 700 10pt \"Aux Mono\";\n"
"	color: #bcbcbc;\n"
"	background-color:#3b3b3e;\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
""
                        "}\n"
"#SettingsForm QLineEdit:focus {\n"
"	color: #bebebe;\n"
"}\n"
"#SettingsForm QLineEdit:hover {\n"
"	background-color:#515153;\n"
"}\n"
"#SettingsForm #numbers_2 QDoubleSpinBox,\n"
"#SettingsForm #numbers QSpinBox{\n"
"	font: 700 10pt \"Aux Mono\";\n"
"	color: #bebebe;\n"
"	background-color:#3b3b3e;\n"
"	border-left: 0px;\n"
"	border-right:0px;\n"
"	text-align: center;\n"
"}\n"
"#SettingsForm #numbers_2 #plus_2,\n"
"#SettingsForm #numbers #plus{\n"
"	border-left: 0px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#SettingsForm #numbers_2 #minus_2,\n"
"#SettingsForm #numbers #minus{\n"
"	border-right: 0px;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"/* toggle */\n"
"\n"
"#SettingsForm #off {\n"
"	border-right: 0px;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"#SettingsForm #on {\n"
"	border-left: 0px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"#SettingsF"
                        "orm #off:checked {\n"
"	font: 900 10pt \"Aux Mono\";\n"
"	background-color: #4c272a;\n"
"	border: 1px solid #261315;\n"
"}\n"
"#SettingsForm #on:checked {\n"
"	font: 900 10pt \"Aux Mono\";\n"
"	background-color: #627254;\n"
"	border: 1px solid #21261c;\n"
"}\n"
"\n"
"/* icons */\n"
"\n"
"#goToSettingsButton{\n"
"	qproperty-iconSize: 14px;\n"
"	icon: url(:/icons/icons/settings-dark.svg);\n"
"}\n"
"#openJsonSettingsButton{\n"
"	icon: url(:/icons/icons/file-dark.svg);\n"
"}\n"
"#restartAppButton{\n"
"	icon: url(:/icons/icons/refresh-dark.svg);\n"
"}\n"
"#goToHomeButton{\n"
"	icon: url(:/icons/icons/arrow-left-dark.svg);\n"
"}\n"
"#smallModeButton{\n"
"	qproperty-iconSize: 18px;\n"
"	icon: url(:/icons/icons/chevron-left-dark.svg);\n"
"}\n"
"#connectionPanelButton{\n"
"	icon: url(:/icons/icons/radio-dark.svg);\n"
"}\n"
"#reconnectButton{\n"
"	qproperty-iconSize: 14px;\n"
"	icon: url(:/icons/icons/unlock-dark.svg);\n"
"}\n"
"#reconnectButton:checked{\n"
"	icon: url(:/icons/icons/lock-dark.svg);\n"
"}\n"
"#notificati"
                        "onsButton{\n"
"	qproperty-iconSize: 14px;\n"
"	icon: url(:/icons/icons/bell-dark.svg);\n"
"}\n"
"#autoScrollButton{\n"
"	qproperty-iconSize: 14px;\n"
"	icon: url(:/icons/icons/play-dark.svg);\n"
"}\n"
"#autoScrollButton:checked{\n"
"	qproperty-iconSize: 14px;\n"
"	icon: url(:/icons/icons/pause-dark.svg);\n"
"}\n"
"#clearButton{\n"
"	qproperty-iconSize: 14px;\n"
"	icon: url(:/icons/icons/bin-dark.svg);\n"
"}\n"
"#openRecordingFolder {\n"
"	icon: url(:/icons/icons/archive-dark.svg);\n"
"}\n"
"\n"
"/*TitleBar Do Not Delete*/\n"
"\n"
"#titleBarLabel{\n"
"	color: #18181B;\n"
"	font: 900 9pt \"Aux Mono\"; \n"
"	margin-top: 1px;\n"
"	margin-left: 5px;\n"
"}\n"
"#titleBarNormalButton{\n"
"	color: #383838;\n"
"	hover-color: #c5c5c5;\n"
"	pressed-color:#c5c5c5;\n"
"	hover-background-color: #3b3b3e;\n"
"	pressed-background-color:#1e1e20;\n"
"}\n"
"#titleBarCloseButton{\n"
"	color: #383838;\n"
"	hover-color: #c5c5c5;\n"
"	pressed-color:#c5c5c5;\n"
"	hover-background-color: #86444a;\n"
"	pressed-background-color:#4c272a;\n"
""
                        "}")
        self.actionExample = QAction(MainWindow)
        self.actionExample.setObjectName(u"actionExample")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBarFrame = QFrame(self.centralwidget)
        self.titleBarFrame.setObjectName(u"titleBarFrame")
        self.titleBarFrame.setMinimumSize(QSize(0, 32))
        self.titleBarFrame.setMaximumSize(QSize(16777215, 32))
        self.titleBarFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.titleBarFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.titleBarFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(875, 11, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.titleBarFrame)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 1))
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line)

        self.mainContainerFrame = QFrame(self.centralwidget)
        self.mainContainerFrame.setObjectName(u"mainContainerFrame")
        self.mainContainerFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.mainContainerFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.mainContainerFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QStackedWidget(self.mainContainerFrame)
        self.mainPages.setObjectName(u"mainPages")
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.verticalLayout_2 = QVBoxLayout(self.mainPage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pageContainer = QFrame(self.mainPage)
        self.pageContainer.setObjectName(u"pageContainer")
        self.pageContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pageContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.pageContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mainPageSideBarContainer = QFrame(self.pageContainer)
        self.mainPageSideBarContainer.setObjectName(u"mainPageSideBarContainer")
        self.mainPageSideBarContainer.setMinimumSize(QSize(280, 0))
        self.mainPageSideBarContainer.setMaximumSize(QSize(280, 16777215))
        self.mainPageSideBarContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.mainPageSideBarContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.mainPageSideBarContainer)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.topButtons = QFrame(self.mainPageSideBarContainer)
        self.topButtons.setObjectName(u"topButtons")
        self.topButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.topButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.topButtons)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 0, 5, 0)
        self.recordButton = QPushButton(self.topButtons)
        self.recordButton.setObjectName(u"recordButton")
        self.recordButton.setMinimumSize(QSize(0, 32))
        self.recordButton.setMaximumSize(QSize(16777215, 32))
        self.recordButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.recordButton.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.recordButton)


        self.verticalLayout_3.addWidget(self.topButtons)

        self.line_7 = QFrame(self.mainPageSideBarContainer)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMinimumSize(QSize(0, 1))
        self.line_7.setMaximumSize(QSize(16777215, 1))
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_7)

        self.topTelemetry = QFrame(self.mainPageSideBarContainer)
        self.topTelemetry.setObjectName(u"topTelemetry")
        self.topTelemetry.setFrameShape(QFrame.Shape.NoFrame)
        self.topTelemetry.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.topTelemetry)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 0, 5, 0)
        self.stateLabel = QLabel(self.topTelemetry)
        self.stateLabel.setObjectName(u"stateLabel")
        self.stateLabel.setMinimumSize(QSize(0, 39))
        self.stateLabel.setMaximumSize(QSize(16777215, 39))
        self.stateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.stateLabel)


        self.verticalLayout_3.addWidget(self.topTelemetry)

        self.tlmFramesContainer = QFrame(self.mainPageSideBarContainer)
        self.tlmFramesContainer.setObjectName(u"tlmFramesContainer")
        self.tlmFramesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.tlmFramesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.tlmFramesContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 0, 5, 0)
        self.mainTlm = QFrame(self.tlmFramesContainer)
        self.mainTlm.setObjectName(u"mainTlm")
        self.mainTlm.setFrameShape(QFrame.Shape.NoFrame)
        self.mainTlm.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.mainTlm)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.mainTlmContainer = QGridLayout()
        self.mainTlmContainer.setSpacing(5)
        self.mainTlmContainer.setObjectName(u"mainTlmContainer")

        self.verticalLayout_13.addLayout(self.mainTlmContainer)


        self.verticalLayout_12.addWidget(self.mainTlm)

        self.bigTlm = QFrame(self.tlmFramesContainer)
        self.bigTlm.setObjectName(u"bigTlm")
        self.bigTlm.setFrameShape(QFrame.Shape.NoFrame)
        self.bigTlm.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.bigTlm)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.bigTlmContainer = QGridLayout()
        self.bigTlmContainer.setSpacing(5)
        self.bigTlmContainer.setObjectName(u"bigTlmContainer")

        self.verticalLayout_14.addLayout(self.bigTlmContainer)


        self.verticalLayout_12.addWidget(self.bigTlm)


        self.verticalLayout_3.addWidget(self.tlmFramesContainer)

        self.line_8 = QFrame(self.mainPageSideBarContainer)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMinimumSize(QSize(0, 1))
        self.line_8.setMaximumSize(QSize(16777215, 1))
        self.line_8.setFrameShadow(QFrame.Shadow.Plain)
        self.line_8.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_3.addWidget(self.line_8)

        self.dashboarDScroolArea = QScrollArea(self.mainPageSideBarContainer)
        self.dashboarDScroolArea.setObjectName(u"dashboarDScroolArea")
        self.dashboarDScroolArea.setFrameShape(QFrame.Shape.NoFrame)
        self.dashboarDScroolArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.dashboarDScroolArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 280, 288))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.scrollTlmContainer = QFrame(self.scrollAreaWidgetContents)
        self.scrollTlmContainer.setObjectName(u"scrollTlmContainer")
        self.scrollTlmContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollTlmContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.scrollTlmContainer)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 0, 5, 0)
        self.secondTlm = QFrame(self.scrollTlmContainer)
        self.secondTlm.setObjectName(u"secondTlm")
        self.secondTlm.setFrameShape(QFrame.Shape.NoFrame)
        self.secondTlm.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.secondTlm)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.secondTlmContainer = QGridLayout()
        self.secondTlmContainer.setSpacing(5)
        self.secondTlmContainer.setObjectName(u"secondTlmContainer")

        self.verticalLayout_16.addLayout(self.secondTlmContainer)


        self.verticalLayout_18.addWidget(self.secondTlm)

        self.buttonTlm = QFrame(self.scrollTlmContainer)
        self.buttonTlm.setObjectName(u"buttonTlm")
        self.buttonTlm.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonTlm.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.buttonTlm)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.buttonTlmContainer = QGridLayout()
        self.buttonTlmContainer.setSpacing(5)
        self.buttonTlmContainer.setObjectName(u"buttonTlmContainer")

        self.verticalLayout_15.addLayout(self.buttonTlmContainer)


        self.verticalLayout_18.addWidget(self.buttonTlm)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_4)


        self.verticalLayout_17.addWidget(self.scrollTlmContainer)

        self.dashboarDScroolArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.dashboarDScroolArea)

        self.connectionManagementFrame = QFrame(self.mainPageSideBarContainer)
        self.connectionManagementFrame.setObjectName(u"connectionManagementFrame")
        self.connectionManagementFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.connectionManagementFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.connectionManagementFrame)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line_6 = QFrame(self.connectionManagementFrame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(0, 1))
        self.line_6.setMaximumSize(QSize(16777215, 1))
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_6)

        self.connControlsContainer = QFrame(self.connectionManagementFrame)
        self.connControlsContainer.setObjectName(u"connControlsContainer")
        self.connControlsContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.connControlsContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.connControlsContainer)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 0, 5, 0)
        self.connCombosContainer = QFrame(self.connControlsContainer)
        self.connCombosContainer.setObjectName(u"connCombosContainer")
        self.connCombosContainer.setMinimumSize(QSize(0, 27))
        self.connCombosContainer.setMaximumSize(QSize(16777215, 27))
        self.connCombosContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.connCombosContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.connCombosContainer)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ports = QComboBox(self.connCombosContainer)
        self.ports.setObjectName(u"ports")
        self.ports.setMinimumSize(QSize(0, 27))
        self.ports.setMaximumSize(QSize(16777215, 27))
        self.ports.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.ports)

        self.bauds = QComboBox(self.connCombosContainer)
        self.bauds.setObjectName(u"bauds")
        self.bauds.setMinimumSize(QSize(0, 27))
        self.bauds.setMaximumSize(QSize(16777215, 27))
        self.bauds.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.bauds)

        self.reconnectButton = QPushButton(self.connCombosContainer)
        self.reconnectButton.setObjectName(u"reconnectButton")
        self.reconnectButton.setMinimumSize(QSize(32, 27))
        self.reconnectButton.setMaximumSize(QSize(32, 27))
        self.reconnectButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.reconnectButton.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.reconnectButton)


        self.verticalLayout_9.addWidget(self.connCombosContainer)

        self.connectButton = QPushButton(self.connControlsContainer)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setMinimumSize(QSize(0, 32))
        self.connectButton.setMaximumSize(QSize(16777215, 32))
        self.connectButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.connectButton.setCheckable(True)

        self.verticalLayout_9.addWidget(self.connectButton)


        self.verticalLayout_4.addWidget(self.connControlsContainer)


        self.verticalLayout_3.addWidget(self.connectionManagementFrame)

        self.line_5 = QFrame(self.mainPageSideBarContainer)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(0, 1))
        self.line_5.setMaximumSize(QSize(16777215, 1))
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.dasboardMainButtons = QFrame(self.mainPageSideBarContainer)
        self.dasboardMainButtons.setObjectName(u"dasboardMainButtons")
        self.dasboardMainButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.dasboardMainButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.dasboardMainButtons)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.smallModeButton = QPushButton(self.dasboardMainButtons)
        self.smallModeButton.setObjectName(u"smallModeButton")
        self.smallModeButton.setMinimumSize(QSize(0, 38))
        self.smallModeButton.setMaximumSize(QSize(16777215, 38))
        self.smallModeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.smallModeButton.setCheckable(True)
        self.smallModeButton.setChecked(False)

        self.horizontalLayout_7.addWidget(self.smallModeButton)

        self.goToSettingsButton = QPushButton(self.dasboardMainButtons)
        self.goToSettingsButton.setObjectName(u"goToSettingsButton")
        self.goToSettingsButton.setMinimumSize(QSize(0, 38))
        self.goToSettingsButton.setMaximumSize(QSize(16777215, 38))
        self.goToSettingsButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.goToSettingsButton)

        self.connectionPanelButton = QPushButton(self.dasboardMainButtons)
        self.connectionPanelButton.setObjectName(u"connectionPanelButton")
        self.connectionPanelButton.setMinimumSize(QSize(0, 38))
        self.connectionPanelButton.setMaximumSize(QSize(16777215, 38))
        self.connectionPanelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.connectionPanelButton.setCheckable(True)
        self.connectionPanelButton.setChecked(True)

        self.horizontalLayout_7.addWidget(self.connectionPanelButton)


        self.verticalLayout_3.addWidget(self.dasboardMainButtons)


        self.horizontalLayout_4.addWidget(self.mainPageSideBarContainer)

        self.line_3 = QFrame(self.pageContainer)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(1, 0))
        self.line_3.setMaximumSize(QSize(1, 16777215))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_3)

        self.mainPageContainerFrame = QFrame(self.pageContainer)
        self.mainPageContainerFrame.setObjectName(u"mainPageContainerFrame")
        self.mainPageContainerFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.mainPageContainerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.mainPageContainerFrame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.mainPageContainerFrame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(2)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.topLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.topLayout.setObjectName(u"topLayout")
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        self.topContainer = QFrame(self.verticalLayoutWidget)
        self.topContainer.setObjectName(u"topContainer")
        self.topContainer.setMinimumSize(QSize(0, 472))
        self.topContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.topContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.topContainer)
        self.verticalLayout_24.setSpacing(1)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(1, 1, 1, 1)
        self.graphLayout = QVBoxLayout()
        self.graphLayout.setObjectName(u"graphLayout")

        self.verticalLayout_24.addLayout(self.graphLayout)


        self.topLayout.addWidget(self.topContainer)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.bottomLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.bottomLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.bottomLayout.setContentsMargins(0, 0, 0, 0)
        self.bottomContainer = QFrame(self.verticalLayoutWidget_2)
        self.bottomContainer.setObjectName(u"bottomContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomContainer.sizePolicy().hasHeightForWidth())
        self.bottomContainer.setSizePolicy(sizePolicy)
        self.bottomContainer.setMaximumSize(QSize(16777215, 400))
        self.bottomContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.bottomContainer)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.line_9 = QFrame(self.bottomContainer)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMinimumSize(QSize(0, 1))
        self.line_9.setMaximumSize(QSize(16777215, 1))
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_20.addWidget(self.line_9)

        self.terminalContainer = QFrame(self.bottomContainer)
        self.terminalContainer.setObjectName(u"terminalContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.terminalContainer.sizePolicy().hasHeightForWidth())
        self.terminalContainer.setSizePolicy(sizePolicy1)
        self.terminalContainer.setMinimumSize(QSize(0, 74))
        self.terminalContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.terminalContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.terminalContainer)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 6, 5, 5)
        self.terminal = QTextBrowser(self.terminalContainer)
        self.terminal.setObjectName(u"terminal")
        self.terminal.setFrameShape(QFrame.Shape.NoFrame)
        self.terminal.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.terminal.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.terminal.setOpenLinks(False)

        self.verticalLayout_21.addWidget(self.terminal)


        self.verticalLayout_20.addWidget(self.terminalContainer)

        self.line_10 = QFrame(self.bottomContainer)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setMinimumSize(QSize(0, 1))
        self.line_10.setMaximumSize(QSize(16777215, 1))
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_20.addWidget(self.line_10)

        self.inputContainer = QFrame(self.bottomContainer)
        self.inputContainer.setObjectName(u"inputContainer")
        self.inputContainer.setMinimumSize(QSize(0, 48))
        self.inputContainer.setMaximumSize(QSize(16777215, 38))
        self.inputContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.inputContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.inputContainer)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 5, 10)
        self.terminalInput = QLineEdit(self.inputContainer)
        self.terminalInput.setObjectName(u"terminalInput")
        self.terminalInput.setMinimumSize(QSize(0, 38))
        self.terminalInput.setMaximumSize(QSize(16777215, 38))

        self.horizontalLayout_10.addWidget(self.terminalInput)

        self.clearButton = QPushButton(self.inputContainer)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setMinimumSize(QSize(32, 27))
        self.clearButton.setMaximumSize(QSize(32, 27))
        self.clearButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.clearButton)

        self.notificationsButton = QPushButton(self.inputContainer)
        self.notificationsButton.setObjectName(u"notificationsButton")
        self.notificationsButton.setMinimumSize(QSize(32, 27))
        self.notificationsButton.setMaximumSize(QSize(32, 27))
        self.notificationsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.notificationsButton.setCheckable(True)
        self.notificationsButton.setChecked(False)

        self.horizontalLayout_10.addWidget(self.notificationsButton)

        self.autoScrollButton = QPushButton(self.inputContainer)
        self.autoScrollButton.setObjectName(u"autoScrollButton")
        self.autoScrollButton.setMinimumSize(QSize(32, 27))
        self.autoScrollButton.setMaximumSize(QSize(32, 27))
        self.autoScrollButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.autoScrollButton.setCheckable(True)
        self.autoScrollButton.setChecked(True)

        self.horizontalLayout_10.addWidget(self.autoScrollButton)


        self.verticalLayout_20.addWidget(self.inputContainer)


        self.bottomLayout.addWidget(self.bottomContainer)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.verticalLayout_22.addWidget(self.splitter)


        self.horizontalLayout_4.addWidget(self.mainPageContainerFrame)


        self.verticalLayout_2.addWidget(self.pageContainer)

        self.mainPages.addWidget(self.mainPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.horizontalLayout_5 = QHBoxLayout(self.settingsPage)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.settingsPageSideBarContainer = QFrame(self.settingsPage)
        self.settingsPageSideBarContainer.setObjectName(u"settingsPageSideBarContainer")
        self.settingsPageSideBarContainer.setMinimumSize(QSize(50, 0))
        self.settingsPageSideBarContainer.setMaximumSize(QSize(50, 16777215))
        self.settingsPageSideBarContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.settingsPageSideBarContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.settingsPageSideBarContainer)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.goToHomeButton = QPushButton(self.settingsPageSideBarContainer)
        self.goToHomeButton.setObjectName(u"goToHomeButton")
        self.goToHomeButton.setMinimumSize(QSize(42, 38))
        self.goToHomeButton.setMaximumSize(QSize(42, 38))
        self.goToHomeButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.goToHomeButton)

        self.verticalSpacer_2 = QSpacerItem(20, 366, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.openRecordingFolder = QPushButton(self.settingsPageSideBarContainer)
        self.openRecordingFolder.setObjectName(u"openRecordingFolder")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(42)
        sizePolicy2.setVerticalStretch(38)
        sizePolicy2.setHeightForWidth(self.openRecordingFolder.sizePolicy().hasHeightForWidth())
        self.openRecordingFolder.setSizePolicy(sizePolicy2)
        self.openRecordingFolder.setMinimumSize(QSize(42, 38))
        self.openRecordingFolder.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.openRecordingFolder)

        self.openJsonSettingsButton = QPushButton(self.settingsPageSideBarContainer)
        self.openJsonSettingsButton.setObjectName(u"openJsonSettingsButton")
        self.openJsonSettingsButton.setMinimumSize(QSize(42, 38))
        self.openJsonSettingsButton.setMaximumSize(QSize(42, 38))
        self.openJsonSettingsButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.openJsonSettingsButton)

        self.restartAppButton = QPushButton(self.settingsPageSideBarContainer)
        self.restartAppButton.setObjectName(u"restartAppButton")
        self.restartAppButton.setMinimumSize(QSize(42, 38))
        self.restartAppButton.setMaximumSize(QSize(42, 38))
        self.restartAppButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.restartAppButton)


        self.horizontalLayout_5.addWidget(self.settingsPageSideBarContainer)

        self.line_4 = QFrame(self.settingsPage)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(1, 0))
        self.line_4.setMaximumSize(QSize(1, 16777215))
        self.line_4.setFrameShadow(QFrame.Shadow.Plain)
        self.line_4.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_5.addWidget(self.line_4)

        self.settingsPageContainerFrame = QFrame(self.settingsPage)
        self.settingsPageContainerFrame.setObjectName(u"settingsPageContainerFrame")
        self.settingsPageContainerFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.settingsPageContainerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.settingsPageContainerFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.settingsContainer = QFrame(self.settingsPageContainerFrame)
        self.settingsContainer.setObjectName(u"settingsContainer")
        self.settingsContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.settingsContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.settingsContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.settingsScrollContainer = QFrame(self.settingsContainer)
        self.settingsScrollContainer.setObjectName(u"settingsScrollContainer")
        self.settingsScrollContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.settingsScrollContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.settingsScrollContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.settingsScroll = QScrollArea(self.settingsScrollContainer)
        self.settingsScroll.setObjectName(u"settingsScroll")
        self.settingsScroll.setFrameShape(QFrame.Shape.NoFrame)
        self.settingsScroll.setFrameShadow(QFrame.Shadow.Plain)
        self.settingsScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.settingsScroll.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.settingsScroll.setWidgetResizable(True)
        self.settingsScroll.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.settinsScrollContent = QWidget()
        self.settinsScrollContent.setObjectName(u"settinsScrollContent")
        self.settinsScrollContent.setGeometry(QRect(0, 0, 120, 32))
        self.verticalLayout_10 = QVBoxLayout(self.settinsScrollContent)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(50, 20, 50, 10)
        self.settingsLayout = QVBoxLayout()
        self.settingsLayout.setSpacing(10)
        self.settingsLayout.setObjectName(u"settingsLayout")

        self.verticalLayout_10.addLayout(self.settingsLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 530, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.settingsScroll.setWidget(self.settinsScrollContent)

        self.verticalLayout_8.addWidget(self.settingsScroll)


        self.verticalLayout_7.addWidget(self.settingsScrollContainer)

        self.settingsBottom = QFrame(self.settingsContainer)
        self.settingsBottom.setObjectName(u"settingsBottom")
        self.settingsBottom.setMinimumSize(QSize(0, 0))
        self.settingsBottom.setMaximumSize(QSize(16777215, 50))
        self.settingsBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.settingsBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.settingsBottom)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.settingsInfoLabel = QLabel(self.settingsBottom)
        self.settingsInfoLabel.setObjectName(u"settingsInfoLabel")
        self.settingsInfoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.settingsInfoLabel)

        self.horizontalSpacer_4 = QSpacerItem(387, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addWidget(self.settingsBottom)


        self.verticalLayout_6.addWidget(self.settingsContainer)


        self.horizontalLayout_5.addWidget(self.settingsPageContainerFrame)

        self.mainPages.addWidget(self.settingsPage)

        self.horizontalLayout_2.addWidget(self.mainPages)


        self.verticalLayout.addWidget(self.mainContainerFrame)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 1))
        self.line_2.setMaximumSize(QSize(16777215, 1))
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line_2)

        self.customStatusBarFrame = QFrame(self.centralwidget)
        self.customStatusBarFrame.setObjectName(u"customStatusBarFrame")
        self.customStatusBarFrame.setMinimumSize(QSize(0, 17))
        self.customStatusBarFrame.setMaximumSize(QSize(16777215, 17))
        self.customStatusBarFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.customStatusBarFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.customStatusBarFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 0, 8, 0)
        self.statusLabel = QLabel(self.customStatusBarFrame)
        self.statusLabel.setObjectName(u"statusLabel")

        self.horizontalLayout.addWidget(self.statusLabel)

        self.horizontalSpacer = QSpacerItem(821, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.versionLabel = QLabel(self.customStatusBarFrame)
        self.versionLabel.setObjectName(u"versionLabel")

        self.horizontalLayout.addWidget(self.versionLabel)


        self.verticalLayout.addWidget(self.customStatusBarFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExample.setText(QCoreApplication.translate("MainWindow", u"Example", None))
#if QT_CONFIG(tooltip)
        self.recordButton.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle Recording", None))
#endif // QT_CONFIG(tooltip)
        self.recordButton.setText(QCoreApplication.translate("MainWindow", u"RECORDING", None))
        self.stateLabel.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
#if QT_CONFIG(tooltip)
        self.ports.setToolTip(QCoreApplication.translate("MainWindow", u"Select Serial Port", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bauds.setToolTip(QCoreApplication.translate("MainWindow", u"Select Bauds", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.reconnectButton.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle AutoReconnect", None))
#endif // QT_CONFIG(tooltip)
        self.reconnectButton.setText("")
#if QT_CONFIG(tooltip)
        self.connectButton.setToolTip(QCoreApplication.translate("MainWindow", u"Connect To Serial Port", None))
#endif // QT_CONFIG(tooltip)
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
#if QT_CONFIG(tooltip)
        self.smallModeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Small Mode", None))
#endif // QT_CONFIG(tooltip)
        self.smallModeButton.setText("")
#if QT_CONFIG(tooltip)
        self.goToSettingsButton.setToolTip(QCoreApplication.translate("MainWindow", u"Open Settings", None))
#endif // QT_CONFIG(tooltip)
        self.goToSettingsButton.setText("")
#if QT_CONFIG(tooltip)
        self.connectionPanelButton.setToolTip(QCoreApplication.translate("MainWindow", u"Open Connection Panel", None))
#endif // QT_CONFIG(tooltip)
        self.connectionPanelButton.setText("")
        self.terminal.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Aux Mono'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.terminalInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here a message to send to the serial port", None))
#if QT_CONFIG(tooltip)
        self.clearButton.setToolTip(QCoreApplication.translate("MainWindow", u"Clear Terminal", None))
#endif // QT_CONFIG(tooltip)
        self.clearButton.setText("")
#if QT_CONFIG(tooltip)
        self.notificationsButton.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle Recent Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.notificationsButton.setText("")
#if QT_CONFIG(tooltip)
        self.autoScrollButton.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle AutoScroll", None))
#endif // QT_CONFIG(tooltip)
        self.autoScrollButton.setText("")
#if QT_CONFIG(tooltip)
        self.goToHomeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Go Back To Home", None))
#endif // QT_CONFIG(tooltip)
        self.goToHomeButton.setText("")
#if QT_CONFIG(tooltip)
        self.openRecordingFolder.setToolTip(QCoreApplication.translate("MainWindow", u"Open Recording Folder", None))
#endif // QT_CONFIG(tooltip)
        self.openRecordingFolder.setText("")
#if QT_CONFIG(tooltip)
        self.openJsonSettingsButton.setToolTip(QCoreApplication.translate("MainWindow", u"Open Settings As Json File", None))
#endif // QT_CONFIG(tooltip)
        self.openJsonSettingsButton.setText("")
#if QT_CONFIG(tooltip)
        self.restartAppButton.setToolTip(QCoreApplication.translate("MainWindow", u"Restart The Application", None))
#endif // QT_CONFIG(tooltip)
        self.restartAppButton.setText("")
        self.settingsInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Tecnoclub Elburgo Cansat \u00a9 2024 Waves", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"v0.0.1", None))
    # retranslateUi

