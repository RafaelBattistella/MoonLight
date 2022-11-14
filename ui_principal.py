# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Principal.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import MoonLightIcons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(744, 678)
        MainWindow.setStyleSheet(u"background-color: rgb(1, 68, 143);\n"
"border-image: url(:/Outers/stars.png);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_36 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.LateralBar = QFrame(self.centralwidget)
        self.LateralBar.setObjectName(u"LateralBar")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LateralBar.sizePolicy().hasHeightForWidth())
        self.LateralBar.setSizePolicy(sizePolicy)
        self.LateralBar.setMinimumSize(QSize(150, 0))
        self.LateralBar.setStyleSheet(u"background-color: rgb(172, 180, 212);")
        self.LateralBar.setFrameShape(QFrame.StyledPanel)
        self.LateralBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LateralBar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.LateralBar)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.bnt_Perfil = QPushButton(self.frame_2)
        self.bnt_Perfil.setObjectName(u"bnt_Perfil")
        self.bnt_Perfil.setGeometry(QRect(40, 10, 51, 81))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bnt_Perfil.sizePolicy().hasHeightForWidth())
        self.bnt_Perfil.setSizePolicy(sizePolicy2)
        self.bnt_Perfil.setMinimumSize(QSize(30, 50))
        self.bnt_Perfil.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	border-image: url(:/Buttons/HomemPNG.png);\n"
"\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/HomemSombra.png);\n"
"\n"
"}\n"
"")
        self.bnt_Perfil.setIconSize(QSize(5, 30))
        self.lb_Perfil = QLabel(self.frame_2)
        self.lb_Perfil.setObjectName(u"lb_Perfil")
        self.lb_Perfil.setEnabled(True)
        self.lb_Perfil.setGeometry(QRect(40, 10, 51, 81))
        self.lb_Perfil.setStyleSheet(u"border-image: url(:/Buttons/HomemPNG.png);")

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.LateralBar)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(30)
        sizePolicy3.setVerticalStretch(50)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bnt_inicio = QPushButton(self.frame)
        self.bnt_inicio.setObjectName(u"bnt_inicio")
        self.bnt_inicio.setMinimumSize(QSize(0, 40))
        self.bnt_inicio.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(196, 204, 236);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"olor: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.bnt_inicio)

        self.bnt_cadastro = QPushButton(self.frame)
        self.bnt_cadastro.setObjectName(u"bnt_cadastro")
        self.bnt_cadastro.setMinimumSize(QSize(0, 40))
        self.bnt_cadastro.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(196, 204, 236);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"olor: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.bnt_cadastro)

        self.bnt_OS = QPushButton(self.frame)
        self.bnt_OS.setObjectName(u"bnt_OS")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.bnt_OS.sizePolicy().hasHeightForWidth())
        self.bnt_OS.setSizePolicy(sizePolicy4)
        self.bnt_OS.setMinimumSize(QSize(0, 40))
        self.bnt_OS.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(196, 204, 236);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"olor: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.bnt_OS)

        self.bnt_estoque = QPushButton(self.frame)
        self.bnt_estoque.setObjectName(u"bnt_estoque")
        sizePolicy4.setHeightForWidth(self.bnt_estoque.sizePolicy().hasHeightForWidth())
        self.bnt_estoque.setSizePolicy(sizePolicy4)
        self.bnt_estoque.setMinimumSize(QSize(0, 40))
        self.bnt_estoque.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(196, 204, 236);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"olor: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.bnt_estoque)

        self.bnt_Sobre = QPushButton(self.frame)
        self.bnt_Sobre.setObjectName(u"bnt_Sobre")
        self.bnt_Sobre.setMinimumSize(QSize(0, 40))
        self.bnt_Sobre.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(196, 204, 236);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"olor: rgb(0, 0, 0);\n"
"\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.bnt_Sobre)


        self.verticalLayout_2.addWidget(self.frame)

        self.lg_lateral = QLabel(self.LateralBar)
        self.lg_lateral.setObjectName(u"lg_lateral")
        self.lg_lateral.setMinimumSize(QSize(0, 77))
        self.lg_lateral.setStyleSheet(u"border-image: url(:/Logo/MoonLight.png);")

        self.verticalLayout_2.addWidget(self.lg_lateral)


        self.horizontalLayout_36.addWidget(self.LateralBar)

        self.tl_geral = QStackedWidget(self.centralwidget)
        self.tl_geral.setObjectName(u"tl_geral")
        self.tl_geral.setEnabled(True)
        self.tl_inicio = QWidget()
        self.tl_inicio.setObjectName(u"tl_inicio")
        self.tl_inicio.setEnabled(True)
        self.gridLayout = QGridLayout(self.tl_inicio)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.tl_inicio)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_lua = QFrame(self.frame_5)
        self.lb_lua.setObjectName(u"lb_lua")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lb_lua.sizePolicy().hasHeightForWidth())
        self.lb_lua.setSizePolicy(sizePolicy5)
        self.lb_lua.setMinimumSize(QSize(500, 500))
        self.lb_lua.setStyleSheet(u"border-image: url(:/Outers/LuaC.png);")
        self.lb_lua.setFrameShape(QFrame.StyledPanel)
        self.lb_lua.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.lb_lua)

        self.lb_moonlight = QLabel(self.frame_5)
        self.lb_moonlight.setObjectName(u"lb_moonlight")
        sizePolicy5.setHeightForWidth(self.lb_moonlight.sizePolicy().hasHeightForWidth())
        self.lb_moonlight.setSizePolicy(sizePolicy5)
        self.lb_moonlight.setMinimumSize(QSize(500, 50))
        self.lb_moonlight.setStyleSheet(u"font: 48pt \"MS Shell Dlg 2\";\n"
"color: rgb(196, 204, 236);")
        self.lb_moonlight.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_moonlight)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.tl_geral.addWidget(self.tl_inicio)
        self.tl_OS = QWidget()
        self.tl_OS.setObjectName(u"tl_OS")
        self.verticalLayout_7 = QVBoxLayout(self.tl_OS)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.tl_OS)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(10)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.bt_abrirOs = QPushButton(self.frame_8)
        self.bt_abrirOs.setObjectName(u"bt_abrirOs")
        sizePolicy5.setHeightForWidth(self.bt_abrirOs.sizePolicy().hasHeightForWidth())
        self.bt_abrirOs.setSizePolicy(sizePolicy5)
        self.bt_abrirOs.setMinimumSize(QSize(150, 150))
        self.bt_abrirOs.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrela.png);\n"
