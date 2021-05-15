import binascii
import ctypes
import sys
import zlib
import oead
from files_manage import create_folder, get_def_path, dir_to_list, get_res, get_endianness
from shutil import copyfile
import os
from oead import byml, SarcWriter, Sarc,yaz0, aamp, S32,U32

class Actorinfo:
    def __init__(self, weapons, armors, pack_name):
        self.weapons = weapons
        self.armors = armors
        self.pack_name = pack_name


    def do_actorinfo(self):
        actors = get_res('Actors')
        A = 'ActorInfo.product.sbyml'
        source = f'cache\\{A}'
        path = get_def_path() + '\\Actor'
        if not os.path.exists(source):
            copyfile(f'{path}\\{A}', source)
        with open(source, "rb") as f:
            byml = oead.yaz0.decompress(f.read())
            actorinfo = oead.byml.from_binary(byml)
        for weapon in self.weapons:
            actorinfo = weapon_iter(weapon, actorinfo, actors)
            if weapon.sheath == 'custom':
                actorinfo = sheath_iter(weapon, actorinfo)
        for armor in self.armors:
            actorinfo = armor_iter(armor, actorinfo, actors)

        with open(f'{self.pack_name}\\content\\Actor\\{A}', 'wb') as f:
            f.write(oead.yaz0.compress(oead.byml.to_binary(actorinfo, big_endian=get_endianness())))

def sheath_iter(weapon, actorinfo):
    if weapon.sheath != 'custom': return actorinfo
    base_sheath = 'Weapon_Sheath_001'
    new_sheath = f'Weapon_Sheath_' + weapon.name.split('_')[-1]
    entry = get_entry_by_name(base_sheath, actorinfo)
    entry['bfres'] = new_sheath
    entry['mainModel'] = new_sheath
    entry['name'] = new_sheath
    actorinfo = insert_new_entry(entry, actorinfo)
    return actorinfo




def armor_iter(armor, actorinfo, actors):
    armor.base = get_def_item(armor.base, actors)
    old_hash = create_hash(armor.base)
    new_hash = create_hash(armor.name)

    loc = 0
    for x in actorinfo['Hashes']:
        if int(new_hash) < int(x):
            break
        loc += 1

    old_loc = get_arr_index(actorinfo["Hashes"], old_hash)
    actorinfo["Hashes"].insert(loc, new_hash)
    # new_loc = get_arr_index(actorinfo["Hashes"], new_hash)
    new_entry = dict(actorinfo["Actors"][old_loc])
    new_entry["name"] = armor.name
    new_entry = dict(actorinfo["Actors"][old_loc])
    new_entry["name"] = armor.name

    
    if armor.elink: new_entry["elink"] = armor.elink
    
    
    if armor.slink: new_entry["slink"] = armor.slink
    if armor.armorStarNum: new_entry["armorStarNum"] = oead.S32(armor.armorStarNum)
    if armor.armorNextRankName: new_entry["armorNextRankName"] = armor.armorNextRankName
    if armor.itemUseIconActorName: new_entry["itemUseIconActorName"] = armor.itemUseIconActorName

    if armor.defence: new_entry["armorDefenceAddLevel"] = oead.S32(int(armor.defence))
    if armor.effect_lv: new_entry["armorEffectEffectLevel"] = oead.S32(int(armor.effect_lv))
    if armor.effect: new_entry["armorEffectEffectType"] = armor.effect
    elif armor.effect == 'None':
        new_entry["armorEffectEffectLevel"] = oead.S32(0)
    if armor.profile: new_entry["profile"] = armor.profile
    if armor.series: new_entry["seriesArmorSeriesType"] = armor.series

    if armor.bfres: new_entry["bfres"] = armor.bfres
    else: new_entry["bfres"] = armor.bfres_folder

    if armor.mainmodel:  new_entry["mainModel"] = armor.mainmodel
    else: new_entry["mainModel"] = armor.name

    #if "bfres" in new_entry: new_entry["bfres"] = armor.bfres_folder
    #if "mainModel" in new_entry: new_entry["mainModel"] = armor.name
    new_entry["sortKey"] = S32(int(new_entry["sortKey"]) + 1)
    #new_entry["armorNextRankName"] = ''

    if armor.item1 and armor.item1_n:
        new_entry["normal0ItemName01"] = armor.item1
        new_entry["normal0ItemNum01"] = oead.S32(int(armor.item1_n))
    else:
        new_entry["normal0ItemName01"] = 'Item_Enemy_26'
        new_entry["normal0ItemNum01"] = oead.S32(1)

    if armor.item1 and armor.item1_n and armor.item2 and armor.item2_n:
        new_entry["normal0ItemName02"] = armor.item2
        new_entry["normal0ItemNum02"] = oead.S32(int(armor.item2_n))
    else:
        new_entry["normal0ItemName02"] = 'Item_Enemy_00'
        new_entry["normal0ItemNum02"] = oead.S32(1)

    if armor.item1 and armor.item1_n and armor.item2 and armor.item2_n and armor.item3 and armor.item3_n:
        new_entry["normal0ItemName03"] = armor.item3
        new_entry["normal0ItemNum03"] = oead.S32(int(armor.item3_n))
    else:
        new_entry["normal0ItemName03"] = 'Item_Enemy_28'
        new_entry["normal0ItemNum03"] = oead.S32(1)
    new_entry["normal0StuffNum"] = oead.S32(1)
    if armor.price:
        new_entry["itemBuyingPrice"] = oead.S32(int(armor.price))
        new_entry["itemCreatingPrice"] = oead.S32(int(armor.price))

    actorinfo["Actors"].insert(loc, new_entry)
    del new_entry

    return actorinfo


