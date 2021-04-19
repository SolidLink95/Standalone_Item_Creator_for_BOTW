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
    def __init__(self, file, pack_name, lang, progressbar):
        self.progressbar = progressbar
        self.file = file
        self.pack_name = f'{get_mods_path()}\\{pack_name}'
        self.lang = lang

    def create_pack(self):
        self.create_tree()
        data = self.file
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
        self.progressbar.setFormat('Creating actorpacks')
        self.progressbar.setValue(step)
        for wep in Weapons:
            self.progressbar.setFormat('Creating actorpacks: ' + wep.name_desc)
            self.progressbar.setValue(self.progressbar.value() + step)
            wep.create_weapon()
        for armor in Armors:
            self.progressbar.setFormat('Creating actorpacks: ' + armor.name_desc)
            self.progressbar.setValue(self.progressbar.value() + step)
            armor.create_armor()

        self.progressbar.setFormat('Creating actorinfo entries')
        self.progressbar.setValue(self.progressbar.value() + step)
        #print('Creating actorinfo entries...')
        actorinfo = Actorinfo(Weapons, Armors, self.pack_name)
        actorinfo.do_actorinfo()
        boot = BootupPack(Weapons, Armors, self.pack_name, self.lang)
        if data['Weapons']:
            #print('Creating Save flags...')
            self.progressbar.setFormat('Creating Save flags')
            self.progressbar.setValue(self.progressbar.value() + step)
            boot.insert_hashes()
        #print('Creating descriptions...')
        self.progressbar.setFormat('Creating descriptions...')
        self.progressbar.setValue(self.progressbar.value() + step)
        boot.insert_descriptions()
        #print('Inserting oven...')
        self.progressbar.setFormat('Inserting oven...')
        self.progressbar.setValue(self.progressbar.value() + step)
        oven = AncientOven(self.pack_name)
        oven.create_oven()
        if not get_endianness():
            create_folder(f'{self.pack_name}\\01007EF00011E000')
            move(f'{self.pack_name}\\content', f'{self.pack_name}\\01007EF00011E000\\romfs')
            
        #print('Done')
        self.progressbar.setFormat(f'Mod {os.path.basename(self.pack_name)} created successfully')
        self.progressbar.setValue(100)





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