"\n"
"	\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrelaSombra.png);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.bt_abrirOs)

        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        sizePolicy6.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy6)

        self.horizontalLayout_2.addWidget(self.label_6)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.lb_Os = QLabel(self.frame_7)
        self.lb_Os.setObjectName(u"lb_Os")
        sizePolicy5.setHeightForWidth(self.lb_Os.sizePolicy().hasHeightForWidth())
        self.lb_Os.setSizePolicy(sizePolicy5)
        self.lb_Os.setMinimumSize(QSize(250, 250))
        self.lb_Os.setStyleSheet(u"border-image: url(:/Outers/LuaCrescente.png);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.lb_Os.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lb_Os)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        sizePolicy6.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy6)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.bt_fechaOs = QPushButton(self.frame_6)
        self.bt_fechaOs.setObjectName(u"bt_fechaOs")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(10)
        sizePolicy7.setVerticalStretch(50)
        sizePolicy7.setHeightForWidth(self.bt_fechaOs.sizePolicy().hasHeightForWidth())
        self.bt_fechaOs.setSizePolicy(sizePolicy7)
        self.bt_fechaOs.setMinimumSize(QSize(150, 150))
        self.bt_fechaOs.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrela.png);\n"
"\n"
"	\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrelaSombra.png);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.bt_fechaOs)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(10)
        sizePolicy8.setVerticalStretch(10)
        sizePolicy8.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy8)

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout_9.addWidget(self.frame_6)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.tl_geral.addWidget(self.tl_OS)
        self.tl_AbrirOS = QWidget()
        self.tl_AbrirOS.setObjectName(u"tl_AbrirOS")
        self.verticalLayout_21 = QVBoxLayout(self.tl_AbrirOS)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_36 = QFrame(self.tl_AbrirOS)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_22 = QLabel(self.frame_36)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_14.addWidget(self.label_22)

        self.label_53 = QLabel(self.frame_36)
        self.label_53.setObjectName(u"label_53")
        sizePolicy5.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy5)
        self.label_53.setMinimumSize(QSize(200, 200))
        self.label_53.setStyleSheet(u"border-image: url(:/Buttons/estrela.png);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_53)

        self.label_23 = QLabel(self.frame_36)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_14.addWidget(self.label_23)


        self.verticalLayout_21.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.tl_AbrirOS)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_37)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_2 = QWidget(self.frame_37)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 50);")
        self.verticalLayout_24 = QVBoxLayout(self.widget_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_39 = QFrame(self.widget_2)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_39)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_75 = QLabel(self.frame_39)
        self.label_75.setObjectName(u"label_75")

        self.verticalLayout_18.addWidget(self.label_75)

        self.label_74 = QLabel(self.frame_39)
        self.label_74.setObjectName(u"label_74")

        self.verticalLayout_18.addWidget(self.label_74)

        self.widget_7 = QWidget(self.frame_39)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_nome = QLabel(self.widget_7)
        self.lb_nome.setObjectName(u"lb_nome")
        self.lb_nome.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);")

        self.gridLayout_2.addWidget(self.lb_nome, 0, 0, 1, 1)

        self.ed_nome = QLineEdit(self.widget_7)
        self.ed_nome.setObjectName(u"ed_nome")
        self.ed_nome.setCursor(QCursor(Qt.IBeamCursor))
        self.ed_nome.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ed_nome.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);")
        self.ed_nome.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.ed_nome, 0, 1, 1, 2)

        self.lb_os = QLabel(self.widget_7)
        self.lb_os.setObjectName(u"lb_os")
        self.lb_os.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);")

        self.gridLayout_2.addWidget(self.lb_os, 0, 3, 1, 1)

        self.ed_os = QLineEdit(self.widget_7)
        self.ed_os.setObjectName(u"ed_os")
        self.ed_os.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);")

        self.gridLayout_2.addWidget(self.ed_os, 0, 4, 1, 1)

        self.lb_equipamento = QLabel(self.widget_7)
        self.lb_equipamento.setObjectName(u"lb_equipamento")
        self.lb_equipamento.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);")

        self.gridLayout_2.addWidget(self.lb_equipamento, 1, 0, 1, 2)

        self.ed_equipamento = QLineEdit(self.widget_7)
        self.ed_equipamento.setObjectName(u"ed_equipamento")
        self.ed_equipamento.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);")

        self.gridLayout_2.addWidget(self.ed_equipamento, 1, 2, 1, 1)

        self.bt_abrir_OS = QPushButton(self.widget_7)
        self.bt_abrir_OS.setObjectName(u"bt_abrir_OS")
        sizePolicy5.setHeightForWidth(self.bt_abrir_OS.sizePolicy().hasHeightForWidth())
        self.bt_abrir_OS.setSizePolicy(sizePolicy5)
        self.bt_abrir_OS.setMinimumSize(QSize(100, 0))
        self.bt_abrir_OS.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"")

        self.gridLayout_2.addWidget(self.bt_abrir_OS, 1, 4, 1, 1)

        self.label_79 = QLabel(self.widget_7)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_2.addWidget(self.label_79, 2, 0, 1, 1)


        self.verticalLayout_18.addWidget(self.widget_7)

        self.tb_abrir_os = QTableView(self.frame_39)
        self.tb_abrir_os.setObjectName(u"tb_abrir_os")
        self.tb_abrir_os.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);")

        self.verticalLayout_18.addWidget(self.tb_abrir_os)


        self.verticalLayout_24.addWidget(self.frame_39)


        self.verticalLayout_25.addWidget(self.widget_2)


        self.verticalLayout_21.addWidget(self.frame_37)

        self.tl_geral.addWidget(self.tl_AbrirOS)
        self.tl_FecgharOS = QWidget()
        self.tl_FecgharOS.setObjectName(u"tl_FecgharOS")
        self.verticalLayout_10 = QVBoxLayout(self.tl_FecgharOS)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_38 = QFrame(self.tl_FecgharOS)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_24 = QLabel(self.frame_38)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_15.addWidget(self.label_24)

        self.label_54 = QLabel(self.frame_38)
        self.label_54.setObjectName(u"label_54")
        sizePolicy5.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy5)
        self.label_54.setMinimumSize(QSize(200, 200))
        self.label_54.setStyleSheet(u"border-image: url(:/Buttons/estrela.png);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_54)

        self.label_25 = QLabel(self.frame_38)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_15.addWidget(self.label_25)


        self.verticalLayout_10.addWidget(self.frame_38)

        self.frame_40 = QFrame(self.tl_FecgharOS)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_40)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_3 = QWidget(self.frame_40)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 50);")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_41 = QFrame(self.widget_3)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_41)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_18 = QFrame(self.frame_41)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lb_os_2 = QLabel(self.frame_18)
        self.lb_os_2.setObjectName(u"lb_os_2")
        self.lb_os_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);")

        self.horizontalLayout_16.addWidget(self.lb_os_2)

        self.ed_os_fecharOS = QLineEdit(self.frame_18)
        self.ed_os_fecharOS.setObjectName(u"ed_os_fecharOS")
        self.ed_os_fecharOS.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);")

        self.horizontalLayout_16.addWidget(self.ed_os_fecharOS)


        self.verticalLayout_11.addWidget(self.frame_18)

        self.tb_fecharOS = QTableView(self.frame_41)
        self.tb_fecharOS.setObjectName(u"tb_fecharOS")
        self.tb_fecharOS.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);")

        self.verticalLayout_11.addWidget(self.tb_fecharOS)


        self.gridLayout_3.addWidget(self.frame_41, 0, 0, 1, 3)

        self.label_28 = QLabel(self.widget_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)

        self.bt_fechar_os = QPushButton(self.widget_3)
        self.bt_fechar_os.setObjectName(u"bt_fechar_os")
        sizePolicy5.setHeightForWidth(self.bt_fechar_os.sizePolicy().hasHeightForWidth())
        self.bt_fechar_os.setSizePolicy(sizePolicy5)
        self.bt_fechar_os.setMinimumSize(QSize(100, 0))
        self.bt_fechar_os.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
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
"}\n"
"")

        self.gridLayout_3.addWidget(self.bt_fechar_os, 1, 1, 1, 1)

        self.label_29 = QLabel(self.widget_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"background-color: rgba(0, 0, 0, 00);")

        self.gridLayout_3.addWidget(self.label_29, 1, 2, 1, 1)


        self.verticalLayout_27.addWidget(self.widget_3)


        self.verticalLayout_10.addWidget(self.frame_40)

        self.tl_geral.addWidget(self.tl_FecgharOS)
        self.tl_Estoque = QWidget()
        self.tl_Estoque.setObjectName(u"tl_Estoque")
        self.verticalLayout_5 = QVBoxLayout(self.tl_Estoque)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_10 = QFrame(self.tl_Estoque)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.bt_requisicao = QPushButton(self.frame_10)
        self.bt_requisicao.setObjectName(u"bt_requisicao")
        sizePolicy7.setHeightForWidth(self.bt_requisicao.sizePolicy().hasHeightForWidth())
        self.bt_requisicao.setSizePolicy(sizePolicy7)
        self.bt_requisicao.setMinimumSize(QSize(150, 150))
        self.bt_requisicao.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrela.png);\n"