def weapon_iter(weapon, actorinfo,actors):
    weapon.base = get_def_item(weapon.base, actors)
    old_hash = create_hash(weapon.base)

    new_hash = create_hash(weapon.name)

    loc = 0
    for x in actorinfo['Hashes']:
        if int(new_hash) < int(x):
            break
        loc += 1

    old_loc = get_arr_index(actorinfo["Hashes"], old_hash)
    actorinfo["Hashes"].insert(loc, new_hash)
    #new_loc = get_arr_index(actorinfo["Hashes"], new_hash)
    new_entry = dict(actorinfo["Actors"][old_loc])
    new_entry["name"] = weapon.name

    if weapon.profile == 'WeaponShield':
        if weapon.attack: new_entry["weaponCommonGuardPower"] = oead.S32(int(weapon.attack))
    else:
        if weapon.attack: new_entry["attackPower"] = oead.S32(int(weapon.attack))

    if weapon.elink: new_entry["elink"] = weapon.elink
    if weapon.slink: new_entry["slink"] = weapon.slink
    if weapon.dur: new_entry["generalLife"] = oead.S32(int(weapon.dur))
    new_entry["bfres"] = weapon.name
    new_entry["mainModel"] = weapon.name
    new_entry["sortKey"] = S32(int(new_entry["sortKey"]) + 1)

    if weapon.item1 and weapon.item1_n:
        new_entry["normal0ItemName01"] = weapon.item1
        new_entry["normal0ItemNum01"] = oead.S32(int(weapon.item1_n))
    else:
        new_entry["normal0ItemName01"] = 'Item_Enemy_26'
        new_entry["normal0ItemNum01"] = oead.S32(1)

    if weapon.item1 and weapon.item1_n and weapon.item2 and weapon.item2_n:
        new_entry["normal0ItemName02"] = weapon.item2
        new_entry["normal0ItemNum02"] = oead.S32(int(weapon.item2_n))
    else:
        new_entry["normal0ItemName02"] = 'Item_Enemy_00'
        new_entry["normal0ItemNum02"] = oead.S32(1)

    if weapon.item1 and weapon.item1_n and weapon.item2 and weapon.item2_n and weapon.item3 and weapon.item3_n:
        new_entry["normal0ItemName03"] = weapon.item3
        new_entry["normal0ItemNum03"] = oead.S32(int(weapon.item3_n))
    else:
        new_entry["normal0ItemName03"] = 'Item_Enemy_28'
        new_entry["normal0ItemNum03"] = oead.S32(1)

    new_entry["normal0StuffNum"] = oead.S32(1)
    if weapon.price:
        new_entry["itemBuyingPrice"] = oead.S32(int(weapon.price))
        new_entry["itemCreatingPrice"] = oead.S32(int(weapon.price))

    actorinfo["Actors"].insert(loc, new_entry)
    del new_entry
    return actorinfo



def get_arr_index(arr, elem):
    for i in range(len(arr)):
        if arr[i] == elem:
            return i
    sys.exit(f'Wrong base for {elem}')

def create_hash(x):
    result = zlib.crc32(bytes(x.encode()))
    if result < 2147483647:
        return oead.S32(result)
    else:
        return oead.U32(result)

def get_def_item(base, actors):
    if f'{base}.sbactorpack' in actors:
        return base
    else:
        n = (base.split("_")[-1])
        size = (-1) * len(n)
        base = base[:size] + '001'
        return base

def sort_dict(x):
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[0])}

def get_index_by_name(name, pio):
    new_hash = create_hash(name)
    for i, elem in enumerate(pio['Hashes'], 0):
        if int(new_hash) < int(pio['Hashes'][i]):
            return i
    return len(pio['Hashes']) - 1

def get_entry_by_name(name, pio):
    for i, elem in enumerate(pio['Actors'], 0):
        if elem['name'] == name:
            return dict(elem)
    sys.exit(f'Actor entry {name} does not exist')

def check_if_actor_exists(name, pio):
    for i, elem in enumerate(pio['Actors'], 0):
        if elem['name'] == name:
            return True
    return False

def insert_new_entry(entry, pio):
    if check_if_actor_exists(entry['name'], pio):
        print('Actor entry ' + entry['name'] + ' already exists, skipping')
        return pio
    new_hash = create_hash(entry['name'])
    index = get_index_by_name(entry['name'], pio)
    pio['Actors'].insert(index, entry)
    pio['Hashes'].insert(index, new_hash)
    return pio