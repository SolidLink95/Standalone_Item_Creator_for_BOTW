# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prompt.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(646, 334)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.message = QtWidgets.QTextBrowser(self.frame)
        self.message.setObjectName("message")
        self.gridLayout.addWidget(self.message, 0, 0, 1, 1)
        self.YesButton = QtWidgets.QPushButton(self.frame)
        self.YesButton.setMinimumSize(QtCore.QSize(0, 35))
        self.YesButton.setObjectName("YesButton")
        self.gridLayout.addWidget(self.YesButton, 2, 0, 1, 1)
        self.OkButton = QtWidgets.QPushButton(self.frame)
        self.OkButton.setMinimumSize(QtCore.QSize(0, 35))
        self.OkButton.setObjectName("OkButton")
        self.gridLayout.addWidget(self.OkButton, 1, 0, 1, 1)
        self.NoButton = QtWidgets.QPushButton(self.frame)
        self.NoButton.setMinimumSize(QtCore.QSize(0, 35))
        self.NoButton.setObjectName("NoButton")
        self.gridLayout.addWidget(self.NoButton, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Message"))
        self.YesButton.setText(_translate("Form", "Yes"))
        self.OkButton.setText(_translate("Form", "OK"))
        self.NoButton.setText(_translate("Form", "No"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