"\n"
"	\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrelaSombra.png);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.bt_requisicao)

        self.label_2 = QLabel(self.frame_10)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.tl_Estoque)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_15 = QLabel(self.frame_9)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_7.addWidget(self.label_15)

        self.lb_Os_2 = QLabel(self.frame_9)
        self.lb_Os_2.setObjectName(u"lb_Os_2")
        sizePolicy5.setHeightForWidth(self.lb_Os_2.sizePolicy().hasHeightForWidth())
        self.lb_Os_2.setSizePolicy(sizePolicy5)
        self.lb_Os_2.setMinimumSize(QSize(250, 250))
        self.lb_Os_2.setStyleSheet(u"border-image: url(:/Outers/LuaCrescente.png);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.lb_Os_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lb_Os_2)

        self.label_16 = QLabel(self.frame_9)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_7.addWidget(self.label_16)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.tl_Estoque)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_64 = QLabel(self.frame_11)
        self.label_64.setObjectName(u"label_64")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(5)
        sizePolicy9.setVerticalStretch(20)
        sizePolicy9.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy9)

        self.horizontalLayout_5.addWidget(self.label_64)

        self.bt_pedido = QPushButton(self.frame_11)
        self.bt_pedido.setObjectName(u"bt_pedido")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(5)
        sizePolicy10.setVerticalStretch(20)
        sizePolicy10.setHeightForWidth(self.bt_pedido.sizePolicy().hasHeightForWidth())
        self.bt_pedido.setSizePolicy(sizePolicy10)
        self.bt_pedido.setMinimumSize(QSize(150, 150))
        self.bt_pedido.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrela.png);\n"
