import configparser
import os
from PyQt5.QtWidgets import QWidget, QFileDialog

from ConfigClass import Config
from Options import Ui_Options
from Select_file import Select_file


class options_window(QWidget, Ui_Options):

    def __init__(self,  valid_rgb, invalid_rgb, config_file, Style_Sheet='', parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.valid_rgb = valid_rgb
        self.invalid_rgb = invalid_rgb
        self.config_file = config_file
        self.setWindowTitle('Options')
        self.setFixedSize(self.size())
        if Style_Sheet:            self.Style_Sheet = Style_Sheet
        else:                      self.Style_Sheet = ''

        self.frame.setStyleSheet(self.Style_Sheet)
        self.cancel_button.clicked.connect(lambda: self.close())
        self.ok_button.clicked.connect(self.Apply)
        self.switchpath.editingFinished.connect(lambda: self.validate(self.switchpath))
        self.wiiupath.editingFinished.connect(lambda: self.validate(self.wiiupath))
        self.modspath.editingFinished.connect(lambda: self.validate(self.modspath))
        self.validate(self.switchpath)
        self.validate(self.wiiupath)
        self.validate(self.modspath)
        #self.modspath.editingFinished.connect(lambda: self.validate(self.wiiupath))
        self.wiiupath_browse.clicked.connect(self.wiiupath_browse_f)
        self.wiiupath_update_browse.clicked.connect(self.wiiu_update_browse_f)
        self.switchpath_browse.clicked.connect(self.switchpath_browse_f)
        self.modspath_browse.clicked.connect(self.modspath_browse_f)
        self.import_from_bcml.clicked.connect(self.import_from_bcml_f)
        self.select_file = Select_file(stylesheet=self.Style_Sheet)

    def import_from_bcml_f(self):
        conf = Config()
        conf.get_paths()
        conf.save_to_config()
        self.load_from_config()

    def load_from_config(self):
        conf = Config()
        config = configparser.ConfigParser()
        config.read(conf.config_file)

        self.switchpath.setText(config['DEFAULT']['switch_path'])
        self.wiiupath.setText(config['DEFAULT']['wiiu_path'])
        self.wiiu_update.setText(config['DEFAULT']['wiiu_update'])
        self.modspath.setText(config['DEFAULT']['mods_path'])
        self.lang.setText(config['DEFAULT']['lang'])
        if config['DEFAULT']['is_bcml_settings'] == "True": self.is_bcml_settings.setChecked(True)
        else: self.is_bcml_settings.setChecked(False)
        if os.path.exists(config['DEFAULT']['switch_path']):
            self.switchpath.setStyleSheet(f"background-color: {self.valid_rgb};")
        else:
            self.switchpath.setStyleSheet(f"background-color: {self.invalid_rgb};")
        if os.path.exists(config['DEFAULT']['wiiu_path']):
            self.wiiupath.setStyleSheet(f"background-color: {self.valid_rgb};")
        else:
            self.wiiupath.setStyleSheet(f"background-color: {self.invalid_rgb};")

    def modspath_browse_f(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select mods directory"))
        if folder: self.modspath.setText(folder)
        self.validate(self.modspath)

    def switchpath_browse_f(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select Switch dump directory"))
        if folder: self.switchpath.setText(folder)
        self.validate(self.switchpath)

    def wiiupath_browse_f(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select WiiU base game directory"))
        if folder: self.wiiupath.setText(folder)
        self.validate(self.wiiupath)

    def wiiu_update_browse_f(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select WiiU update directory"))
        if folder: self.wiiupath.setText(folder)
        self.validate(self.wiiupath)

    def validate(self, object):
        if object.text():
            if os.path.exists(object.text()):
                object.setStyleSheet(f"background-color: {self.valid_rgb};")
            else:
                object.setStyleSheet(f"background-color: {self.invalid_rgb};")


    def Apply(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        config['DEFAULT']['switch_path'] = self.switchpath.text()
        config['DEFAULT']['wiiu_path'] = self.wiiupath.text()
        config['DEFAULT']['wiiu_update'] = self.wiiu_update.text()
        config['DEFAULT']['mods_path'] = self.modspath.text()
        config['DEFAULT']['is_bcml_settings'] = str(self.is_bcml_settings.isChecked())
        with open(self.config_file, 'w') as f:  # save
            config.write(f)
        self.close()