import binascii
import ctypes
import json
import os
import sys
import pathlib
import zlib
from sarc_class import Sarc_file
import oead
from oead import FixedSafeString32, FixedSafeString64
from bfres_dup import Bfres_Dup
from files_manage import get_def_path, create_folder, get_endianness
from shutil import copyfile

class Sheath:
    def __init__(self, base, name, pack_name):
        self.name = 'Weapon_Sheath_' + name.split('_')[-1]
        self.pack_name = pack_name
        self.base = 'Weapon_Sheath_001'
        self.data = self.get_actorpack_data()


    def get_actorpack_data(self):
        file = f'{get_def_path()}\\Actor\\Pack\\{self.base}.sbactorpack'
        if os.path.exists(file):
            return Sarc_file(file)
        else:
            print(f'Cant find base actor {file}')
            sys.exit()


    def do_actorlink(self):
        old_name = f'Actor/ActorLink/{self.base}.bxml'
        new_name = f'Actor/ActorLink/{self.name}.bxml'
        pio = get_raw_data(self.data.data_sarc, old_name)

        pio.objects['LinkTarget'].params['ActorNameJpn'] = 'asdf'
        pio.objects['LinkTarget'].params['ModelUser'] = self.name

        update_sarc(pio, self.data, old_name, new_name)

    def do_model(self):
        old_name = f'Actor/ModelList/{self.base}.bmodellist'
        new_name = f'Actor/ModelList/{self.name}.bmodellist'
        pio = get_raw_data(self.data.data_sarc, old_name)

        pio.lists['ModelData'].lists['ModelData_0'].objects['Base'].params['Folder'] \
            = FixedSafeString64(self.name)
        pio.lists['ModelData'].lists['ModelData_0'].lists['Unit'].objects['Unit_0'].params['UnitName'] \
            = FixedSafeString64(self.name)

        #print_aamp(pio)
        update_sarc(pio, self.data, old_name, new_name)

    def do_bfres(self):
        path = f'{get_def_path()}\\Model\\'
        if get_endianness():
            files = [f'{path}{self.base}.sbfres', f'{path}{self.base}.Tex1.sbfres', f'{path}{self.base}.Tex2.sbfres']
        else:
            files = [f'{path}{self.base}.sbfres', f'{path}{self.base}.Tex.sbfres']
        for file in files:
            if not os.path.exists(file): return
        for file in files:
            output = self.pack_name + '\\content\\Model\\' + file.split('\\')[-1].replace(self.base, self.name)
            if not os.path.exists(output):
                with open(file, "rb") as f:
                    content = oead.yaz0.decompress(f.read())
                to_write = content.replace(self.base.replace('Weapon_','').encode(), self.name.replace('Weapon_','').encode())
                to_write = oead.yaz0.compress(to_write)
                with open(output, "wb") as f:
                    f.write(to_write)

    def create_sheath(self):
        self.do_actorlink()
        self.do_model()
        self.do_bfres()

        actorpack = f'{self.pack_name}\\content\\Actor\\Pack\\{self.name}.sbactorpack'
        if not os.path.exists(actorpack):
            with open(actorpack, 'wb') as f:
                f.write(oead.yaz0.compress(self.data.data_writer.write()[1]))

def update_sarc(pio, data, old_name, new_name):
    data.data_writer.files[new_name] = oead.aamp.ParameterIO.to_binary(pio)
    del data.data_writer.files[old_name]

def get_raw_data(data_sarc, file):
    data = data_sarc.get_file(file).data.tobytes()
    pio = oead.aamp.ParameterIO.from_binary(data)
    return pio