"\n"
"	\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrelaSombra.png);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.bt_pedido)

        self.label_65 = QLabel(self.frame_11)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_5.addWidget(self.label_65)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.tl_geral.addWidget(self.tl_Estoque)
        self.tl_Requisicao = QWidget()
        self.tl_Requisicao.setObjectName(u"tl_Requisicao")
        self.verticalLayout_13 = QVBoxLayout(self.tl_Requisicao)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_42 = QFrame(self.tl_Requisicao)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_26 = QLabel(self.frame_42)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_17.addWidget(self.label_26)

        self.label_55 = QLabel(self.frame_42)
        self.label_55.setObjectName(u"label_55")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(100)
        sizePolicy11.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy11)
        self.label_55.setMinimumSize(QSize(200, 200))
        self.label_55.setStyleSheet(u"border-image: url(:/Buttons/estrela.png);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_55)

        self.label_27 = QLabel(self.frame_42)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_17.addWidget(self.label_27)


        self.verticalLayout_13.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.tl_Requisicao)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"background-color: rgba(0, 0, 0, 50);")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_43)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_44)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.bt_requisicao_tabela = QPushButton(self.frame_44)
        self.bt_requisicao_tabela.setObjectName(u"bt_requisicao_tabela")
        self.bt_requisicao_tabela.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"")

        self.gridLayout_8.addWidget(self.bt_requisicao_tabela, 1, 1, 1, 1)

        self.label_30 = QLabel(self.frame_44)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_8.addWidget(self.label_30, 1, 0, 1, 1)

        self.label_31 = QLabel(self.frame_44)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_8.addWidget(self.label_31, 1, 2, 1, 1)

        self.frame_20 = QFrame(self.frame_44)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_20)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_33 = QLabel(self.frame_20)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);")

        self.gridLayout_12.addWidget(self.label_33, 0, 0, 1, 1)

        self.ad_material_requisicao = QLineEdit(self.frame_20)
        self.ad_material_requisicao.setObjectName(u"ad_material_requisicao")
        self.ad_material_requisicao.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_12.addWidget(self.ad_material_requisicao, 0, 1, 1, 1)

        self.label_32 = QLabel(self.frame_20)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);")

        self.gridLayout_12.addWidget(self.label_32, 0, 2, 1, 1)

        self.ed_qnt_requisicao = QLineEdit(self.frame_20)
        self.ed_qnt_requisicao.setObjectName(u"ed_qnt_requisicao")
        self.ed_qnt_requisicao.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_12.addWidget(self.ed_qnt_requisicao, 0, 3, 1, 1)

        self.tb_requisicao = QTableView(self.frame_20)
        self.tb_requisicao.setObjectName(u"tb_requisicao")
        self.tb_requisicao.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_12.addWidget(self.tb_requisicao, 1, 0, 1, 4)


        self.gridLayout_8.addWidget(self.frame_20, 0, 0, 1, 3)


        self.gridLayout_11.addWidget(self.frame_44, 0, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_43)

        self.tl_geral.addWidget(self.tl_Requisicao)
        self.tl_Pedido = QWidget()
        self.tl_Pedido.setObjectName(u"tl_Pedido")
        self.verticalLayout_12 = QVBoxLayout(self.tl_Pedido)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_46 = QFrame(self.tl_Pedido)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_36 = QLabel(self.frame_46)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_22.addWidget(self.label_36)

        self.label_56 = QLabel(self.frame_46)
        self.label_56.setObjectName(u"label_56")
        sizePolicy11.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy11)
        self.label_56.setMinimumSize(QSize(200, 200))
        self.label_56.setStyleSheet(u"border-image: url(:/Buttons/estrela.png);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_56)

        self.label_37 = QLabel(self.frame_46)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_22.addWidget(self.label_37)


        self.verticalLayout_12.addWidget(self.frame_46)

        self.widget_4 = QWidget(self.tl_Pedido)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 50);")
        self.verticalLayout_15 = QVBoxLayout(self.widget_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_45 = QFrame(self.widget_4)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_45)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_22 = QFrame(self.frame_45)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_22)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_34 = QLabel(self.frame_22)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);")

        self.gridLayout_13.addWidget(self.label_34, 0, 0, 1, 1)

        self.ed_material_Pedido = QLineEdit(self.frame_22)
        self.ed_material_Pedido.setObjectName(u"ed_material_Pedido")
        self.ed_material_Pedido.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_13.addWidget(self.ed_material_Pedido, 0, 1, 1, 1)

        self.label_35 = QLabel(self.frame_22)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);")

        self.gridLayout_13.addWidget(self.label_35, 0, 2, 1, 1)

        self.ad_qnt_Pedido = QLineEdit(self.frame_22)
        self.ad_qnt_Pedido.setObjectName(u"ad_qnt_Pedido")
        self.ad_qnt_Pedido.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_13.addWidget(self.ad_qnt_Pedido, 0, 3, 1, 1)

        self.tb_pedido = QTableView(self.frame_22)
        self.tb_pedido.setObjectName(u"tb_pedido")
        self.tb_pedido.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_13.addWidget(self.tb_pedido, 1, 0, 1, 4)


        self.gridLayout_9.addWidget(self.frame_22, 0, 0, 1, 3)

        self.label_73 = QLabel(self.frame_45)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_9.addWidget(self.label_73, 1, 2, 1, 1)

        self.bt_add_pedido = QPushButton(self.frame_45)
        self.bt_add_pedido.setObjectName(u"bt_add_pedido")
        self.bt_add_pedido.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_9.addWidget(self.bt_add_pedido, 1, 1, 1, 1)

        self.label_72 = QLabel(self.frame_45)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_9.addWidget(self.label_72, 1, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_45)


        self.verticalLayout_12.addWidget(self.widget_4)

        self.tl_geral.addWidget(self.tl_Pedido)
        self.tl_Orcamento = QWidget()
        self.tl_Orcamento.setObjectName(u"tl_Orcamento")
        self.verticalLayout_6 = QVBoxLayout(self.tl_Orcamento)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_14 = QFrame(self.tl_Orcamento)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")
        sizePolicy6.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy6)

        self.horizontalLayout_10.addWidget(self.label_14)

        self.bt_abrirOrcamento = QPushButton(self.frame_14)
        self.bt_abrirOrcamento.setObjectName(u"bt_abrirOrcamento")
        sizePolicy12 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(100)
        sizePolicy12.setVerticalStretch(100)
        sizePolicy12.setHeightForWidth(self.bt_abrirOrcamento.sizePolicy().hasHeightForWidth())
        self.bt_abrirOrcamento.setSizePolicy(sizePolicy12)
        self.bt_abrirOrcamento.setMinimumSize(QSize(150, 150))
        self.bt_abrirOrcamento.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrela.png);\n"
"\n"
"	\n"
"	font: 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrelaSombra.png);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"\n"
"}")

        self.horizontalLayout_10.addWidget(self.bt_abrirOrcamento)

        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")
        sizePolicy6.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy6)

        self.horizontalLayout_10.addWidget(self.label_17)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.tl_Orcamento)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.lb_orcamento = QLabel(self.frame_13)
        self.lb_orcamento.setObjectName(u"lb_orcamento")
        sizePolicy5.setHeightForWidth(self.lb_orcamento.sizePolicy().hasHeightForWidth())
        self.lb_orcamento.setSizePolicy(sizePolicy5)
        self.lb_orcamento.setMinimumSize(QSize(200, 200))
        self.lb_orcamento.setStyleSheet(u"border-image: url(:/Outers/LuaCrescente.png);\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.lb_orcamento.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lb_orcamento)

        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.tl_Orcamento)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        sizePolicy6.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy6)

        self.horizontalLayout_9.addWidget(self.label_12)

        self.bt_fechaOrcamento = QPushButton(self.frame_12)
        self.bt_fechaOrcamento.setObjectName(u"bt_fechaOrcamento")
        sizePolicy7.setHeightForWidth(self.bt_fechaOrcamento.sizePolicy().hasHeightForWidth())
        self.bt_fechaOrcamento.setSizePolicy(sizePolicy7)
        self.bt_fechaOrcamento.setMinimumSize(QSize(150, 150))
        self.bt_fechaOrcamento.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrela.png);\n"
