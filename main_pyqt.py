import configparser
import json, shutil
import os
import sys
from copy import deepcopy
import PySimpleGUI as sg
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QCompleter, QWidget, QSizePolicy, QHBoxLayout, QGraphicsScene
from Option_w import options_window
from Prompt_w import prompt_window
from ShopData import get_raw_data
from files_manage import create_folder, get_main_json, file_to_json, get_mods_path, get_res, json_to_file, file_to_str, \
    get_langs, get_endianness, get_def_path
import oead
from load_input import Load_Input
from files_manage import clear_json
from Pyqt_gui import Ui_SIC
from Select_file import Select_file
from Readme import readme_window
from sarc_class import Sarc_file

config_file = 'config.ini'
valid_rgb = 'rgb(21, 155, 130)'
invalid_rgb = 'rgb(239, 74, 70)'
BG_COLOR = [47, 49, 54]

class Window(QMainWindow, Ui_SIC):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = clear_json()
        self.config = 'config.ini'
        self.shops = get_res('shops')
        self.shops_rev = get_res('shops_rev')
        self.actors = get_res('Actors')
        self.weapons = get_res('weapons')
        self.armors = get_res('armors')
        self.items = get_res('items')
        self.items_rev = get_res('items_rev')
        self.magic_types = get_res('magic')
        self.effects = get_res('Effects')
        self.effects_adv_rev = get_res('Effects_adv_rev')
        self.series_types = get_res('Series')
        self.sheaths = get_res('Sheaths')
        self.armor_profiles = ['', 'ArmorHead', 'ArmorLower', 'ArmorUpper']
        self.wep_profiles = ['', 'WeaponSmallSword', 'WeaponLargeSword', 'WeaponBow', 'WeaponSpear', 'WeaponShield']
        self.langs = get_langs()
        self.options_w = options_window(valid_rgb=valid_rgb,invalid_rgb=invalid_rgb, config_file=config_file)
        self.readme_w = readme_window()
        self.prompt_w = prompt_window(valid_rgb, invalid_rgb, config_file, Style_Sheet=self.styleSheet())
        self.setupUi(self)
        self.setup_ui_local()


    def setup_ui_local(self):
        # variables
        for elem in self.shops:
            self.shop_default = elem
            break
        #Buttons
        self.Create_mod.clicked.connect(self.create_mod)
        self.Add_weapon.clicked.connect(self.add_weapon)
        self.Add_armor.clicked.connect(self.add_armor)
        self.Clear_list.clicked.connect(self.clear_list)
        self.Remove_from_mod.clicked.connect(self.remove_from_mod)
        self.Options.clicked.connect(self.options)
        self.patreon.clicked.connect(lambda : os.system(f'start https://www.patreon.com/user?u=32002965'))
        self.patreon.hide()
        self.Upgrade_armors.hide()
        self.edit.clicked.connect(self.edit_click)

        #combo boxes
        medium_h = 25
        big_h = 30
        self.profile_2.addItems(self.wep_profiles)
        self.profile.addItems(self.armor_profiles)
        self.Lang.addItems(self.langs)
        self.base_2.addItems(self.weapons)
        self.base.addItems(self.armors)
        self.series.addItems(self.series_types)
        self.item1_2.addItems(self.items)
        self.item2_2.addItems(self.items)
        self.item3_2.addItems(self.items)
        self.item1.addItems(self.items)
        self.item2.addItems(self.items)
        self.item3.addItems(self.items)
        self.sheath.addItems(self.sheaths)
        self.shop.addItems(self.shops)
        #self.effect.addItems(self.effects)
        for eff in self.effects:
            self.effect.addItem(QIcon(f'res\\{eff}.png'), eff)
        self.effect.adjustSize()

        self.item1_2.setMaxVisibleItems(medium_h)
        self.item2_2.setMaxVisibleItems(medium_h)
        self.item3_2.setMaxVisibleItems(medium_h)
        self.item1.setMaxVisibleItems(medium_h)
        self.item2.setMaxVisibleItems(medium_h)
        self.item3.setMaxVisibleItems(medium_h)
        self.base_2.setMaxVisibleItems(big_h)
        self.base.setMaxVisibleItems(big_h)
        self.sheath.setMaxVisibleItems(medium_h)
        self.effect.setMaxVisibleItems(medium_h)
        self.series.setMaxVisibleItems(medium_h)
        self.shop.setMaxVisibleItems(big_h)

        #radio buttons
        if get_endianness(): self.wiiu_radiobutton.setChecked(True)
        else: self.switch_radiobutton.setChecked(True)

        #autocompleters
        #self.base.setCompleter(QCompleter(self.armors))
        self.magic.setCompleter(QCompleter(self.magic_types))
        #self.base_2.setCompleter(QCompleter(self.weapons))

        #menu bar
        self.actionOpen.triggered.connect(self.open_json)
        self.actionQuit.triggered.connect(lambda : self.close())
        self.actionOptions.triggered.connect(self.options)
        self.actionSave.triggered.connect(lambda : json_to_file(f'jsons\\{self.pack_name.text()}.json', self.data))
        self.actionSave_as.triggered.connect(self.save_as)
        self.actionReadme.triggered.connect(self.readme)

        #other windows
        self.sel_file = Select_file()
        self.sel_file.setStyleSheet("""    background-color: rgb(47, 49, 54);
            color: rgb(220, 220, 220);
            font: 10pt "Segoe MDL2 Assets";""")

        #rand
        self.check_mode()

        #resizing setFixedSize
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.frame)
        self.centralwidget.setLayout(self.layout)
        pal = self.palette()
        pal.setColor(QPalette.Window, QColor(BG_COLOR[0],BG_COLOR[1],BG_COLOR[2]))
        self.setPalette(pal)
        #self.frame. = self.frame.styleSheet.replace('font: 10pt', 'font: 6pt')
        #style = str(self.frame.styleSheet).replace('font\: 10pt', 'font\: 6pt')
        #self.label_28.setStyleSheet('font: 8pt "Segoe MDL2 Assets";')
        #self.setLayout(self.layout)


    def readme(self):
        self.readme_w.load_txt()
        self.readme_w.show()

    def set_up_effects(self):
        effects_adv = get_res('Effects_adv')
        self.effect.addItem('None')
        for elem in effects_adv:
            self.effect.addItem(QIcon(f'res\\{elem}.png'), effects_adv[elem])

    def edit_click(self):
        print('edit click')
        try:
            x = self.Mod_content.currentItem().text()
        except:
            print('Error editing item')
            return
        if not x: return
        if x in self.data['Armors']:
            self.TabWidget.setCurrentIndex(0)
            for elem in self.armors:
                if self.armors[elem] == self.data['Armors'][x]['base']:
                    self.base.setCurrentText(elem)
                    break
                arm = self.data['Armors'][x]
                self.name.setText(arm['name'])
                self.defence.setText(arm['defence'])
                if 'bfres_template' in arm: self.bfres_template.setText(arm['bfres_template'])
                if 'bfres' in arm: self.bfres.setText(arm['bfres'])
                if 'mainmodel' in arm: self.mainmodel.setText(arm['mainmodel'])
                if 'shop' in arm: self.shop.setCurrentText(self.shops_rev[arm["shop"]])
                else: self.shop.setCurrentText(self.shop_default)
                self.elink.setText(arm['elink'])
                self.slink.setText(arm['slink'])
                self.profile.setCurrentText(arm['profile'])
                self.effect.setCurrentText(arm['effect'])
                self.series.setCurrentText(arm['series'])
                self.effect_lv.setText(arm['effect_lv'])
                self.price.setText(arm['price'])
                self.physics.setText(arm['physics'])
                self.name_desc.setText(arm['name_desc'])
                self.desc.setPlainText(arm['desc'])
                self.korok_mask.setChecked(bool(arm['korok_mask']))
                self.item1.setCurrentText(self.items_rev[arm['Crafting']['item1']])
                self.item2.setCurrentText(self.items_rev[arm['Crafting']['item2']])
                self.item3.setCurrentText(self.items_rev[arm['Crafting']['item3']])
                self.item1_n.setText(arm['Crafting']['item1_n'])
                self.item2_n.setText(arm['Crafting']['item2_n'])
                self.item3_n.setText(arm['Crafting']['item3_n'])
        elif x in self.data['Weapons']:
            self.TabWidget.setCurrentIndex(1)
            for elem in self.weapons:
                if self.weapons[elem] == self.data['Weapons'][x]['base']:
                    self.base_2.setCurrentText(elem)
                    break
                wep = self.data['Weapons'][x]
                self.name_2.setText(wep['name'])
                self.attack.setText(wep['attack'])
                if 'shop' in wep: self.shop.setCurrentText(self.shops_rev[wep["shop"]])
                else: self.shop.setCurrentText(self.shop_default)
                self.dur.setText(wep['dur'])
                self.islifeinfinite.setChecked(bool(wep['islifeinfinite']))
                self.sheath.setCurrentText(wep['sheath'])
                self.elink_2.setText(wep['elink'])
                self.slink_2.setText(wep['slink'])
                self.profile_2.setCurrentText(wep['profile'])
                self.magic.setText(wep['magic'])
                self.magicspeed.setText(wep['magicspeed'])
                self.magicradius.setText(wep['magicradius'])
                self.magicrange.setText(wep['magicrange'])
                self.magicpower.setText(wep['magicpower'])
                self.magicgravity.setText(wep['magicgravity'])
                self.ismagicinf.setChecked(bool(wep['ismagicinf']))
                self.physics_2.setText(wep['physics'])
                self.price_2.setText(wep['price'])
                self.name_desc_2.setText(wep['name_desc'])
                self.desc_2.setPlainText(wep['desc'])
                self.anims.setChecked(bool(wep['anims']))
                self.item1_2.setCurrentText(self.items_rev[wep['Crafting']['item1']])
                self.item2_2.setCurrentText(self.items_rev[wep['Crafting']['item2']])
                self.item3_2.setCurrentText(self.items_rev[wep['Crafting']['item3']])
                self.item1_n_2.setText(wep['Crafting']['item1_n'])
                self.item2_n_2.setText(wep['Crafting']['item2_n'])
                self.item3_n_2.setText(wep['Crafting']['item3_n'])



    def save_as(self):
        file = self.sel_file.saveFileDialog()
        if file: json_to_file(file, self.data)


    def open_json(self):
        file = self.sel_file.openFileNameDialog()
        #file = sg.popup_get_file(message='Choose json file to load', file_types=(('Json', '*.json'),))
        if not file: return
        try:
            self.data = file_to_json(file)
        except:
            sg.popup_error(f'Error reading file: {file}')
            return
        self.Mod_content.clear()
        for elem in self.data['Weapons']:
            self.Mod_content.addItem(elem)
        for elem in self.data['Armors']:
            self.Mod_content.addItem(elem)
        self.pack_name.setText(os.path.basename(file[:-5]))
        #print(f'opening {file}')
    
    def check_mode(self):
        config = configparser.ConfigParser()
        config.read(self.config)
        #print(self.wiiu_radiobutton.isChecked())
        if self.switch_radiobutton.isChecked():
            config['DEFAULT']['mode'] = 'switch'
        elif self.wiiu_radiobutton.isChecked():
            config['DEFAULT']['mode'] = 'wiiu'
        with open(self.config, 'w') as f:
            config.write(f)

    def create_mod(self):
        #print('create_mod function')
        if os.path.exists('cache'):
            shutil.rmtree('cache')
        if not self.pack_name.text(): return
        #if not self.data.text(): return
        if not self.Lang.currentText(): return
        if not os.path.exists(self.config): return
        self.check_mode()
        Load_Input(self.data, self.pack_name.text(), self.Lang.currentText(), self.progressBar).create_pack()


    def add_weapon(self):
        #print('add_weapon function')
        #input validation
        base = self.base_2.currentText()
        if not base in self.weapons:
            print(f'Weapon {base} does not exist')
            return
        if not self.name_2.text(): return
        for elem in [self.item1_2.currentText(), self.item2_2.currentText(), self.item3_2.currentText()]:
            if not elem in self.items: return
        if self.name_2.text() in self.data['Weapons']:
            del self.data['Weapons'][self.name_2.text()]
        self.data['Weapons'][self.name_2.text()] = {
            "shop":             self.shops[self.shop.currentText()],
            "base":             self.weapons[base],
            "name":             self.name_2.text(),
            "attack":           self.attack.text(),
            "dur":              self.dur.text(),
            "islifeinfinite":   self.islifeinfinite.isChecked(),
            "sheath":           self.sheath.currentText(),
            "elink":            self.elink_2.text(),
            "slink":            self.slink_2.text(),
            "profile":          self.profile_2.currentText(),
            "magic":            self.magic.text(),
            "magicspeed":       self.magicspeed.text(),
            "magicradius":      self.magicradius.text(),
            "magicrange":       self.magicrange.text(),
            "magicpower":       self.magicpower.text(),
            "magicgravity":     self.magicgravity.text(),
            "ismagicinf":       self.ismagicinf.isChecked(),
            "subtype":          '',
            "physics":          self.physics_2.text(),
            "price":            self.price_2.text(),
            "name_desc":        self.name_desc_2.text(),
            "desc":             self.desc_2.toPlainText(),
            "anims":            bool(self.anims.isChecked()),
            "Crafting": {
                "item1": self.items[self.item1_2.currentText()],
                "item1_n": self.item1_n_2.text(),
                "item2": self.items[self.item2_2.currentText()],
                "item2_n": self.item2_n_2.text(),
                "item3": self.items[self.item3_2.currentText()],
                "item3_n": self.item3_n_2.text()
            }
        }
        if not self.Mod_content.findItems(self.name_2.text(), QtCore.Qt.MatchExactly):
            self.Mod_content.addItem(str(self.name_2.text()))

    def add_armor(self):
        #print('add_armor function')
        #Validation
        base = self.base.currentText()
        if not base in self.armors:
            print(f'Armor {base} does not exist')
            return
        if not self.name.text(): return
        for elem in [self.item1.currentText(), self.item2.currentText(), self.item3.currentText()]:
            if not elem in self.items: return
        if self.name.text() in self.data['Armors']:
            del self.data['Armors'][self.name.text()]

        self.data['Armors'][self.name.text()] = {
            "shop": self.shops[self.shop.currentText()],
            "base": self.armors[base],
            "name": self.name.text(),
            "armorNextRankName": '',
            "armorStarNum": '',
            "bfres_template": self.bfres_template.text(),
            "bfres": self.bfres.text(),
            "mainmodel": self.mainmodel.text(),
            "defence": self.defence.text(),
            "elink": self.elink.text(),
            "slink": self.slink.text(),
            "profile": self.profile.currentText(),
            "effect": self.effect.currentText(),
            "effect_lv": self.effect_lv.text(),
            "series": self.series.currentText(),
            "physics": self.physics.text(),
            "price": self.price.text(),
            "name_desc": self.name_desc.text(),
            "desc": self.desc.toPlainText(),
            "korok_mask": bool(self.korok_mask.isChecked()),
            "Crafting": {
                "item1": self.items[self.item1.currentText()],
                "item1_n": self.item1_n.text(),
                "item2": self.items[self.item2.currentText()],
                "item2_n": self.item2_n.text(),
                "item3": self.items[self.item3.currentText()],
                "item3_n": self.item3_n.text()
            }
        }
        if not self.Mod_content.findItems(self.name.text(), QtCore.Qt.MatchExactly):
            self.Mod_content.addItem(str(self.name.text()))

    def clear_list(self):
        #print('clear_list function')
        if self.data == clear_json(): return
        self.data = clear_json()
        self.Mod_content.clear()
        self.prompt_w.setWindowTitle('Message')
        self.prompt_w.buttons()
        self.prompt_w.message.setPlainText('Mod content cleared successfully')
        self.prompt_w.frame.setStyleSheet(self.frame.styleSheet())
        self.prompt_w.setPalette(self.palette())
        self.prompt_w.show()

    def remove_from_mod(self):
        try:
            x = self.Mod_content.currentItem()
        except:
            return
        if not x: return
        if x.text() in self.data['Armors']:            del self.data['Armors'][x.text()]
        elif x.text() in self.data['Weapons']:          del self.data['Weapons'][x.text()]
        row = self.Mod_content.currentRow()
        self.Mod_content.takeItem(row)

    def options(self):
        self.options_w.frame.setStyleSheet(self.frame.styleSheet())
        self.options_w.setPalette(self.palette())
        self.options_w.show()
        config = configparser.ConfigParser()
        config.read(config_file)
        self.options_w.switchpath.setText(config['DEFAULT']['switch_path'])
        self.options_w.wiiupath.setText(config['DEFAULT']['wiiu_path'])
        self.options_w.modspath.setText(config['DEFAULT']['mods_path'])
        if os.path.exists(config['DEFAULT']['switch_path']): self.options_w.switchpath.setStyleSheet(f"background-color: {valid_rgb};")
        else: self.options_w.switchpath.setStyleSheet(f"background-color: {invalid_rgb};")
        if os.path.exists(config['DEFAULT']['wiiu_path']): self.options_w.wiiupath.setStyleSheet(f"background-color: {valid_rgb};")
        else: self.options_w.wiiupath.setStyleSheet(f"background-color: {invalid_rgb};")






