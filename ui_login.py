# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import MoonLightIcons_rc

class Ui_Login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(644, 581)
        Form.setStyleSheet(u"background-color: rgb(1, 68, 143);\n"
"border-image: url(:/Outers/stars.png);")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(500, 300))
        self.frame_3.setStyleSheet(u"\n"
"border-image: url(:/Logo/MoonLight.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 1, 1, 2, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgba(0, 0, 0, 50);\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txtlogin = QLineEdit(self.widget)
        self.txtlogin.setObjectName(u"txtlogin")
        self.txtlogin.setStyleSheet(u"\n"
"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.txtlogin.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txtlogin)

        self.txt_password = QLineEdit(self.widget)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.txt_password.setStyleSheet(u"\n"
"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_password)

        self.btn_login = QPushButton(self.widget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgba(196, 204, 236, 100);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.btn_login)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.txtlogin.setText("")
        self.txtlogin.setPlaceholderText(QCoreApplication.translate("Form", u"User", None))
        self.txt_password.setText("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"Logar", None))
    # retranslateUi