"\n"
"	\n"
"	font: 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrelaSombra.png);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"\n"
"}")

        self.horizontalLayout_9.addWidget(self.bt_fechaOrcamento)

        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")
        sizePolicy8.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy8)

        self.horizontalLayout_9.addWidget(self.label_13)


        self.verticalLayout_6.addWidget(self.frame_12)

        self.tl_geral.addWidget(self.tl_Orcamento)
        self.tl_abrir_Orcamento = QWidget()
        self.tl_abrir_Orcamento.setObjectName(u"tl_abrir_Orcamento")
        self.verticalLayout_14 = QVBoxLayout(self.tl_abrir_Orcamento)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_47 = QFrame(self.tl_abrir_Orcamento)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_38 = QLabel(self.frame_47)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_23.addWidget(self.label_38)

        self.label_57 = QLabel(self.frame_47)
        self.label_57.setObjectName(u"label_57")
        sizePolicy11.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy11)
        self.label_57.setMinimumSize(QSize(200, 200))
        self.label_57.setStyleSheet(u"border-image: url(:/Buttons/estrela.png);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_57)

        self.label_39 = QLabel(self.frame_47)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_23.addWidget(self.label_39)


        self.verticalLayout_14.addWidget(self.frame_47)

        self.widget_5 = QWidget(self.tl_abrir_Orcamento)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 50);")
        self.verticalLayout_16 = QVBoxLayout(self.widget_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_48 = QFrame(self.widget_5)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_48)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_24 = QFrame(self.frame_48)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lb_os_5 = QLabel(self.frame_24)
        self.lb_os_5.setObjectName(u"lb_os_5")
        self.lb_os_5.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"")

        self.horizontalLayout_24.addWidget(self.lb_os_5)

        self.ed_os_5 = QLineEdit(self.frame_24)
        self.ed_os_5.setObjectName(u"ed_os_5")
        sizePolicy13 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.ed_os_5.sizePolicy().hasHeightForWidth())
        self.ed_os_5.setSizePolicy(sizePolicy13)
        self.ed_os_5.setMinimumSize(QSize(10, 0))
        self.ed_os_5.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.horizontalLayout_24.addWidget(self.ed_os_5)

        self.lb_data_5 = QLabel(self.frame_24)
        self.lb_data_5.setObjectName(u"lb_data_5")
        self.lb_data_5.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"")

        self.horizontalLayout_24.addWidget(self.lb_data_5)

        self.ed_data_5 = QDateEdit(self.frame_24)
        self.ed_data_5.setObjectName(u"ed_data_5")
        self.ed_data_5.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.horizontalLayout_24.addWidget(self.ed_data_5)


        self.gridLayout_10.addWidget(self.frame_24, 0, 0, 1, 4)

        self.frame_25 = QFrame(self.frame_48)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_40 = QLabel(self.frame_25)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"")

        self.horizontalLayout_25.addWidget(self.label_40)

        self.lineEdit_5 = QLineEdit(self.frame_25)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.horizontalLayout_25.addWidget(self.lineEdit_5)

        self.label_41 = QLabel(self.frame_25)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"")

        self.horizontalLayout_25.addWidget(self.label_41)

        self.lineEdit_6 = QLineEdit(self.frame_25)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.horizontalLayout_25.addWidget(self.lineEdit_6)


        self.gridLayout_10.addWidget(self.frame_25, 1, 0, 1, 4)

        self.tableWidget_4 = QTableWidget(self.frame_48)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_10.addWidget(self.tableWidget_4, 2, 0, 1, 4)

        self.label_76 = QLabel(self.frame_48)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_10.addWidget(self.label_76, 3, 0, 1, 1)

        self.bt_adicionar_Orcamento = QPushButton(self.frame_48)
        self.bt_adicionar_Orcamento.setObjectName(u"bt_adicionar_Orcamento")
        self.bt_adicionar_Orcamento.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"")

        self.gridLayout_10.addWidget(self.bt_adicionar_Orcamento, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_48)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"")

        self.gridLayout_10.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.label_77 = QLabel(self.frame_48)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_10.addWidget(self.label_77, 3, 3, 1, 1)


        self.verticalLayout_16.addWidget(self.frame_48)


        self.verticalLayout_14.addWidget(self.widget_5)

        self.tl_geral.addWidget(self.tl_abrir_Orcamento)
        self.tl_cadastro_User = QWidget()
        self.tl_cadastro_User.setObjectName(u"tl_cadastro_User")
        self.verticalLayout_23 = QVBoxLayout(self.tl_cadastro_User)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_29 = QFrame(self.tl_cadastro_User)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_29)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_71 = QLabel(self.frame_29)
        self.label_71.setObjectName(u"label_71")
        sizePolicy5.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy5)
        self.label_71.setMinimumSize(QSize(200, 200))
        self.label_71.setStyleSheet(u"border-image: url(:/Buttons/HomemPNG.png);")
        self.label_71.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_71)


        self.verticalLayout_23.addWidget(self.frame_29)

        self.widget = QWidget(self.tl_cadastro_User)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgba(0, 0, 0, 50);")
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_66 = QLabel(self.widget)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"")

        self.gridLayout_6.addWidget(self.label_66, 0, 0, 1, 1)

        self.ed_nome_cadastro = QLineEdit(self.widget)
        self.ed_nome_cadastro.setObjectName(u"ed_nome_cadastro")
        self.ed_nome_cadastro.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_6.addWidget(self.ed_nome_cadastro, 0, 1, 1, 1)

        self.label_67 = QLabel(self.widget)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"")

        self.gridLayout_6.addWidget(self.label_67, 1, 0, 1, 1)

        self.ed_usuario_cadastro = QLineEdit(self.widget)
        self.ed_usuario_cadastro.setObjectName(u"ed_usuario_cadastro")
        self.ed_usuario_cadastro.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_6.addWidget(self.ed_usuario_cadastro, 1, 1, 1, 1)

        self.label_68 = QLabel(self.widget)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"")

        self.gridLayout_6.addWidget(self.label_68, 2, 0, 1, 1)

        self.ed_senha_cadastro = QLineEdit(self.widget)
        self.ed_senha_cadastro.setObjectName(u"ed_senha_cadastro")
        self.ed_senha_cadastro.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")
        self.ed_senha_cadastro.setEchoMode(QLineEdit.Password)

        self.gridLayout_6.addWidget(self.ed_senha_cadastro, 2, 1, 1, 1)

        self.label_69 = QLabel(self.widget)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"")

        self.gridLayout_6.addWidget(self.label_69, 3, 0, 1, 1)

        self.ed_senha2_cadastro = QLineEdit(self.widget)
        self.ed_senha2_cadastro.setObjectName(u"ed_senha2_cadastro")
        self.ed_senha2_cadastro.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")
        self.ed_senha2_cadastro.setEchoMode(QLineEdit.Password)

        self.gridLayout_6.addWidget(self.ed_senha2_cadastro, 3, 1, 1, 1)

        self.label_70 = QLabel(self.widget)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"")

        self.gridLayout_6.addWidget(self.label_70, 4, 0, 1, 1)

        self.cb_perfil_cadastro = QComboBox(self.widget)
        self.cb_perfil_cadastro.addItem("")
        self.cb_perfil_cadastro.addItem("")
        self.cb_perfil_cadastro.setObjectName(u"cb_perfil_cadastro")
        sizePolicy14 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy14.setHorizontalStretch(100)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.cb_perfil_cadastro.sizePolicy().hasHeightForWidth())
        self.cb_perfil_cadastro.setSizePolicy(sizePolicy14)
        self.cb_perfil_cadastro.setMinimumSize(QSize(130, 0))
        self.cb_perfil_cadastro.setSizeIncrement(QSize(100, 100))
        self.cb_perfil_cadastro.setBaseSize(QSize(101, 0))
        self.cb_perfil_cadastro.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_6.addWidget(self.cb_perfil_cadastro, 4, 1, 1, 1)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy15 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy15)
        self.widget_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_78 = QLabel(self.widget_6)
        self.label_78.setObjectName(u"label_78")

        self.horizontalLayout_29.addWidget(self.label_78)

        self.bt_cadastraruser = QPushButton(self.widget_6)
        self.bt_cadastraruser.setObjectName(u"bt_cadastraruser")
        sizePolicy5.setHeightForWidth(self.bt_cadastraruser.sizePolicy().hasHeightForWidth())
        self.bt_cadastraruser.setSizePolicy(sizePolicy5)
        self.bt_cadastraruser.setMinimumSize(QSize(100, 0))
        self.bt_cadastraruser.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_29.addWidget(self.bt_cadastraruser)


        self.gridLayout_6.addWidget(self.widget_6, 5, 1, 1, 1)


        self.verticalLayout_23.addWidget(self.widget)

        self.tl_geral.addWidget(self.tl_cadastro_User)
        self.tl_Sobre = QWidget()
        self.tl_Sobre.setObjectName(u"tl_Sobre")
        self.verticalLayout_8 = QVBoxLayout(self.tl_Sobre)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_15 = QFrame(self.tl_Sobre)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.bt_requisicao_2 = QPushButton(self.frame_15)
        self.bt_requisicao_2.setObjectName(u"bt_requisicao_2")
        sizePolicy7.setHeightForWidth(self.bt_requisicao_2.sizePolicy().hasHeightForWidth())
        self.bt_requisicao_2.setSizePolicy(sizePolicy7)
        self.bt_requisicao_2.setMinimumSize(QSize(150, 150))
        self.bt_requisicao_2.setStyleSheet(u"	\n"
"	border-image: url(:/Buttons/estrela.png);\n"
"	\n"
"	font: 8pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_11.addWidget(self.bt_requisicao_2)

        self.label_11 = QLabel(self.frame_15)
        self.label_11.setObjectName(u"label_11")
        sizePolicy6.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy6)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.bt_linkedin = QPushButton(self.frame_15)
        self.bt_linkedin.setObjectName(u"bt_linkedin")
        sizePolicy7.setHeightForWidth(self.bt_linkedin.sizePolicy().hasHeightForWidth())
        self.bt_linkedin.setSizePolicy(sizePolicy7)
        self.bt_linkedin.setMinimumSize(QSize(150, 150))
        self.bt_linkedin.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrela.png);\n"
