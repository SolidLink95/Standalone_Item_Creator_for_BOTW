import json
import os
import pathlib
from shutil import copytree, move

from files_manage import get_mods_path, create_folder, get_endianness
from weapon import Weapon
from BootupPack import BootupPack
from Actorinfo import Actorinfo
from AncientOven import AncientOven
from Armor import Armor

class Load_Input:
    def __init__(self, data, pack_name, lang, progressbar):
        self.progressbar = progressbar
        self.data = data
        self.pack_name = f'{get_mods_path()}\\{pack_name}'
        self.lang = lang

    def create_pack(self):
        self.create_tree()
        data = self.data
        Weapons = []
        Armors = []
        for wep in data['Weapons']:
            new = Weapon(data, wep, pack_name=self.pack_name)
            Weapons.append(new)

        for armor in data['Armors']:
            new = Armor(data, armor, pack_name=self.pack_name)
            Armors.append(new)

        step = 100 / (len(Weapons) + len(Armors) + 6)

        #print('Creating actorpacks...')
        if self.progressbar: self.progressbar.setFormat('Creating actorpacks')
        if self.progressbar: self.progressbar.setValue(step)
        for wep in Weapons:
            if self.progressbar: self.progressbar.setFormat('Creating actorpacks: ' + wep.name_desc)
            if self.progressbar: self.progressbar.setValue(self.progressbar.value() + step)
            wep.create_weapon()
        for armor in Armors:
            if self.progressbar: self.progressbar.setFormat('Creating actorpacks: ' + armor.name_desc)
            if self.progressbar: self.progressbar.setValue(self.progressbar.value() + step)
            armor.create_armor()

        if self.progressbar: self.progressbar.setFormat('Creating actorinfo entries')
        if self.progressbar: self.progressbar.setValue(self.progressbar.value() + step)
        #print('Creating actorinfo entries...')
        actorinfo = Actorinfo(Weapons, Armors, self.pack_name)
        actorinfo.do_actorinfo()
        boot = BootupPack(Weapons, Armors, self.pack_name, self.lang)
        if data['Weapons']:
            #print('Creating Save flags...')
            if self.progressbar: self.progressbar.setFormat('Creating Save flags')
            if self.progressbar: self.progressbar.setValue(self.progressbar.value() + step)
            boot.insert_hashes()
        #print('Creating descriptions...')
        if self.progressbar: self.progressbar.setFormat('Creating descriptions...')
        if self.progressbar: self.progressbar.setValue(self.progressbar.value() + step)
        boot.insert_descriptions()
        #print('Inserting oven...')
        if self.progressbar: self.progressbar.setFormat('Inserting oven...')
        if self.progressbar: self.progressbar.setValue(self.progressbar.value() + step)
        oven = AncientOven(self.pack_name, 'TwnObj_AncientOven_A_01', data)
        oven.create_oven()
        if not get_endianness():
            create_folder(f'{self.pack_name}\\01007EF00011E000')
            move(f'{self.pack_name}\\content', f'{self.pack_name}\\01007EF00011E000\\romfs')
            
        #print('Done')
        if self.progressbar: self.progressbar.setFormat(f'Mod {os.path.basename(self.pack_name)} created successfully')
        if self.progressbar: self.progressbar.setValue(100)





    def create_tree(self):
        create_folder(f'cache')
        create_folder(f'{self.pack_name}\\content\\Actor\\Pack')
        create_folder(f'{self.pack_name}\\content\\Model')
        create_folder(f'{self.pack_name}\\content\\Pack')
        create_folder(f'{self.pack_name}\\content\\UI\\StockItem')
        self.make_rules(self.pack_name.split('\\')[-1])


    def make_rules(self, name):
        s = f'[Definition]\n' \
            f'titleIds = 00050000101C9300,00050000101C9400,00050000101C9500\n' \
            f'name = {name}\n' \
            f'path = \"The Legend of Zelda: Breath of the Wild/Game Mods/{name}\"\n' \
            f'description = {name} made by banan039\'s Standalone Items Creator\nversion = 3'
        with open(f'{self.pack_name}\\rules.txt', 'w') as f:
            f.write(s)