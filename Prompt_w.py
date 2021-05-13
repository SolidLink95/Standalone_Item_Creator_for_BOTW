from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget

from Prompt import Ui_Form


class prompt_window(QWidget, Ui_Form):

    def __init__(self,  valid_rgb, invalid_rgb, config_file,message='', Style_Sheet='', title='Message', parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.valid_rgb = valid_rgb
        self.invalid_rgb = invalid_rgb
        self.config_file = config_file
        self.setWindowTitle(title)
        self.setFixedSize(self.size())
        self.Style_Sheet = Style_Sheet
        self.choice = None
        self.frame.setStyleSheet(self.Style_Sheet)
        self.message.setPlainText(message)
        self.icons = {
            "Message" : "icon.ico",
            "Confirm" : "icon.ico",
            "Warning" : "Warning.png",
            "Error" : "Error.png"
        }
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(f"res/{self.icons[title]}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(self.icon)
        self.buttons()


    def buttons(self):
        self.OkButton.clicked.connect(lambda : self.close())
        self.YesButton.clicked.connect(lambda : self.close())
        self.NoButton.clicked.connect(lambda : self.close())
        if self.windowTitle() == 'Message':
            self.OkButton.show()
            self.YesButton.hide()
            self.NoButton.hide()
            self.icon = QtGui.QIcon()
            self.icon.addPixmap(QtGui.QPixmap(f"res/{self.icons[self.windowTitle()]}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(self.icon)
        elif self.windowTitle() == 'Warning':
            self.OkButton.hide()
            self.YesButton.show()
            self.NoButton.show()
            self.icon = QtGui.QIcon()
            self.icon.addPixmap(QtGui.QPixmap(f"res/{self.icons[self.windowTitle()]}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(self.icon)
        elif self.windowTitle() == 'Confirm':
            self.OkButton.hide()
            self.YesButton.show()
            self.NoButton.show()
            self.icon = QtGui.QIcon()
            self.icon.addPixmap(QtGui.QPixmap(f"res/{self.icons[self.windowTitle()]}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(self.icon)
        elif self.windowTitle() == 'Error':
            self.OkButton.show()
            self.YesButton.hide()
            self.NoButton.hide()
            self.icon = QtGui.QIcon()
            self.icon.addPixmap(QtGui.QPixmap(f"res/{self.icons[self.windowTitle()]}"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(self.icon)

    def click_ok(self):
        self.close()
        self.choice =  True

    def click_yes(self):
        self.close()
        self.choice =  True

    def click_no(self):
        self.close()
        self.choice =  False