"\n"
"	\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrelaSombra.png);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"}")

        self.horizontalLayout_11.addWidget(self.bt_linkedin)


        self.verticalLayout_8.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.tl_Sobre)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_18 = QLabel(self.frame_16)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_12.addWidget(self.label_18)

        self.lb_Os_3 = QLabel(self.frame_16)
        self.lb_Os_3.setObjectName(u"lb_Os_3")
        sizePolicy5.setHeightForWidth(self.lb_Os_3.sizePolicy().hasHeightForWidth())
        self.lb_Os_3.setSizePolicy(sizePolicy5)
        self.lb_Os_3.setMinimumSize(QSize(200, 200))
        self.lb_Os_3.setStyleSheet(u"border-image: url(:/Outers/LuaCrescente.png);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.lb_Os_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lb_Os_3)

        self.label_19 = QLabel(self.frame_16)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_12.addWidget(self.label_19)


        self.verticalLayout_8.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.tl_Sobre)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel(self.frame_17)
        self.label_20.setObjectName(u"label_20")
        sizePolicy6.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy6)

        self.horizontalLayout_13.addWidget(self.label_20)

        self.bt_fechaOs_2 = QPushButton(self.frame_17)
        self.bt_fechaOs_2.setObjectName(u"bt_fechaOs_2")
        sizePolicy7.setHeightForWidth(self.bt_fechaOs_2.sizePolicy().hasHeightForWidth())
        self.bt_fechaOs_2.setSizePolicy(sizePolicy7)
        self.bt_fechaOs_2.setMinimumSize(QSize(100, 100))
        self.bt_fechaOs_2.setStyleSheet(u"\n"
"	border-image: url(:/Buttons/estrela.png);\n"
"\n"
"	\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"")

        self.horizontalLayout_13.addWidget(self.bt_fechaOs_2)

        self.label_21 = QLabel(self.frame_17)
        self.label_21.setObjectName(u"label_21")
        sizePolicy8.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy8)

        self.horizontalLayout_13.addWidget(self.label_21)


        self.verticalLayout_8.addWidget(self.frame_17)

        self.tl_geral.addWidget(self.tl_Sobre)
        self.tl_Cadastro = QWidget()
        self.tl_Cadastro.setObjectName(u"tl_Cadastro")
        self.verticalLayout_17 = QVBoxLayout(self.tl_Cadastro)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_33 = QFrame(self.tl_Cadastro)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_43 = QLabel(self.frame_33)
        self.label_43.setObjectName(u"label_43")
        sizePolicy6.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy6)

        self.horizontalLayout_26.addWidget(self.label_43)

        self.bt_Equipamento = QPushButton(self.frame_33)
        self.bt_Equipamento.setObjectName(u"bt_Equipamento")
        sizePolicy7.setHeightForWidth(self.bt_Equipamento.sizePolicy().hasHeightForWidth())
        self.bt_Equipamento.setSizePolicy(sizePolicy7)
        self.bt_Equipamento.setMinimumSize(QSize(150, 150))
        self.bt_Equipamento.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrela.png);\n"
