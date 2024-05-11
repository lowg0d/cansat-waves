# type: ignore
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)
from ..assets import src

class Ui_SettingsForm(object):
    def setupUi(self, SettingsForm):
        if not SettingsForm.objectName():
            SettingsForm.setObjectName(u"SettingsForm")
        SettingsForm.resize(1204, 70)
        SettingsForm.setMinimumSize(QSize(0, 70))
        SettingsForm.setMaximumSize(QSize(16777215, 70))
        SettingsForm.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(SettingsForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(SettingsForm)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.Shape.NoFrame)
        self.container.setFrameShadow(QFrame.Shadow.Plain)
        self.container.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.infoContainer = QFrame(self.container)
        self.infoContainer.setObjectName(u"infoContainer")
        self.infoContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.infoContainer.setFrameShadow(QFrame.Shadow.Plain)
        self.infoContainer.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.infoContainer)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.profile = QFrame(self.infoContainer)
        self.profile.setObjectName(u"profile")
        self.profile.setFrameShape(QFrame.Shape.NoFrame)
        self.profile.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.profile)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.profile_label = QLabel(self.profile)
        self.profile_label.setObjectName(u"profile_label")
        self.profile_label.setMinimumSize(QSize(55, 55))
        self.profile_label.setMaximumSize(QSize(55, 55))
        self.profile_label.setStyleSheet(u"")
        self.profile_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.profile_label)


        self.horizontalLayout_2.addWidget(self.profile)

        self.info = QFrame(self.infoContainer)
        self.info.setObjectName(u"info")
        self.info.setFrameShape(QFrame.Shape.NoFrame)
        self.info.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.info)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.name_restart = QFrame(self.info)
        self.name_restart.setObjectName(u"name_restart")
        self.name_restart.setFrameShape(QFrame.Shape.NoFrame)
        self.name_restart.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.name_restart)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.name = QLabel(self.name_restart)
        self.name.setObjectName(u"name")

        self.horizontalLayout_4.addWidget(self.name)

        self.restart = QLabel(self.name_restart)
        self.restart.setObjectName(u"restart")

        self.horizontalLayout_4.addWidget(self.restart)


        self.verticalLayout_2.addWidget(self.name_restart)

        self.description = QLabel(self.info)
        self.description.setObjectName(u"description")

        self.verticalLayout_2.addWidget(self.description)


        self.horizontalLayout_2.addWidget(self.info)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.infoContainer)

        self.controls = QFrame(self.container)
        self.controls.setObjectName(u"controls")
        self.controls.setFrameShape(QFrame.Shape.NoFrame)
        self.controls.setFrameShadow(QFrame.Shadow.Plain)
        self.controls.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.controls)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.string = QLineEdit(self.controls)
        self.string.setObjectName(u"string")
        self.string.setMinimumSize(QSize(150, 33))
        self.string.setMaximumSize(QSize(150, 33))

        self.horizontalLayout_5.addWidget(self.string)

        self.combo = QComboBox(self.controls)
        self.combo.setObjectName(u"combo")
        self.combo.setMinimumSize(QSize(150, 33))
        self.combo.setMaximumSize(QSize(150, 33))
        self.combo.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.combo.setAutoFillBackground(False)
        self.combo.setFrame(False)

        self.horizontalLayout_5.addWidget(self.combo)

        self.button = QPushButton(self.controls)
        self.button.setObjectName(u"button")
        self.button.setMinimumSize(QSize(150, 33))
        self.button.setMaximumSize(QSize(150, 33))
        self.button.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.button)

        self.toggle = QFrame(self.controls)
        self.toggle.setObjectName(u"toggle")
        self.toggle.setMinimumSize(QSize(150, 0))
        self.toggle.setMaximumSize(QSize(150, 16777215))
        self.toggle.setFrameShape(QFrame.Shape.NoFrame)
        self.toggle.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.toggle)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.off = QPushButton(self.toggle)
        self.off.setObjectName(u"off")
        self.off.setMinimumSize(QSize(0, 33))
        self.off.setCursor(QCursor(Qt.PointingHandCursor))
        self.off.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.off)

        self.on = QPushButton(self.toggle)
        self.on.setObjectName(u"on")
        self.on.setMinimumSize(QSize(0, 33))
        self.on.setCursor(QCursor(Qt.PointingHandCursor))
        self.on.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.on)


        self.horizontalLayout_5.addWidget(self.toggle)

        self.numbers = QFrame(self.controls)
        self.numbers.setObjectName(u"numbers")
        self.numbers.setMinimumSize(QSize(150, 33))
        self.numbers.setMaximumSize(QSize(150, 33))
        self.numbers.setFrameShape(QFrame.Shape.NoFrame)
        self.numbers.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.numbers)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, -1)
        self.minus = QPushButton(self.numbers)
        self.minus.setObjectName(u"minus")
        self.minus.setMinimumSize(QSize(40, 33))
        self.minus.setMaximumSize(QSize(40, 33))
        self.minus.setCursor(QCursor(Qt.PointingHandCursor))
        self.minus.setFlat(True)

        self.horizontalLayout_6.addWidget(self.minus)

        self.int_2 = QSpinBox(self.numbers)
        self.int_2.setObjectName(u"int_2")
        self.int_2.setEnabled(True)
        self.int_2.setMinimumSize(QSize(70, 33))
        self.int_2.setMaximumSize(QSize(70, 33))
        self.int_2.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.int_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.int_2.setStyleSheet(u"")
        self.int_2.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.int_2.setWrapping(False)
        self.int_2.setFrame(False)
        self.int_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.int_2.setReadOnly(False)
        self.int_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.int_2.setKeyboardTracking(False)
        self.int_2.setProperty("showGroupSeparator", False)
        self.int_2.setMinimum(-100000)
        self.int_2.setMaximum(100000)

        self.horizontalLayout_6.addWidget(self.int_2)

        self.plus = QPushButton(self.numbers)
        self.plus.setObjectName(u"plus")
        self.plus.setMinimumSize(QSize(40, 33))
        self.plus.setMaximumSize(QSize(40, 33))
        self.plus.setCursor(QCursor(Qt.PointingHandCursor))
        self.plus.setFlat(True)

        self.horizontalLayout_6.addWidget(self.plus)


        self.horizontalLayout_5.addWidget(self.numbers)

        self.numbers_2 = QFrame(self.controls)
        self.numbers_2.setObjectName(u"numbers_2")
        self.numbers_2.setMinimumSize(QSize(150, 33))
        self.numbers_2.setMaximumSize(QSize(150, 33))
        self.numbers_2.setFrameShape(QFrame.Shape.NoFrame)
        self.numbers_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.numbers_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.minus_2 = QPushButton(self.numbers_2)
        self.minus_2.setObjectName(u"minus_2")
        self.minus_2.setMinimumSize(QSize(40, 33))
        self.minus_2.setMaximumSize(QSize(40, 33))
        self.minus_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.minus_2.setFlat(True)

        self.horizontalLayout_8.addWidget(self.minus_2)

        self.float_2 = QDoubleSpinBox(self.numbers_2)
        self.float_2.setObjectName(u"float_2")
        self.float_2.setMinimumSize(QSize(70, 33))
        self.float_2.setMaximumSize(QSize(70, 33))
        self.float_2.setFrame(False)
        self.float_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.float_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.float_2.setDecimals(2)
        self.float_2.setMinimum(-100000.000000000000000)
        self.float_2.setMaximum(100000.000000000000000)

        self.horizontalLayout_8.addWidget(self.float_2)

        self.plus_2 = QPushButton(self.numbers_2)
        self.plus_2.setObjectName(u"plus_2")
        self.plus_2.setMinimumSize(QSize(40, 33))
        self.plus_2.setMaximumSize(QSize(40, 33))
        self.plus_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.plus_2.setFlat(True)

        self.horizontalLayout_8.addWidget(self.plus_2)


        self.horizontalLayout_5.addWidget(self.numbers_2)


        self.horizontalLayout.addWidget(self.controls)


        self.verticalLayout.addWidget(self.container)


        self.retranslateUi(SettingsForm)
        self.plus.clicked.connect(self.int_2.stepUp)
        self.minus.clicked.connect(self.int_2.stepDown)
        self.plus_2.clicked.connect(self.float_2.stepUp)
        self.minus_2.clicked.connect(self.float_2.stepDown)

        QMetaObject.connectSlotsByName(SettingsForm)
    # setupUi

    def retranslateUi(self, SettingsForm):
        SettingsForm.setWindowTitle(QCoreApplication.translate("SettingsForm", u"Form", None))
        self.profile_label.setText(QCoreApplication.translate("SettingsForm", u"?", None))
        self.name.setText(QCoreApplication.translate("SettingsForm", u"Name", None))
        self.restart.setText(QCoreApplication.translate("SettingsForm", u"[!] NEED RESTART TO APLY", None))
        self.description.setText(QCoreApplication.translate("SettingsForm", u"Description", None))
        self.string.setInputMask("")
        self.string.setText("")
        self.string.setPlaceholderText(QCoreApplication.translate("SettingsForm", u"Text Here", None))
        self.button.setText(QCoreApplication.translate("SettingsForm", u"BUTTON", None))
        self.off.setText(QCoreApplication.translate("SettingsForm", u"OFF", None))
        self.on.setText(QCoreApplication.translate("SettingsForm", u"ON", None))
        self.minus.setText(QCoreApplication.translate("SettingsForm", u"-", None))
        self.plus.setText(QCoreApplication.translate("SettingsForm", u"+", None))
        self.minus_2.setText(QCoreApplication.translate("SettingsForm", u"-", None))
        self.plus_2.setText(QCoreApplication.translate("SettingsForm", u"+", None))
    # retranslateUi