def main():
    app = QApplication(sys.argv)
    win = Window()
    #win.setFixedSize(win.size())
    #win.setFixedSize(win.layout.sizeHint())
    win.show()
    create_folder('jsons')
    create_folder('res')
    create_folder('cache')
    #json_to_file('res\\res.json', res)
    app.exec()


def init():
    #get_main_json()
    create_folder('jsons')
    create_folder('res')
    create_folder('cache')
    if not os.path.exists('config.ini'):
        dump = sg.popup_get_folder('Please enter a path to BOTW dump')
        if not dump: sys.exit()
        if not os.path.exists(dump):
            sg.popup_error(f'Path {dump} does not exist')
            sys.exit()
        #sg.popup('Results', 'The value returned from popup_get_folder', text)
        with open('config.ini', 'w') as f:
            f.write(f"""[DEFAULT]
path = {dump}
mods_path = MODS
lang = Bootup_EUen
mode = wiiu""")
    else:
        config = configparser.ConfigParser()
        config.read('config.ini')
        PATH = str(config['DEFAULT']['path'])
        if not os.path.exists(PATH):
            sg.popup_error(f'Path \n{PATH} \ndoes not exist. Program will now exit')
            sys.exit()

def test():
    try:
        shutil.rmtree('MODS')
    except:
        pass
    create_folder('MODS')
    #Load_Input(file_to_json('jsons\\Madara.json'), 'chuchu', 'Bootup_EUen', None).create_pack()
    shops_rev = get_res('shops_rev')
    res = file_to_json('res\\res.json')
    shops = file_to_json('res\\shops.json')
    botw_names = file_to_json('res\\botw_names.json')
    tmp = []
    for elem in shops:
        name = botw_names[elem]
        res['shops'][name] = elem
        res['shops_rev'][elem] = name

    json_to_file('res\\res1.json', res)

if __name__ == '__main__':
    #init()
    main()
    #test()