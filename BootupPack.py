import binascii
import ctypes
import os
import sys
from pymsyt import Msbt
import zlib
from oead import byml, SarcWriter, Sarc,yaz0, aamp, S32
import oead
from files_manage import get_def_path, create_folder, json_to_file, get_res, get_endianness, get_file_path
from shutil import copyfile
from sarc_class import Sarc_file, set_sarc_endian
import pymsyt
from shutil import rmtree, copytree

class BootupPack:
    def __init__(self, Weapons, Armors, pack_name, lang):
        self.Weapons = Weapons
        self.Armors = Armors
        self.pack_name = pack_name
        self.lang = lang
        self.eu = self.lang.split('_')[-1]
        self.init()

    def init(self):
        #path = get_def_path() + '\\Pack'
        create_folder('cache')
        if not os.path.exists('cache\\Bootup.pack'):
            #copyfile(f'{path}\\Bootup.pack', 'cache\\Bootup.pack')
            copyfile(get_file_path(f'Pack\\Bootup.pack'), 'cache\\Bootup.pack')
        if not os.path.exists(f'cache\\{self.lang}.pack'):
            #copyfile(f'{path}\\{self.lang}.pack', f'cache\\{self.lang}.pack')
            copyfile(get_file_path(f'Pack\\{self.lang}.pack'), f'cache\\{self.lang}.pack')


    def insert_hashes(self):
        if not self.Weapons: return
        source = 'cache\\Bootup.pack'
        output = f'{self.pack_name}\\content\\Pack\\Bootup.pack'
        with open(source + '', 'rb') as f:
            writer = SarcWriter.from_sarc(Sarc(f.read()))
            set_sarc_endian(writer)
        gamedata = SarcWriter.from_sarc(Sarc(yaz0.decompress(writer.files['GameData/gamedata.ssarc'])))
        # print_sarc_cont(gamedata)
        flags = byml.from_binary(gamedata.files['/bool_data_0.bgdata'])

        for wep in self.Weapons:
            flags = iteration(flags, wep)
        gamedata.files['/bool_data_0.bgdata'] =\
            byml.to_binary(flags, big_endian=get_endianness())
        writer.files['GameData/gamedata.ssarc'] =\
            yaz0.compress(gamedata.write()[1])

        with open(output, 'wb') as f:
            f.write(writer.write()[1])

    def insert_descriptions(self):
        profiles = ['WeaponSmallSword', 'WeaponLargeSword', 'WeaponSpear', 'WeaponShield', 'WeaponBow', 'ArmorHead', 'ArmorUpper', 'ArmorLower']

        source = f'cache\\{self.lang}.pack'
        with open(source, 'rb') as f:
            data_sarc = oead.Sarc(f.read())
            writer = oead.SarcWriter.from_sarc(data_sarc)
            set_sarc_endian(writer)

        product_data_sarc =  Sarc(yaz0.decompress((writer.files[f'Message/Msg_{self.eu}.product.ssarc'])))
        product_writer = oead.SarcWriter.from_sarc(product_data_sarc)
        set_sarc_endian(product_writer)

        descs_json = descs_to_json(self.Weapons, self.Armors, profiles)

        for profile in descs_json:
            msbt_path = f'ActorType/{profile}.msbt'
            data = product_data_sarc.get_file(msbt_path).data.tobytes()
            msbt_raw = Msbt.from_binary(data)
            msbt_dict = msbt_raw.to_dict()
            for item in descs_json[profile]:
                desc = descs_json[profile][item]['desc']
                name_desc = descs_json[profile][item]['name_desc']
                msbt_dict["entries"][f"{item}_Desc"] = {"contents": [{"text": desc}]}
                msbt_dict["entries"][f"{item}_Name"] = {"contents": [{"text": name_desc}]}
                msbt_dict["entries"][f"{item}_PictureBook"] = {"contents": [{"text": desc}]}
            to_write = Msbt.from_dict(msbt_dict).to_binary(big_endian=get_endianness())
            product_writer.files[msbt_path] = to_write


        writer.files[f'Message/Msg_{self.eu}.product.ssarc'] = yaz0.compress(product_writer.write()[1])
        with open(f'{self.pack_name}\\content\\Pack\\{self.lang}.pack', 'wb') as f:
            f.write(writer.write()[1])




def descs_to_json(Weapons, Armors, profiles):
    res = {}
    for wep in Weapons:
        if not wep.profile in profiles:
            wep.profile = get_profile_from_name(wep.name)
        name = (wep.name)
        name_desc = (wep.name_desc)
        desc = (wep.desc)
        if not name_desc:
            name_desc = name
        if not desc:
            desc = f'This is {name_desc}'
        if not wep.profile in res:
            res[wep.profile] = {}
        res[wep.profile][name] = {
            "name_desc" : name_desc,
            "desc" : desc
        }

    for armor in Armors:
        if not armor.profile in profiles:
            armor.profile = get_profile_from_name(armor.name)
        name = (armor.name)
        name_desc = (armor.name_desc)
        desc = (armor.desc)
        if not name_desc:
            name_desc = name
        if not desc:
            desc = f'This is {name_desc}'
        if not armor.profile in res:
            res[armor.profile] = {}
        res[armor.profile][name] = {
            "name_desc" : name_desc,
            "desc" : desc
        }

    return res



def iteration(flags, wep):
    ind = get_entry(flags['bool_data'], wep.base)
    new_entry = dict(flags['bool_data'][ind])

    new_entry['DataName'] = f'IsGet_{wep.name}'
    new_entry['HashValue'] = S32(create_hash(f'IsGet_{wep.name}'))

    flags['bool_data'].append(new_entry)
    del new_entry
    return flags

def print_msbt(msbt):
    for ent in msbt['entries']:
        try:
            print(ent)
            print(msbt['entries'][ent]['contents'][0]['text'])
        except:
            pass

def get_base_msyt(name):
    pref = name.split('_')[-1]
    base = name[:(len(name)-len(pref))]
    base += '001'
    return base

def get_profile_from_name(s):
    profiles = get_res('profiles')
    if 'Lsword' in s:       return 'WeaponLargeSword'
    if 'Sword' in s:        return 'WeaponSmallSword'
    if 'Bow' in s:          return 'WeaponBow'
    if 'Spear' in s:        return 'WeaponSpear'
    if 'Shield' in s:        return 'WeaponShield'
    if 'Head' in s:   return 'ArmorHead'
    if 'Lower' in s:  return 'ArmorLower'
    if 'Upper' in s:  return 'ArmorUpper'
    return ''


def create_hash(x):
    return ctypes.c_int32(binascii.crc32(bytes(x, 'utf-8'))).value



def print_byml(byml):
    for elem in byml:
        print(dict(elem))

def get_entry(byml, name):
    for i in range(len(byml)):
        if dict(byml[i])['DataName'] == f'IsGet_{name}':
            return i
    return None

def print_sarc_cont(writer):
    for elem in writer.files:
    #for elem in self.data.data_sarc.get_files():
        print(elem)

def get_raw_data(data_sarc, file):
    data = data_sarc.get_file(file).data.tobytes()
    pio = aamp.ParameterIO.from_binary(data)
    return pio