import os
import sys
from shutil import copyfile
import oead
from files_manage import get_def_path, dir_to_list, get_endianness
from sarc_class import Sarc_file
from Actorinfo import create_hash, get_arr_index

class AncientOven:
    def __init__(self, pack_name):
        self.name = 'TwnObj_AncientOven_A_01'
        self.bshop = 'TwnObj_AncientOven_A_01'
        self.pack_name = pack_name
        self.data = Sarc_file(self.init_oven())


    def init_oven(self):
        O = 'TwnObj_AncientOven_A_01'
        path = f'{get_def_path()}\\Actor\\Pack\\{O}.sbactorpack'
        if not os.path.exists(f'cache\\{O}.sbactorpack'):
            copyfile(path, f'cache\\{O}.sbactorpack')
        return f'cache\\{O}.sbactorpack'

    def do_actorlink(self):
        old_name = f'Actor/ActorLink/TwnObj_AncientOven_A_01.bxml'
        new_name = f'Actor/ActorLink/{self.name}.bxml'
        pio = get_raw_data(self.data.data_sarc, old_name)

        pio.objects['LinkTarget'].params['ActorNameJpn'] = 'asdf'
        pio.objects['LinkTarget'].params['ShopDataUser'] = self.bshop

        update_sarc(pio, self.data, old_name, new_name)

    def do_shopdata(self):
        old_name = f'Actor/ShopData/TwnObj_AncientOven_A_01.bshop'
        new_name = f'Actor/ShopData/{self.bshop}.bshop'
        pio = get_raw_data(self.data.data_sarc, old_name)

        actors = dir_to_list(f'{self.pack_name}\\content\\Actor\\Pack')
        #iter = int(pio.objects['Ancient'].params['ColumnNum'].v) + 2
        iter = int(pio.objects['Ancient'].params['ColumnNum'].v) 
        size = len(actors)
        #for elem in pio.objects['Ancient'].params:
        #    if not 'ColumnNum' in elem:
        #        del pio.objects['Ancient'].params[elem]
        pio.objects['Ancient'].params['ColumnNum'] = size + iter


        for actor in actors:
            iter += 1
            name = actor.split('.')[0]
            n = int_to_3digits(iter)
            pio.objects['Ancient'].params[f'ItemSort{n}'] = iter
            pio.objects['Ancient'].params[f'ItemName{n}'] = oead.FixedSafeString64(name)
            pio.objects['Ancient'].params[f'ItemNum{n}'] = 0
            pio.objects['Ancient'].params[f'ItemAdjustPrice{n}'] = 0
            pio.objects['Ancient'].params[f'ItemLookGetFlg{n}'] = False
            pio.objects['Ancient'].params[f'ItemAmount{n}'] = 0

        update_sarc(pio, self.data, old_name, new_name)

    def create_oven(self):
        self.do_actorlink()
        self.do_shopdata()
        #self.do_actorinfo()

        actorpack = f'{self.pack_name}\\content\\Actor\\Pack\\{self.name}.sbactorpack'
        with open(actorpack, 'wb') as f:
            f.write(oead.yaz0.compress(self.data.data_writer.write()[1]))




def int_to_3digits(n):
    res = str(n)
    while len(res) != 3:
        res = '0' + res
    return res








def get_raw_data(data_sarc, file):
    data = data_sarc.get_file(file).data.tobytes()
    pio = oead.aamp.ParameterIO.from_binary(data)
    return pio

def update_sarc(pio, data, old_name, new_name):
    del data.data_writer.files[old_name]
    data.data_writer.files[new_name] = oead.aamp.ParameterIO.to_binary(pio)