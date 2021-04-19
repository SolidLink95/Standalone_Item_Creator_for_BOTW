import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class Select_file(QWidget):

    def __init__(self,stylesheet=''):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        self.Style_Sheet = stylesheet
        if self.Style_Sheet: self.setStyleSheet(self.Style_Sheet)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self.openFileNameDialog()
        #self.openFileNamesDialog()
        #self.saveFileDialog()

        #self.show()

    def openFileNameDialog(self):
        #dialog = QFileDialog
        #dialog.setStyleSheet(self.Style_Sheet)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open JSON file", "",
                                                  "JSON (*.json);;All Files (*)")

        return fileName

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)

        return files

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save JSON file", "",
                                                  "JSON (*.json);;All Files (*)")
        return fileName

    def openFolderDialog(self, path=''):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folder= str(QFileDialog.getExistingDirectory(self, f"Select {path} Directory"))
        return folder
