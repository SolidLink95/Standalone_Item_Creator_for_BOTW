import configparser
import datetime
import json
import os
import pathlib
import sys
import urllib.request
from os import listdir
from os.path import isfile, join


def create_folder(dir):
    pathlib.Path(dir).mkdir(parents=True, exist_ok=True)


def dir_to_list(mypath):
    return [f for f in listdir(mypath) if isfile(join(mypath, f))]


def calc_profile(s):
    profiles = get_res('profiles')
    data = {
        "Lsword": "WeaponLargeSword",
        "Sword": "WeaponSmallSword",
        "Bow": "WeaponBow",
        "Spear": "WeaponSpear",
        "Shield": "WeaponShield",
        "Head": "ArmorHead",
        "Lower": "ArmorLower",
        "Upper": "ArmorUpper"
    }
    if s in profiles:
        return s
    for key, item in data.items():
        if key in s:
            return item
    return ''


def file_to_str(file):
    if os.path.exists(file):
        with open(file, 'r', errors='ignore') as f:
            return f.read()
    else:
        print('File does not exist: ' + file)


def file_to_dict(file):
    with open(file, encoding="utf8") as json_file:
        return json.load(json_file)


def get_langs():
    langs = ['Bootup_EUde', 'Bootup_EUen', 'Bootup_EUes', 'Bootup_EUfr', 'Bootup_EUit', 'Bootup_EUnl', 'Bootup_EUru',
             'Bootup_USen']
    config = configparser.ConfigParser()
    config.read('config.ini')
    if str(config['DEFAULT']['lang']) in langs:
        langs.remove(config['DEFAULT']['lang'])
        langs.insert(0, config['DEFAULT']['lang'])
    return langs


def get_def_path():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        if get_endianness():
            return str(config['DEFAULT']['wiiu_path'])
        else:
            return str(config['DEFAULT']['switch_path'])
    except:
        return ''


def get_file_path(file):
    config = configparser.ConfigParser()
    config.read('config.ini')
    if get_endianness():
        the_path = str(config['DEFAULT']['wiiu_update'])
        if os.path.exists(os.path.join(the_path, file)):
            the_path = os.path.join(str(config['DEFAULT']['wiiu_update']), file)
        else:
            the_path = os.path.join(str(config['DEFAULT']['wiiu_path']), file)
        print(the_path)
        return the_path
    else:
        return os.path.join(str(config['DEFAULT']['switch_path']), file)


def get_def_lang(config_file='config.ini'):
    try:
        config = configparser.ConfigParser()
        config.read(config_file)
        langs = get_langs()
        if str(config['DEFAULT']['lang']) in langs:
            return str(config['DEFAULT']['lang'])
        else:
            return langs[0]
    except:
        return ''


def get_endianness(config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)
    if config['DEFAULT']['mode'] == 'wiiu':
        return True
    elif config['DEFAULT']['mode'] == 'switch':
        return False


def get_mods_path():
    config = configparser.ConfigParser()
    config.read('config.ini')
    pathlib.Path(str(config['DEFAULT']['mods_path'])).mkdir(parents=True, exist_ok=True)
    return str(config['DEFAULT']['mods_path'])


def json_to_file(file, JSON):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(JSON, f, indent=4, sort_keys=True)


def get_main_json():
    file = 'res\\botw_names.json'
    url = 'https://raw.githubusercontent.com/MrCheeze/botw-tools/master/botw_names.json'
    if not os.path.exists(file):
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/79.0')]
        urllib.request.install_opener(opener)
        with urllib.request.urlopen(url) as fin, open(
                file, 'w', encoding='utf-8') as fout:
            for line in fin:
                fout.write((line.decode('utf-8')))
    with open(file) as f:
        return json.load(f)


def clear_json():
    return {
        "Weapons": {},
        "Armors": {},
    }


def remove_dups(mylist):
    return list(set(mylist))


def get_res(att):
    if att == 'Actors':
        res = file_to_dict('res\\Actors.json')
    else:
        res = file_to_dict('res\\res.json')
    return res[att]