"\n"
"	\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrelaSombra.png);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"}")

        self.horizontalLayout_26.addWidget(self.bt_Equipamento)

        self.label_44 = QLabel(self.frame_33)
        self.label_44.setObjectName(u"label_44")
        sizePolicy6.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy6)

        self.horizontalLayout_26.addWidget(self.label_44)


        self.verticalLayout_17.addWidget(self.frame_33)

        self.frame_35 = QFrame(self.tl_Cadastro)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_47 = QLabel(self.frame_35)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_28.addWidget(self.label_47)

        self.lb_cadastro = QLabel(self.frame_35)
        self.lb_cadastro.setObjectName(u"lb_cadastro")
        sizePolicy5.setHeightForWidth(self.lb_cadastro.sizePolicy().hasHeightForWidth())
        self.lb_cadastro.setSizePolicy(sizePolicy5)
        self.lb_cadastro.setMinimumSize(QSize(200, 200))
        self.lb_cadastro.setStyleSheet(u"border-image: url(:/Outers/LuaCrescente.png);\n"
"font: 36pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);")
        self.lb_cadastro.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.lb_cadastro)

        self.label_48 = QLabel(self.frame_35)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_28.addWidget(self.label_48)


        self.verticalLayout_17.addWidget(self.frame_35)

        self.frame_34 = QFrame(self.tl_Cadastro)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_45 = QLabel(self.frame_34)
        self.label_45.setObjectName(u"label_45")
        sizePolicy6.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy6)

        self.horizontalLayout_27.addWidget(self.label_45)

        self.bt_Produto = QPushButton(self.frame_34)
        self.bt_Produto.setObjectName(u"bt_Produto")
        sizePolicy7.setHeightForWidth(self.bt_Produto.sizePolicy().hasHeightForWidth())
        self.bt_Produto.setSizePolicy(sizePolicy7)
        self.bt_Produto.setMinimumSize(QSize(150, 150))
        self.bt_Produto.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrela.png);\n"
"\n"
"	\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"\n"
"	\n"
"	\n"
"	border-image: url(:/Buttons/estrelaSombra.png);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"}")

        self.horizontalLayout_27.addWidget(self.bt_Produto)

        self.label_46 = QLabel(self.frame_34)
        self.label_46.setObjectName(u"label_46")
        sizePolicy8.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy8)

        self.horizontalLayout_27.addWidget(self.label_46)


        self.verticalLayout_17.addWidget(self.frame_34)

        self.tl_geral.addWidget(self.tl_Cadastro)
        self.tl_equipamento = QWidget()
        self.tl_equipamento.setObjectName(u"tl_equipamento")
        self.verticalLayout_20 = QVBoxLayout(self.tl_equipamento)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_50 = QFrame(self.tl_equipamento)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_50 = QLabel(self.frame_50)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_33.addWidget(self.label_50)

        self.label_58 = QLabel(self.frame_50)
        self.label_58.setObjectName(u"label_58")
        sizePolicy11.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy11)
        self.label_58.setMinimumSize(QSize(200, 200))
        self.label_58.setStyleSheet(u"border-image: url(:/Buttons/estrela.png);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_58)

        self.label_51 = QLabel(self.frame_50)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_33.addWidget(self.label_51)


        self.verticalLayout_20.addWidget(self.frame_50)

        self.frame_49 = QFrame(self.tl_equipamento)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"background-color: rgba(0, 0, 0, 50);")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_49)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_26 = QFrame(self.frame_49)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_26)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lb_os_6 = QLabel(self.frame_26)
        self.lb_os_6.setObjectName(u"lb_os_6")
        self.lb_os_6.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);")

        self.gridLayout_5.addWidget(self.lb_os_6, 0, 0, 1, 1)

        self.ed_codg_Equipamento = QLineEdit(self.frame_26)
        self.ed_codg_Equipamento.setObjectName(u"ed_codg_Equipamento")
        sizePolicy13.setHeightForWidth(self.ed_codg_Equipamento.sizePolicy().hasHeightForWidth())
        self.ed_codg_Equipamento.setSizePolicy(sizePolicy13)
        self.ed_codg_Equipamento.setMinimumSize(QSize(10, 0))
        self.ed_codg_Equipamento.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_5.addWidget(self.ed_codg_Equipamento, 0, 1, 1, 1)

        self.label_42 = QLabel(self.frame_26)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);")

        self.gridLayout_5.addWidget(self.label_42, 0, 2, 1, 1)

        self.ed_material_Equipamento = QLineEdit(self.frame_26)
        self.ed_material_Equipamento.setObjectName(u"ed_material_Equipamento")
        self.ed_material_Equipamento.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_5.addWidget(self.ed_material_Equipamento, 0, 3, 1, 1)

        self.tb_equipamento = QTableView(self.frame_26)
        self.tb_equipamento.setObjectName(u"tb_equipamento")
        self.tb_equipamento.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_5.addWidget(self.tb_equipamento, 1, 0, 1, 4)


        self.gridLayout_4.addWidget(self.frame_26, 0, 0, 1, 3)

        self.bt_enviar_equipamento = QPushButton(self.frame_49)
        self.bt_enviar_equipamento.setObjectName(u"bt_enviar_equipamento")
        self.bt_enviar_equipamento.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_4.addWidget(self.bt_enviar_equipamento, 1, 1, 1, 1)

        self.label_52 = QLabel(self.frame_49)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_4.addWidget(self.label_52, 1, 0, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_49)

        self.tl_geral.addWidget(self.tl_equipamento)
        self.tl_produto = QWidget()
        self.tl_produto.setObjectName(u"tl_produto")
        self.verticalLayout_19 = QVBoxLayout(self.tl_produto)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_52 = QFrame(self.tl_produto)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_60 = QLabel(self.frame_52)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_34.addWidget(self.label_60)

        self.label_61 = QLabel(self.frame_52)
        self.label_61.setObjectName(u"label_61")
        sizePolicy11.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy11)
        self.label_61.setMinimumSize(QSize(200, 200))
        self.label_61.setStyleSheet(u"border-image: url(:/Buttons/estrela.png);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_61)

        self.label_62 = QLabel(self.frame_52)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_34.addWidget(self.label_62)


        self.verticalLayout_19.addWidget(self.frame_52)

        self.frame_51 = QFrame(self.tl_produto)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"background-color: rgba(0, 0, 0, 50);")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_51)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_27 = QFrame(self.frame_51)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lb_os_7 = QLabel(self.frame_27)
        self.lb_os_7.setObjectName(u"lb_os_7")
        self.lb_os_7.setStyleSheet(u"\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"")

        self.horizontalLayout_32.addWidget(self.lb_os_7)

        self.ed_codg_produto = QLineEdit(self.frame_27)
        self.ed_codg_produto.setObjectName(u"ed_codg_produto")
        sizePolicy13.setHeightForWidth(self.ed_codg_produto.sizePolicy().hasHeightForWidth())
        self.ed_codg_produto.setSizePolicy(sizePolicy13)
        self.ed_codg_produto.setMinimumSize(QSize(10, 0))
        self.ed_codg_produto.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.horizontalLayout_32.addWidget(self.ed_codg_produto)

        self.label_49 = QLabel(self.frame_27)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"")

        self.horizontalLayout_32.addWidget(self.label_49)

        self.ed_equipamento_produto = QLineEdit(self.frame_27)
        self.ed_equipamento_produto.setObjectName(u"ed_equipamento_produto")
        self.ed_equipamento_produto.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.horizontalLayout_32.addWidget(self.ed_equipamento_produto)


        self.gridLayout_7.addWidget(self.frame_27, 0, 0, 1, 2)

        self.frame_28 = QFrame(self.frame_51)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_59 = QLabel(self.frame_28)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 0, 0);\n"
