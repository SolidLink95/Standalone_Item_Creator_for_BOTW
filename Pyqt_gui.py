# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt/main_window_black.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SIC(object):
    def setupUi(self, SIC):
        SIC.setObjectName("SIC")
        SIC.resize(945, 824)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SIC.setWindowIcon(icon)
        SIC.setStyleSheet("QMenuBar {\n"
"    background-color: rgb(35, 37, 41);\n"
"    color: white;\n"
"    border-color: rgb(60, 85, 109);\n"
"    gridline-color:  rgb(60, 85, 109);\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    spacing: 3px;           \n"
"    padding: 2px 10px;\n"
"    background-color: rgb(35, 37, 41);\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar::item:selected {    \n"
"    background-color: rgb(244,164,96);\n"
"    color: white;\n"
"}\n"
"QMenuBar::item:pressed {\n"
"    background: rgb(128,0,0);\n"
"}\n"
"\n"
"/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */  \n"
"\n"
"QMenu {\n"
"    background-color: rgb(35, 37, 41);\n"
"    border: 1px solid black;\n"
"    margin: 2px;\n"
"    color: white;\n"
"}\n"
"QMenu::item {\n"
"    background-color: rgb(35, 37, 41);\n"
"}\n"
"QMenu::item:selected { \n"
"    background-color: rgb(149, 165, 166);\n"
"    color: rgb(220,220,220);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(SIC)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 951, 811))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(99)
        sizePolicy.setVerticalStretch(99)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("QProgressBar {\n"
"    \n"
"    background-color: rgb(96, 116, 165);\n"
"    /*color: white;*/\n"
"    color: black;\n"
"    border-style: none;\n"
"    text-align: center;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea{ \n"
"    background-color: rgb(149, 165, 166);\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.534, x2:1, y2:0.522, stop:0 rgba(46, 68, 91, 255), stop:1 rgba(101, 151, 200, 255));\n"
"}\n"
"\n"
"QTabWidget {\n"
"    background-color: rgb(91, 129, 165);\n"
"    color: black;\n"
"    border-color: rgb(60, 85, 109);\n"
"    gridline-color:  rgb(60, 85, 109);\n"
"    font: 8pt \"Segoe MDL2 Assets\";\n"
"}\n"
"\n"
"QListWidget {\n"
"    background-color: rgb(79, 104, 191);\n"
"    color: white;\n"
"    border-color: rgb(60, 85, 109);\n"
"    gridline-color:  rgb(60, 85, 109);\n"
"font: 10pt \"Segoe MDL2 Assets\";\n"
"}\n"
"QLineEdit {\n"
"    background-color: rgb(149, 165, 166);\n"
"    color: white;\n"
"    border: none;\n"
"font: 10pt \"Segoe MDL2 Assets\";\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: rgb(81, 85, 93);\n"
"    color: white;\n"
"}\n"
" QTabBar::tab:!selected {\n"
"    background-color: rgb(138, 138, 138);\n"
"    color: white;\n"
"    }\n"
"\n"
"QFrame{\n"
"    background-color: rgb(47, 49, 54);\n"
"    color: white;\n"
"    \n"
"    font: 10pt \"Segoe MDL2 Assets\";\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: rgb(149, 165, 166);\n"
"font: 10pt \"Segoe MDL2 Assets\";\n"
"}\n"
"\n"
"QLabel {\n"
"font: 10pt \"Segoe MDL2 Assets\";\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: rgb(149, 165, 166);\n"
"    border: none;\n"
"    font: 10pt \"Segoe MDL2 Assets\";\n"
"    color: white;\n"
"}\n"
"\n"
"    QComboBox QAbstractItemView::item\n"
"    {\n"
"      padding-top: 10px;\n"
"      padding-bottom: 10px;\n"
"    }\n"
"\n"
"QRadioButton {\n"
"    color: white;\n"
"    border-color: rgb(60, 85, 109);\n"
"    gridline-color:  rgb(60, 85, 109);\n"
"    font: 10pt \"Segoe MDL2 Assets\";\n"
"}\n"
"QCheckBox {\n"
"    color: white;\n"
"    border-color: rgb(60, 85, 109);\n"
"    gridline-color:  rgb(60, 85, 109);\n"
"    font: 10pt \"Segoe MDL2 Assets\";\n"
"}\n"
"QTabWidget::pane { \n"
"border: 1; \n"
"border-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(255, 173, 0);\n"
"border-radius: 10px;\n"
"font: 11pt \"Segoe MDL2 Assets\";\n"
"    border: none;\n"
"font-weight: bold\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"                             {\n"
"                             background-color : rgb(244, 207, 0);\n"
"                             }\n"
"QMenuBar::item:pressed\n"
"                             {\n"
"                             background-color : rgb(149, 165, 166);\n"
"                             }\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Create_mod = QtWidgets.QPushButton(self.frame)
        self.Create_mod.setMinimumSize(QtCore.QSize(0, 30))
        self.Create_mod.setObjectName("Create_mod")
        self.gridLayout_2.addWidget(self.Create_mod, 3, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 35))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 4, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_83 = QtWidgets.QLabel(self.frame)
        self.label_83.setMinimumSize(QtCore.QSize(100, 0))
        self.label_83.setObjectName("label_83")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_83)
        self.Lang = QtWidgets.QComboBox(self.frame)
        self.Lang.setMinimumSize(QtCore.QSize(0, 25))
        self.Lang.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Lang.setObjectName("Lang")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Lang)
        self.label_84 = QtWidgets.QLabel(self.frame)
        self.label_84.setMinimumSize(QtCore.QSize(100, 0))
        self.label_84.setObjectName("label_84")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_84)
        self.pack_name = QtWidgets.QLineEdit(self.frame)
        self.pack_name.setMinimumSize(QtCore.QSize(0, 25))
        self.pack_name.setMaximumSize(QtCore.QSize(200, 25))
        self.pack_name.setObjectName("pack_name")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pack_name)
        self.horizontalLayout_4.addLayout(self.formLayout_9)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setMinimumSize(QtCore.QSize(0, 25))
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wiiu_radiobutton = QtWidgets.QRadioButton(self.frame)
        self.wiiu_radiobutton.setMinimumSize(QtCore.QSize(0, 20))
        self.wiiu_radiobutton.setChecked(True)
        self.wiiu_radiobutton.setObjectName("wiiu_radiobutton")
        self.horizontalLayout_2.addWidget(self.wiiu_radiobutton)
        self.switch_radiobutton = QtWidgets.QRadioButton(self.frame)
        self.switch_radiobutton.setEnabled(True)
        self.switch_radiobutton.setMinimumSize(QtCore.QSize(0, 20))
        self.switch_radiobutton.setObjectName("switch_radiobutton")
        self.horizontalLayout_2.addWidget(self.switch_radiobutton)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_85 = QtWidgets.QLabel(self.frame)
        self.label_85.setMinimumSize(QtCore.QSize(100, 0))
        self.label_85.setObjectName("label_85")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_85)
        self.shop = QtWidgets.QComboBox(self.frame)
        self.shop.setMinimumSize(QtCore.QSize(180, 25))
        self.shop.setMaximumSize(QtCore.QSize(185, 0))
        self.shop.setObjectName("shop")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.shop)
        self.horizontalLayout_4.addLayout(self.formLayout_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.TabWidget = QtWidgets.QTabWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabWidget.sizePolicy().hasHeightForWidth())
        self.TabWidget.setSizePolicy(sizePolicy)
        self.TabWidget.setMinimumSize(QtCore.QSize(720, 580))
        self.TabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TabWidget.setStyleSheet("QTabWidget {\n"
"    background-color: rgb(91, 129, 165);\n"
"    color: rgb(60, 85, 109);\n"
"    border-color: rgb(60, 85, 109);\n"
"    gridline-color:  rgb(60, 85, 109);\n"
"    font: 8pt \"Segoe MDL2 Assets\";\n"
"}")
        self.TabWidget.setObjectName("TabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_4 = QtWidgets.QFrame(self.tab)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 711, 631))
        self.frame_4.setStyleSheet("QFrame{\n"
"    background-color: rgb(81, 85, 93);\n"
"    color: white;\n"
"    \n"
"    font: 9pt \"Segoe MDL2 Assets\";\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_28 = QtWidgets.QLabel(self.frame_4)
        self.label_28.setObjectName("label_28")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.base = QtWidgets.QComboBox(self.frame_4)
        self.base.setEnabled(True)
        self.base.setMinimumSize(QtCore.QSize(260, 25))
        self.base.setMaximumSize(QtCore.QSize(166666, 16777215))
        self.base.setObjectName("base")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.base)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.name = QtWidgets.QLineEdit(self.frame_4)
        self.name.setMinimumSize(QtCore.QSize(0, 25))
        self.name.setMaximumSize(QtCore.QSize(16777215, 25))
        self.name.setObjectName("name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.defence = QtWidgets.QLineEdit(self.frame_4)
        self.defence.setMinimumSize(QtCore.QSize(0, 25))
        self.defence.setMaximumSize(QtCore.QSize(16777215, 25))
        self.defence.setObjectName("defence")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.defence)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.elink = QtWidgets.QLineEdit(self.frame_4)
        self.elink.setMinimumSize(QtCore.QSize(0, 25))
        self.elink.setMaximumSize(QtCore.QSize(16777215, 25))
        self.elink.setObjectName("elink")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.elink)
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.slink = QtWidgets.QLineEdit(self.frame_4)
        self.slink.setMinimumSize(QtCore.QSize(0, 25))
        self.slink.setMaximumSize(QtCore.QSize(16777215, 25))
        self.slink.setObjectName("slink")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.slink)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.profile = QtWidgets.QComboBox(self.frame_4)
        self.profile.setMinimumSize(QtCore.QSize(0, 25))
        self.profile.setObjectName("profile")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.profile)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.series = QtWidgets.QComboBox(self.frame_4)
        self.series.setMinimumSize(QtCore.QSize(0, 25))
        self.series.setObjectName("series")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.series)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.physics = QtWidgets.QLineEdit(self.frame_4)
        self.physics.setMinimumSize(QtCore.QSize(0, 25))
        self.physics.setMaximumSize(QtCore.QSize(16777215, 25))
        self.physics.setObjectName("physics")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.physics)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.price = QtWidgets.QLineEdit(self.frame_4)
        self.price.setMinimumSize(QtCore.QSize(0, 25))
        self.price.setMaximumSize(QtCore.QSize(16777215, 25))
        self.price.setObjectName("price")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.price)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.name_desc = QtWidgets.QLineEdit(self.frame_4)
        self.name_desc.setMinimumSize(QtCore.QSize(0, 25))
        self.name_desc.setMaximumSize(QtCore.QSize(16777215, 25))
        self.name_desc.setObjectName("name_desc")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.name_desc)
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.desc = QtWidgets.QTextEdit(self.frame_4)
        self.desc.setMaximumSize(QtCore.QSize(16777215, 100))
        self.desc.setStyleSheet("background-color: rgb(149, 165, 166);\n"
"font: 10pt \"Segoe MDL2 Assets\";")
        self.desc.setObjectName("desc")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.desc)
        self.horizontalLayout_5.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.effect = QtWidgets.QComboBox(self.frame_4)
        self.effect.setMinimumSize(QtCore.QSize(0, 25))
        self.effect.setMaximumSize(QtCore.QSize(16666, 0))
        self.effect.setStyleSheet("/*font: 12pt \"Segoe MDL2 Assets\";")
        self.effect.setObjectName("effect")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.effect)
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setMinimumSize(QtCore.QSize(75, 0))
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.effect_lv = QtWidgets.QLineEdit(self.frame_4)
        self.effect_lv.setMinimumSize(QtCore.QSize(0, 25))
        self.effect_lv.setMaximumSize(QtCore.QSize(16777215, 25))
        self.effect_lv.setObjectName("effect_lv")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.effect_lv)
        self.label_27 = QtWidgets.QLabel(self.frame_4)
        self.label_27.setObjectName("label_27")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.bfres_template = QtWidgets.QLineEdit(self.frame_4)
        self.bfres_template.setMinimumSize(QtCore.QSize(0, 25))
        self.bfres_template.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bfres_template.setObjectName("bfres_template")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bfres_template)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.bfres = QtWidgets.QLineEdit(self.frame_4)
        self.bfres.setMinimumSize(QtCore.QSize(0, 25))
        self.bfres.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bfres.setObjectName("bfres")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bfres)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.mainmodel = QtWidgets.QLineEdit(self.frame_4)
        self.mainmodel.setMinimumSize(QtCore.QSize(0, 25))
        self.mainmodel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.mainmodel.setObjectName("mainmodel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.mainmodel)
        self.label_25 = QtWidgets.QLabel(self.frame_4)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.korok_mask = QtWidgets.QCheckBox(self.frame_4)
        self.korok_mask.setMinimumSize(QtCore.QSize(0, 25))
        self.korok_mask.setObjectName("korok_mask")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.korok_mask)
        self.label_26 = QtWidgets.QLabel(self.frame_4)
        self.label_26.setMinimumSize(QtCore.QSize(0, 25))
        self.label_26.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_26.setObjectName("label_26")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.label_19 = QtWidgets.QLabel(self.frame_4)
        self.label_19.setMinimumSize(QtCore.QSize(0, 25))
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_19)
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.item1 = QtWidgets.QComboBox(self.frame_4)
        self.item1.setMinimumSize(QtCore.QSize(0, 25))
        self.item1.setObjectName("item1")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.item1)
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.item1_n = QtWidgets.QLineEdit(self.frame_4)
        self.item1_n.setMinimumSize(QtCore.QSize(0, 25))
        self.item1_n.setMaximumSize(QtCore.QSize(16777215, 25))
        self.item1_n.setObjectName("item1_n")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.item1_n)
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.item2 = QtWidgets.QComboBox(self.frame_4)
        self.item2.setMinimumSize(QtCore.QSize(0, 25))
        self.item2.setObjectName("item2")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.item2)
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.item2_n = QtWidgets.QLineEdit(self.frame_4)
        self.item2_n.setMinimumSize(QtCore.QSize(0, 25))
        self.item2_n.setMaximumSize(QtCore.QSize(16777215, 25))
        self.item2_n.setObjectName("item2_n")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.item2_n)
        self.label_23 = QtWidgets.QLabel(self.frame_4)
        self.label_23.setObjectName("label_23")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.item3 = QtWidgets.QComboBox(self.frame_4)
        self.item3.setMinimumSize(QtCore.QSize(0, 25))
        self.item3.setObjectName("item3")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.item3)
        self.Add_armor = QtWidgets.QPushButton(self.frame_4)
        self.Add_armor.setMinimumSize(QtCore.QSize(200, 50))
        self.Add_armor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Add_armor.setObjectName("Add_armor")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.Add_armor)
        self.item3_n = QtWidgets.QLineEdit(self.frame_4)
        self.item3_n.setMinimumSize(QtCore.QSize(0, 25))
        self.item3_n.setMaximumSize(QtCore.QSize(16777215, 25))
        self.item3_n.setObjectName("item3_n")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.item3_n)
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.horizontalLayout_5.addLayout(self.formLayout_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.TabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_5 = QtWidgets.QFrame(self.tab_2)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 711, 621))
        self.frame_5.setStyleSheet("QFrame{\n"
"    background-color: rgb(81, 85, 93);\n"
"    color: white;\n"
"    \n"
"    font: 9pt \"Segoe MDL2 Assets\";\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_49 = QtWidgets.QLabel(self.frame_5)
        self.label_49.setMinimumSize(QtCore.QSize(0, 0))
        self.label_49.setMaximumSize(QtCore.QSize(16666, 16777215))
        self.label_49.setObjectName("label_49")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_49)
        self.base_2 = QtWidgets.QComboBox(self.frame_5)
        self.base_2.setMinimumSize(QtCore.QSize(0, 25))
        self.base_2.setObjectName("base_2")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.base_2)
        self.label_50 = QtWidgets.QLabel(self.frame_5)
        self.label_50.setObjectName("label_50")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_50)
        self.name_2 = QtWidgets.QLineEdit(self.frame_5)
        self.name_2.setMinimumSize(QtCore.QSize(0, 25))
        self.name_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.name_2.setObjectName("name_2")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_2)
        self.label_51 = QtWidgets.QLabel(self.frame_5)
        self.label_51.setObjectName("label_51")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_51)
        self.attack = QtWidgets.QLineEdit(self.frame_5)
        self.attack.setMinimumSize(QtCore.QSize(0, 25))
        self.attack.setMaximumSize(QtCore.QSize(16777215, 25))
        self.attack.setObjectName("attack")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.attack)
        self.label_81 = QtWidgets.QLabel(self.frame_5)
        self.label_81.setObjectName("label_81")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_81)
        self.dur = QtWidgets.QLineEdit(self.frame_5)
        self.dur.setMinimumSize(QtCore.QSize(0, 25))
        self.dur.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dur.setObjectName("dur")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dur)
        self.label_52 = QtWidgets.QLabel(self.frame_5)
        self.label_52.setObjectName("label_52")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_52)
        self.elink_2 = QtWidgets.QLineEdit(self.frame_5)
        self.elink_2.setMinimumSize(QtCore.QSize(0, 25))
        self.elink_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.elink_2.setObjectName("elink_2")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.elink_2)
        self.label_53 = QtWidgets.QLabel(self.frame_5)
        self.label_53.setObjectName("label_53")
        self.formLayout_10.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_53)
        self.slink_2 = QtWidgets.QLineEdit(self.frame_5)
        self.slink_2.setMinimumSize(QtCore.QSize(0, 25))
        self.slink_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.slink_2.setObjectName("slink_2")
        self.formLayout_10.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.slink_2)
        self.label_54 = QtWidgets.QLabel(self.frame_5)
        self.label_54.setObjectName("label_54")
        self.formLayout_10.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_54)
        self.profile_2 = QtWidgets.QComboBox(self.frame_5)
        self.profile_2.setMinimumSize(QtCore.QSize(0, 25))
        self.profile_2.setObjectName("profile_2")
        self.formLayout_10.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.profile_2)
        self.label_75 = QtWidgets.QLabel(self.frame_5)
        self.label_75.setObjectName("label_75")
        self.formLayout_10.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_75)
        self.islifeinfinite = QtWidgets.QCheckBox(self.frame_5)
        self.islifeinfinite.setMinimumSize(QtCore.QSize(0, 25))
        self.islifeinfinite.setText("")
        self.islifeinfinite.setObjectName("islifeinfinite")
        self.formLayout_10.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.islifeinfinite)
        self.label_82 = QtWidgets.QLabel(self.frame_5)
        self.label_82.setObjectName("label_82")
        self.formLayout_10.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_82)
        self.sheath = QtWidgets.QComboBox(self.frame_5)
        self.sheath.setMinimumSize(QtCore.QSize(0, 25))
        self.sheath.setObjectName("sheath")
        self.formLayout_10.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.sheath)
        self.label_56 = QtWidgets.QLabel(self.frame_5)
        self.label_56.setObjectName("label_56")
        self.formLayout_10.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_56)
        self.physics_2 = QtWidgets.QLineEdit(self.frame_5)
        self.physics_2.setMinimumSize(QtCore.QSize(0, 25))
        self.physics_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.physics_2.setObjectName("physics_2")
        self.formLayout_10.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.physics_2)
        self.label_57 = QtWidgets.QLabel(self.frame_5)
        self.label_57.setObjectName("label_57")
        self.formLayout_10.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_57)
        self.price_2 = QtWidgets.QLineEdit(self.frame_5)
        self.price_2.setMinimumSize(QtCore.QSize(0, 25))
        self.price_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.price_2.setObjectName("price_2")
        self.formLayout_10.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.price_2)
        self.label_58 = QtWidgets.QLabel(self.frame_5)
        self.label_58.setObjectName("label_58")
        self.formLayout_10.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_58)
        self.name_desc_2 = QtWidgets.QLineEdit(self.frame_5)
        self.name_desc_2.setMinimumSize(QtCore.QSize(0, 25))
        self.name_desc_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.name_desc_2.setObjectName("name_desc_2")
        self.formLayout_10.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.name_desc_2)
        self.label_59 = QtWidgets.QLabel(self.frame_5)
        self.label_59.setObjectName("label_59")
        self.formLayout_10.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_59)
        self.desc_2 = QtWidgets.QTextEdit(self.frame_5)
        self.desc_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.desc_2.setStyleSheet("background-color: rgb(149, 165, 166);\n"
"font: 10pt \"Segoe MDL2 Assets\";")
        self.desc_2.setObjectName("desc_2")
        self.formLayout_10.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.desc_2)
        self.horizontalLayout_3.addLayout(self.formLayout_10)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_70 = QtWidgets.QLabel(self.frame_5)
        self.label_70.setMinimumSize(QtCore.QSize(0, 25))
        self.label_70.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_70.setObjectName("label_70")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_70)
        self.label_61 = QtWidgets.QLabel(self.frame_5)
        self.label_61.setMinimumSize(QtCore.QSize(75, 25))
        self.label_61.setObjectName("label_61")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_61)
        self.magic = QtWidgets.QLineEdit(self.frame_5)
        self.magic.setMinimumSize(QtCore.QSize(0, 25))
        self.magic.setMaximumSize(QtCore.QSize(16777215, 25))
        self.magic.setObjectName("magic")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.magic)
        self.label_64 = QtWidgets.QLabel(self.frame_5)
        self.label_64.setMinimumSize(QtCore.QSize(75, 25))
        self.label_64.setText("")
        self.label_64.setObjectName("label_64")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_64)
        self.ismagicinf = QtWidgets.QCheckBox(self.frame_5)
        self.ismagicinf.setMinimumSize(QtCore.QSize(0, 25))
        self.ismagicinf.setObjectName("ismagicinf")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ismagicinf)
        self.label_69 = QtWidgets.QLabel(self.frame_5)
        self.label_69.setMinimumSize(QtCore.QSize(0, 25))
        self.label_69.setObjectName("label_69")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_69)
        self.magicgravity = QtWidgets.QLineEdit(self.frame_5)
        self.magicgravity.setMinimumSize(QtCore.QSize(0, 25))
        self.magicgravity.setMaximumSize(QtCore.QSize(16777215, 25))
        self.magicgravity.setObjectName("magicgravity")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.magicgravity)
        self.label_71 = QtWidgets.QLabel(self.frame_5)
        self.label_71.setMinimumSize(QtCore.QSize(0, 25))
        self.label_71.setObjectName("label_71")
        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_71)
        self.magicspeed = QtWidgets.QLineEdit(self.frame_5)
        self.magicspeed.setMinimumSize(QtCore.QSize(0, 25))
        self.magicspeed.setMaximumSize(QtCore.QSize(16777215, 25))
        self.magicspeed.setObjectName("magicspeed")
        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.magicspeed)
        self.label_72 = QtWidgets.QLabel(self.frame_5)
        self.label_72.setMinimumSize(QtCore.QSize(0, 25))
        self.label_72.setObjectName("label_72")
        self.formLayout_8.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_72)
        self.magicradius = QtWidgets.QLineEdit(self.frame_5)
        self.magicradius.setMinimumSize(QtCore.QSize(0, 25))
        self.magicradius.setMaximumSize(QtCore.QSize(16777215, 25))
        self.magicradius.setObjectName("magicradius")
        self.formLayout_8.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.magicradius)
        self.label_73 = QtWidgets.QLabel(self.frame_5)
        self.label_73.setMinimumSize(QtCore.QSize(0, 25))
        self.label_73.setObjectName("label_73")
        self.formLayout_8.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_73)
        self.magicrange = QtWidgets.QLineEdit(self.frame_5)
        self.magicrange.setMinimumSize(QtCore.QSize(0, 25))
        self.magicrange.setMaximumSize(QtCore.QSize(16777215, 25))
        self.magicrange.setObjectName("magicrange")
        self.formLayout_8.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.magicrange)
        self.label_74 = QtWidgets.QLabel(self.frame_5)
        self.label_74.setMinimumSize(QtCore.QSize(0, 25))
        self.label_74.setObjectName("label_74")
        self.formLayout_8.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_74)
        self.magicpower = QtWidgets.QLineEdit(self.frame_5)
        self.magicpower.setMinimumSize(QtCore.QSize(0, 25))
        self.magicpower.setMaximumSize(QtCore.QSize(16777215, 25))
        self.magicpower.setObjectName("magicpower")
        self.formLayout_8.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.magicpower)
        self.label_87 = QtWidgets.QLabel(self.frame_5)
        self.label_87.setText("")
        self.label_87.setObjectName("label_87")
        self.formLayout_8.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_87)
        self.anims = QtWidgets.QCheckBox(self.frame_5)
        self.anims.setMinimumSize(QtCore.QSize(0, 25))
        self.anims.setObjectName("anims")
        self.formLayout_8.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.anims)
        self.label_65 = QtWidgets.QLabel(self.frame_5)
        self.label_65.setMinimumSize(QtCore.QSize(0, 30))
        self.label_65.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_65.setObjectName("label_65")
        self.formLayout_8.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_65)
        self.label_62 = QtWidgets.QLabel(self.frame_5)
        self.label_62.setMinimumSize(QtCore.QSize(0, 25))
        self.label_62.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_62.setText("")
        self.label_62.setObjectName("label_62")
        self.formLayout_8.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.label_62)
        self.label_55 = QtWidgets.QLabel(self.frame_5)
        self.label_55.setObjectName("label_55")
        self.formLayout_8.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_55)
        self.item1_2 = QtWidgets.QComboBox(self.frame_5)
        self.item1_2.setMinimumSize(QtCore.QSize(0, 25))
        self.item1_2.setObjectName("item1_2")
        self.formLayout_8.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.item1_2)
        self.item1_n_2 = QtWidgets.QLineEdit(self.frame_5)
        self.item1_n_2.setMinimumSize(QtCore.QSize(0, 25))
        self.item1_n_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.item1_n_2.setObjectName("item1_n_2")
        self.formLayout_8.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.item1_n_2)
        self.label_76 = QtWidgets.QLabel(self.frame_5)
        self.label_76.setObjectName("label_76")
        self.formLayout_8.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_76)
        self.item2_2 = QtWidgets.QComboBox(self.frame_5)
        self.item2_2.setMinimumSize(QtCore.QSize(0, 25))
        self.item2_2.setObjectName("item2_2")
        self.formLayout_8.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.item2_2)
        self.label_77 = QtWidgets.QLabel(self.frame_5)
        self.label_77.setObjectName("label_77")
        self.formLayout_8.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_77)
        self.item2_n_2 = QtWidgets.QLineEdit(self.frame_5)
        self.item2_n_2.setMinimumSize(QtCore.QSize(0, 25))
        self.item2_n_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.item2_n_2.setObjectName("item2_n_2")
        self.formLayout_8.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.item2_n_2)
        self.label_78 = QtWidgets.QLabel(self.frame_5)
        self.label_78.setObjectName("label_78")
        self.formLayout_8.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_78)
        self.item3_2 = QtWidgets.QComboBox(self.frame_5)
        self.item3_2.setMinimumSize(QtCore.QSize(0, 25))
        self.item3_2.setObjectName("item3_2")
        self.formLayout_8.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.item3_2)
        self.label_80 = QtWidgets.QLabel(self.frame_5)
        self.label_80.setObjectName("label_80")
        self.formLayout_8.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_80)
        self.item3_n_2 = QtWidgets.QLineEdit(self.frame_5)
        self.item3_n_2.setMinimumSize(QtCore.QSize(0, 25))
        self.item3_n_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.item3_n_2.setObjectName("item3_n_2")
        self.formLayout_8.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.item3_n_2)
        self.label_79 = QtWidgets.QLabel(self.frame_5)
        self.label_79.setObjectName("label_79")
        self.formLayout_8.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_79)
        self.Add_weapon = QtWidgets.QPushButton(self.frame_5)
        self.Add_weapon.setMinimumSize(QtCore.QSize(0, 30))
        self.Add_weapon.setObjectName("Add_weapon")
        self.formLayout_8.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.Add_weapon)
        self.label_86 = QtWidgets.QLabel(self.frame_5)
        self.label_86.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_86.setText("")
        self.label_86.setObjectName("label_86")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_86)
        self.horizontalLayout_3.addLayout(self.formLayout_8)
        self.TabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.TabWidget, 1, 0, 2, 1)
        self.Right_column = QtWidgets.QFrame(self.frame)
        self.Right_column.setObjectName("Right_column")
        self.gridLayout = QtWidgets.QGridLayout(self.Right_column)
        self.gridLayout.setObjectName("gridLayout")
        self.edit = QtWidgets.QPushButton(self.Right_column)
        self.edit.setMinimumSize(QtCore.QSize(200, 25))
        self.edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit.setObjectName("edit")
        self.gridLayout.addWidget(self.edit, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Mod_content = QtWidgets.QListWidget(self.Right_column)
        self.Mod_content.setMaximumSize(QtCore.QSize(250, 16777215))
        self.Mod_content.setStyleSheet("background-color: rgb(46, 68, 91);\n"
"    color: rgb(220, 220, 220);")
        self.Mod_content.setObjectName("Mod_content")
        self.gridLayout.addWidget(self.Mod_content, 1, 0, 1, 1)
        self.Clear_list = QtWidgets.QPushButton(self.Right_column)
        self.Clear_list.setMinimumSize(QtCore.QSize(200, 25))
        self.Clear_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Clear_list.setObjectName("Clear_list")
        self.gridLayout.addWidget(self.Clear_list, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Options = QtWidgets.QPushButton(self.Right_column)
        self.Options.setMinimumSize(QtCore.QSize(200, 25))
        self.Options.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Options.setObjectName("Options")
        self.gridLayout.addWidget(self.Options, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_24 = QtWidgets.QLabel(self.Right_column)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1)
        self.Remove_from_mod = QtWidgets.QPushButton(self.Right_column)
        self.Remove_from_mod.setMinimumSize(QtCore.QSize(200, 25))
        self.Remove_from_mod.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Remove_from_mod.setObjectName("Remove_from_mod")
        self.gridLayout.addWidget(self.Remove_from_mod, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.Right_column, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        self.patreon = QtWidgets.QToolButton(self.centralwidget)
        self.patreon.setGeometry(QtCore.QRect(120, 790, 103, 103))
        self.patreon.setMinimumSize(QtCore.QSize(80, 40))
        self.patreon.setStyleSheet("background-image : url(res/patreon.png);\n"
"background-color: rgb(47, 49, 54);\n"
"border: none;")
        self.patreon.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/ppatreon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.patreon.setIcon(icon1)
        self.patreon.setIconSize(QtCore.QSize(100, 100))
        self.patreon.setObjectName("patreon")
        SIC.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SIC)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 25))
        self.menubar.setObjectName("menubar")
        self.menuQuit = QtWidgets.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        self.menuMod = QtWidgets.QMenu(self.menubar)
        self.menuMod.setObjectName("menuMod")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        SIC.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(SIC)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/open.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(SIC)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("res/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(SIC)
        self.actionSave_as.setIcon(icon3)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionQuit = QtWidgets.QAction(SIC)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("res/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon4)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOptions = QtWidgets.QAction(SIC)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("res/options.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOptions.setIcon(icon5)
        self.actionOptions.setObjectName("actionOptions")
        self.actionCreate_mod = QtWidgets.QAction(SIC)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("res/create.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_mod.setIcon(icon6)
        self.actionCreate_mod.setObjectName("actionCreate_mod")
        self.actionClear_list = QtWidgets.QAction(SIC)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("res/shredder.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear_list.setIcon(icon7)
        self.actionClear_list.setObjectName("actionClear_list")
        self.actionReadme = QtWidgets.QAction(SIC)
        self.actionReadme.setObjectName("actionReadme")
        self.menuQuit.addAction(self.actionOpen)
        self.menuQuit.addAction(self.actionSave)
        self.menuQuit.addAction(self.actionSave_as)
        self.menuQuit.addSeparator()
        self.menuQuit.addAction(self.actionOptions)
        self.menuQuit.addSeparator()
        self.menuQuit.addAction(self.actionQuit)
        self.menuMod.addAction(self.actionCreate_mod)
        self.menuMod.addAction(self.actionClear_list)
        self.menuAbout.addAction(self.actionReadme)
        self.menubar.addAction(self.menuQuit.menuAction())
        self.menubar.addAction(self.menuMod.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(SIC)
        self.TabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(SIC)

    def retranslateUi(self, SIC):
        _translate = QtCore.QCoreApplication.translate
        SIC.setWindowTitle(_translate("SIC", "Standalone Item Creator for BOTW"))
        self.Create_mod.setText(_translate("SIC", "Create mod"))
        self.label_83.setText(_translate("SIC", "Game language"))
        self.label_84.setText(_translate("SIC", "Mod name "))
        self.label_14.setText(_translate("SIC", "Mode       "))
        self.wiiu_radiobutton.setText(_translate("SIC", "Wii-U"))
        self.switch_radiobutton.setText(_translate("SIC", "Switch"))
        self.label_85.setText(_translate("SIC", "Shop"))
        self.label_28.setText(_translate("SIC", "Template"))
        self.label_4.setText(_translate("SIC", "Armor ID"))
        self.label_5.setText(_translate("SIC", "Defence"))
        self.label_6.setText(_translate("SIC", "Elink"))
        self.label_7.setText(_translate("SIC", "Slink"))
        self.label_8.setText(_translate("SIC", "Profile"))
        self.label_9.setText(_translate("SIC", "Series"))
        self.label_10.setText(_translate("SIC", "Physics"))
        self.label_11.setText(_translate("SIC", "Price"))
        self.label_12.setText(_translate("SIC", "Item name"))
        self.label_13.setText(_translate("SIC", "Description"))
        self.label_15.setText(_translate("SIC", "Effect"))
        self.label_16.setText(_translate("SIC", "Effect level"))
        self.label_27.setText(_translate("SIC", "Bfres template"))
        self.label.setText(_translate("SIC", "Bfres name"))
        self.label_2.setText(_translate("SIC", "Model name"))
        self.korok_mask.setText(_translate("SIC", "Custom animations"))
        self.label_26.setText(_translate("SIC", "Crafting"))
        self.label_17.setText(_translate("SIC", "First item"))
        self.label_18.setText(_translate("SIC", "amount"))
        self.label_20.setText(_translate("SIC", "Second item"))
        self.label_21.setText(_translate("SIC", "amount"))
        self.label_23.setText(_translate("SIC", "Third item"))
        self.Add_armor.setText(_translate("SIC", "Add armor"))
        self.label_22.setText(_translate("SIC", "amount"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab), _translate("SIC", "Add armor"))
        self.label_49.setText(_translate("SIC", "Template"))
        self.label_50.setText(_translate("SIC", "Weapon ID"))
        self.label_51.setText(_translate("SIC", "Attack"))
        self.label_81.setText(_translate("SIC", "Durability"))
        self.label_52.setText(_translate("SIC", "Elink"))
        self.label_53.setText(_translate("SIC", "Slink"))
        self.label_54.setText(_translate("SIC", "Profile"))
        self.label_75.setText(_translate("SIC", "Unbreakable"))
        self.label_82.setText(_translate("SIC", "Sheath"))
        self.label_56.setText(_translate("SIC", "Physics"))
        self.label_57.setText(_translate("SIC", "Price"))
        self.label_58.setText(_translate("SIC", "Item name"))
        self.label_59.setText(_translate("SIC", "Description"))
        self.label_70.setText(_translate("SIC", "Magic"))
        self.label_61.setText(_translate("SIC", "Type"))
        self.ismagicinf.setText(_translate("SIC", "Infinite power"))
        self.label_69.setText(_translate("SIC", "Gravity"))
        self.label_71.setText(_translate("SIC", "Speed"))
        self.label_72.setText(_translate("SIC", "Radius"))
        self.label_73.setText(_translate("SIC", "Range"))
        self.label_74.setText(_translate("SIC", "Power"))
        self.anims.setText(_translate("SIC", "Custom animations"))
        self.label_65.setText(_translate("SIC", "Crafting"))
        self.label_55.setText(_translate("SIC", "First item"))
        self.label_76.setText(_translate("SIC", "amount"))
        self.label_77.setText(_translate("SIC", "Second item"))
        self.label_78.setText(_translate("SIC", "amount"))
        self.label_80.setText(_translate("SIC", "Third item"))
        self.label_79.setText(_translate("SIC", "amount"))
        self.Add_weapon.setText(_translate("SIC", "Add weapon"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_2), _translate("SIC", "Add weapon"))
        self.edit.setText(_translate("SIC", "Edit"))
        self.Clear_list.setText(_translate("SIC", "Clear list"))
        self.Options.setText(_translate("SIC", "Options"))
        self.label_24.setText(_translate("SIC", "Mod content"))
        self.Remove_from_mod.setText(_translate("SIC", "Remove from mod"))
        self.menuQuit.setTitle(_translate("SIC", "File"))
        self.menuMod.setTitle(_translate("SIC", "Mod"))
        self.menuAbout.setTitle(_translate("SIC", "About"))
        self.actionOpen.setText(_translate("SIC", "Open"))
        self.actionSave.setText(_translate("SIC", "Save"))
        self.actionSave_as.setText(_translate("SIC", "Save as"))
        self.actionQuit.setText(_translate("SIC", "Quit"))
        self.actionOptions.setText(_translate("SIC", "Options"))
        self.actionCreate_mod.setText(_translate("SIC", "Create mod"))
        self.actionClear_list.setText(_translate("SIC", "Clear list"))
        self.actionReadme.setText(_translate("SIC", "Readme"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SIC = QtWidgets.QMainWindow()
    ui = Ui_SIC()
    ui.setupUi(SIC)
    SIC.show()
    sys.exit(app.exec_())