"")

        self.horizontalLayout_35.addWidget(self.label_59)

        self.ed_descricao_produto = QLineEdit(self.frame_28)
        self.ed_descricao_produto.setObjectName(u"ed_descricao_produto")
        self.ed_descricao_produto.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.horizontalLayout_35.addWidget(self.ed_descricao_produto)


        self.gridLayout_7.addWidget(self.frame_28, 1, 0, 1, 2)

        self.bt_enviar_produto = QPushButton(self.frame_51)
        self.bt_enviar_produto.setObjectName(u"bt_enviar_produto")
        self.bt_enviar_produto.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_7.addWidget(self.bt_enviar_produto, 3, 0, 1, 1)

        self.label_63 = QLabel(self.frame_51)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")

        self.gridLayout_7.addWidget(self.label_63, 4, 0, 1, 1)

        self.tb_produto = QTableView(self.frame_51)
        self.tb_produto.setObjectName(u"tb_produto")
        self.tb_produto.setStyleSheet(u"background-color: rgba(196, 204, 236, 80);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(243, 243, 243);\n"
"")

        self.gridLayout_7.addWidget(self.tb_produto, 2, 0, 1, 2)


        self.verticalLayout_19.addWidget(self.frame_51)

        self.tl_geral.addWidget(self.tl_produto)

        self.horizontalLayout_36.addWidget(self.tl_geral)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tl_geral.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bnt_Perfil.setText("")
        self.lb_Perfil.setText("")
        self.bnt_inicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.bnt_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.bnt_OS.setText(QCoreApplication.translate("MainWindow", u"OS", None))
        self.bnt_estoque.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.bnt_Sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.lg_lateral.setText("")
        self.lb_moonlight.setText(QCoreApplication.translate("MainWindow", u"MoonLight", None))
        self.label_5.setText("")
        self.bt_abrirOs.setText(QCoreApplication.translate("MainWindow", u"Abrir OS", None))
        self.label_6.setText("")
        self.label_9.setText("")
        self.lb_Os.setText(QCoreApplication.translate("MainWindow", u"OS", None))
        self.label_10.setText("")
        self.label_7.setText("")
        self.bt_fechaOs.setText(QCoreApplication.translate("MainWindow", u"Fechar OS", None))
        self.label_8.setText("")
        self.label_22.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Abrir OS", None))
        self.label_23.setText("")
        self.label_75.setText("")
        self.label_74.setText("")
        self.lb_nome.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.ed_nome.setText("")
        self.lb_os.setText(QCoreApplication.translate("MainWindow", u"OS:", None))
        self.lb_equipamento.setText(QCoreApplication.translate("MainWindow", u"Equipamento:", None))
        self.bt_abrir_OS.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_79.setText("")
        self.label_24.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Fechar OS", None))
        self.label_25.setText("")
        self.lb_os_2.setText(QCoreApplication.translate("MainWindow", u"OS:", None))
        self.label_28.setText("")
        self.bt_fechar_os.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.label_29.setText("")
        self.label.setText("")
        self.bt_requisicao.setText(QCoreApplication.translate("MainWindow", u"Requisi\u00e7\u00e3o", None))
        self.label_2.setText("")
        self.label_15.setText("")
        self.lb_Os_2.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.label_16.setText("")
        self.label_64.setText("")
        self.bt_pedido.setText(QCoreApplication.translate("MainWindow", u"Pedido", None))
        self.label_65.setText("")
        self.label_26.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Requisi\u00e7\u00e3o", None))
        self.label_27.setText("")
        self.bt_requisicao_tabela.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_30.setText("")
        self.label_31.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Material:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_36.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Pedido", None))
        self.label_37.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Material:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_73.setText("")
        self.bt_add_pedido.setText(QCoreApplication.translate("MainWindow", u"adicionar", None))
        self.label_72.setText("")
        self.label_14.setText("")
        self.bt_abrirOrcamento.setText(QCoreApplication.translate("MainWindow", u"Abrir Or\u00e7amento", None))
        self.label_17.setText("")
        self.label_3.setText("")
        self.lb_orcamento.setText(QCoreApplication.translate("MainWindow", u"Or\u00e7amentos", None))
        self.label_4.setText("")
        self.label_12.setText("")
        self.bt_fechaOrcamento.setText(QCoreApplication.translate("MainWindow", u"Fechar Or\u00e7amento", None))
        self.label_13.setText("")
        self.label_38.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Abrir Or\u00e7amento", None))
        self.label_39.setText("")
        self.lb_os_5.setText(QCoreApplication.translate("MainWindow", u"OS:", None))
        self.lb_data_5.setText(QCoreApplication.translate("MainWindow", u"Data:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Material:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_76.setText("")
        self.bt_adicionar_Orcamento.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.label_77.setText("")
        self.label_71.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Perfil:", None))
        self.cb_perfil_cadastro.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil_cadastro.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_78.setText("")
        self.bt_cadastraruser.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.bt_requisicao_2.setText(QCoreApplication.translate("MainWindow", u"Rafael Battistella", None))
        self.label_11.setText("")
        self.bt_linkedin.setText(QCoreApplication.translate("MainWindow", u"Linkedin", None))
        self.label_18.setText("")
        self.lb_Os_3.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.label_19.setText("")
        self.label_20.setText("")
        self.bt_fechaOs_2.setText(QCoreApplication.translate("MainWindow", u"V 1.0", None))
        self.label_21.setText("")
        self.label_43.setText("")
        self.bt_Equipamento.setText(QCoreApplication.translate("MainWindow", u"Equipamento", None))
        self.label_44.setText("")
        self.label_47.setText("")
        self.lb_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_48.setText("")
        self.label_45.setText("")
        self.bt_Produto.setText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.label_46.setText("")
        self.label_50.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Equipamento", None))
        self.label_51.setText("")
        self.lb_os_6.setText(QCoreApplication.translate("MainWindow", u"Codigo:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Equipamento:", None))
        self.bt_enviar_equipamento.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_52.setText("")
        self.label_60.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.label_62.setText("")
        self.lb_os_7.setText(QCoreApplication.translate("MainWindow", u"Codigo:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Equipamento:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o:", None))
        self.bt_enviar_produto.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.label_63.setText("")
    # retranslateUi

