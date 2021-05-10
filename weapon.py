import binascii
import ctypes
import json
import os
import sys
from Sheaths import Sheath
import zlib
from sarc_class import Sarc_file
import oead
from oead import FixedSafeString32, FixedSafeString64
from bfres_dup import Bfres_Dup, duplicate_bfres
from files_manage import get_def_path, create_folder
from shutil import copyfile

class Weapon:
    def __init__(self, data, wep, pack_name):
        self.name = data['Weapons'][wep]['name']
        self.attack = data['Weapons'][wep]['attack']
        self.dur = data['Weapons'][wep]['dur']
        self.islifeinfinite = data['Weapons'][wep]['islifeinfinite']
        self.base = data['Weapons'][wep]['base']
        self.sheath = data['Weapons'][wep]['sheath']
        self.elink = data['Weapons'][wep]['elink']
        self.slink = data['Weapons'][wep]['slink']
        self.profile = data['Weapons'][wep]['profile']
        self.magicpower = data['Weapons'][wep]['magicpower']
        self.magic = data['Weapons'][wep]['magic']
        self.magicradius = data['Weapons'][wep]['magicradius']
        self.magicrange = data['Weapons'][wep]['magicrange']
        self.magicspeed = data['Weapons'][wep]['magicspeed']
        self.magicgravity = data['Weapons'][wep]['magicgravity']
        self.ismagicinf = data['Weapons'][wep]['ismagicinf']
        self.subtype = data['Weapons'][wep]['subtype']
        self.price = data['Weapons'][wep]['price']
        self.name_desc = data['Weapons'][wep]['name_desc']
        self.desc = data['Weapons'][wep]['desc']
        self.item1 = data['Weapons'][wep]['Crafting']['item1']
        self.item1_n = data['Weapons'][wep]['Crafting']['item1_n']
        self.item2 = data['Weapons'][wep]['Crafting']['item2']
        self.item2_n = data['Weapons'][wep]['Crafting']['item2_n']
        self.item3 = data['Weapons'][wep]['Crafting']['item3']
        self.item3_n = data['Weapons'][wep]['Crafting']['item3_n']
        self.data = self.get_actorpack_data()
        self.pack_name = pack_name
        self.physics = ''
        self.anims = False
        if 'physics' in data['Weapons'][wep]:
            self.physics = data['Weapons'][wep]['physics']
        if 'anims' in data['Weapons'][wep]:
            self.anims = bool(data['Weapons'][wep]['anims'])


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
        if self.elink:      pio.objects['LinkTarget'].params['ElinkUser'] = self.elink
        if self.slink:      pio.objects['LinkTarget'].params['SlinkUser'] = self.slink
        if self.profile:    pio.objects['LinkTarget'].params['ProfileUser'] = self.profile
        pio.objects['LinkTarget'].params['GParamUser'] = self.name
        pio.objects['LinkTarget'].params['ModelUser'] = self.name
        pio.objects['LinkTarget'].params['RecipeUser'] = self.name
        OldPhysicsUser = str(pio.objects['LinkTarget'].params['PhysicsUser'])
        PhysicsUser = self.do_physics(OldPhysicsUser)
        if PhysicsUser:
            pio.objects['LinkTarget'].params['PhysicsUser'] = PhysicsUser
        
        if self.anims and 'Weapon' in self.name:
            print(f'Adding boko arm anims to {self.name}...')
            new_AI, new_name_baslist = self.do_anims()
            pio.objects['LinkTarget'].params['AIProgramUser'] = new_AI
            pio.objects['LinkTarget'].params['ASUser'] = new_name_baslist
        
        update_sarc(pio, self.data, old_name, new_name)

    def do_physics(self, OldPhysicsUser):
        if not self.physics: return ''
        file = f'{get_def_path()}\\Actor\\Pack\\{self.physics}.sbactorpack'
        if os.path.exists(file):
            data = Sarc_file(file)
        else:
            print(f'Cant find base actor {file}')
            return ''

        #Removing old physics files from actorpack
        to_rem = []
        for file in self.data.data_writer.files:
            if 'Physics/' in file and not '.bphysics' in file:
                to_rem.append(file)
        for file in to_rem:
            del self.data.data_writer.files[file]

        PhysicsUser = ''
        for file in data.data_writer.files:
            if '.bphysics' in file and 'Actor/Physics/' in file:
                PhysicsUser = os.path.basename(file).split('.')[0]
                pio = get_raw_data(data.data_sarc, file)
                old_name = f'Actor/Physics/{OldPhysicsUser}.bphysics'
                new_name = f'Actor/Physics/{PhysicsUser}.bphysics'
                update_sarc(pio, self.data, old_name, new_name)
            elif 'Physics/' in file and not '.bphysics' in file:
                self.data.data_writer.files[file] = data.data_sarc.get_file(file).data.tobytes()
        return PhysicsUser



    def do_gparam(self):
        old_name = f'Actor/GeneralParamList/{self.base}.bgparamlist'
        new_name = f'Actor/GeneralParamList/{self.name}.bgparamlist'
        pio = get_raw_data(self.data.data_sarc, old_name)

        if self.profile == 'WeaponShield':
            if self.attack: pio.objects['WeaponCommon'].params["GuardPower"] = int(self.attack)
        else:
            if self.attack: pio.objects['Attack'].params["Power"] = int(self.attack)


        if self.dur: pio.objects['General'].params["Life"] = int(self.dur)
        try:
            if self.magic:          pio.objects['Rod'].params["MagicName"] = oead.aamp.Parameter(FixedSafeString32(self.magic))
            if self.magicgravity:   pio.objects['Rod'].params["MagicGravity"] = float(self.magicgravity)#0.01
            if self.magicradius:    pio.objects['Rod'].params["MagicRadius"] = float(self.magicradius)
            if self.magicrange:     pio.objects['Rod'].params["MagicRange"] = float(self.magicrange)
            if self.magicspeed:     pio.objects['Rod'].params["MagicSpeed"] = float(self.magicspeed)
            if self.magicpower:     pio.objects['Rod'].params["MagicPower"] = int(self.magicpower)
            if self.ismagicinf:
                pio.objects['WeaponCommon'].params["ChemicalEnergyAmountUsed"] = 1
                pio.objects['WeaponCommon'].params["ChemicalEnergyRecoverRate"] = 400.0
        except:
            pass
        if self.price:          pio.objects['Item'].params["BuyingPrice"] = int(self.price)
        if self.islifeinfinite: pio.objects['General'].params["IsLifeInfinite"] = self.islifeinfinite
        if self.subtype and self.profile != 'WeaponShield':
            pio.objects[self.profile.replace('Weapon', '')].params["WeaponSubType"] = oead.aamp.Parameter(FixedSafeString32(self.subtype))

        if self.profile != 'WeaponShield' and self.profile and not 'shield' in self.name.lower():
            if self.sheath == 'custom':
                sheath = 'Weapon_Sheath_' + self.name.split('_')[-1]
            elif self.sheath == 'none':
                sheath = ''
            else:
                sheath = self.sheath
            #print('Sheath ' + sheath)
            pio.objects[self.profile.replace('Weapon', '')].params["PodName"] = oead.aamp.Parameter(oead.FixedSafeString32(sheath))


        #print_aamp(pio)
        update_sarc(pio, self.data, old_name, new_name)

    def do_model(self):
        old_name = f'Actor/ModelList/{self.base}.bmodellist'
        new_name = f'Actor/ModelList/{self.name}.bmodellist'
        pio = get_raw_data(self.data.data_sarc, old_name)

        pio.lists['ModelData'].lists['ModelData_0'].objects['Base'].params['Folder'] \
            = FixedSafeString64(self.name)
        try:
            pio.lists['ModelData'].lists['ModelData_0'].lists['Unit'].objects['Unit_0'].params['UnitName'] \
            = FixedSafeString64(self.name)
        except:
            pass

        #print_aamp(pio)
        update_sarc(pio, self.data, old_name, new_name)

    def get_recipe(self):
        template = 'Weapon_Shield_038'
        recipe = f'{self.name}.brecipe'
        if not os.path.exists(f'cache\\{template}.sbactorpack'):
            copyfile(f'{get_def_path()}\\Actor\\Pack\\{template}.sbactorpack', f'cache\\{template}.sbactorpack')
        path = f'cache\\{template}.sbactorpack'
        data = Sarc_file(path)
        pio = get_raw_data(data.data_sarc, f'Actor/Recipe/{template}.brecipe')

        if self.item1 and self.item1_n:
            pio.objects['Normal0'].params['ItemName01'] = oead.FixedSafeString64(self.item1)
            pio.objects['Normal0'].params['ItemNum01'] = int(self.item1_n)
        if self.item1 and self.item1_n and self.item2 and self.item2_n:
            pio.objects['Normal0'].params['ItemName02'] = oead.FixedSafeString64(self.item2)
            pio.objects['Normal0'].params['ItemNum02'] = int(self.item2_n)
        else:
            pio.objects['Normal0'].params['ItemNum02'] = 1
        if self.item1 and self.item1_n and self.item2 and self.item2_n and self.item3 and self.item3_n:
            pio.objects['Normal0'].params['ItemName03'] = oead.FixedSafeString64(self.item3)
            pio.objects['Normal0'].params['ItemNum03'] = int(self.item3_n)
        else:
            pio.objects['Normal0'].params['ItemName03'] = oead.FixedSafeString64('Item_Enemy_00')

        self.data.data_writer.files[f'Actor/Recipe/{recipe}'] = oead.aamp.ParameterIO.to_binary(pio)

    def do_sheath(self):
        if not 'Weapon' in self.profile: return
        if 'Shield' in self.profile: return
        
        if self.sheath == 'custom':
            print(f'Creating custom sheath for {self.name}')
            sheath = Sheath('Weapon_Sheath_001', self.name, self.pack_name)
            sheath.create_sheath()
    
    def do_anims(self):
        if 'Weapon_Lsword_' in self.name:
            template = 'Weapon_Lsword_019'
        else:
            template = 'Weapon_Sword_019'
        
        path = f'cache\\{template}.sbactorpack'
        if not os.path.exists(path):
            copyfile(f'{get_def_path()}\\Actor\\Pack\\{template}.sbactorpack', path)
        
        data = Sarc_file(path)
        for file in self.data.data_writer.files:
            if '.baiprog' in file or '.baslist' in file or '.bas' in file:
                del self.data.data_writer.files[file]
        
        for file in data.data_writer.files:
            if '.baiprog' in file:
                new_AI = get_internal_name('.baiprog', data)
                pio = get_raw_data(data.data_sarc, new_AI)
                self.data.data_writer.files[new_AI] = oead.aamp.ParameterIO.to_binary(pio)
            elif '.baslist' in file:
                new_name_baslist = file.replace(template,self.name)
                pio = get_raw_data(data.data_sarc, file)
                raw_text = pio.to_text()
                raw_text = raw_text.replace(template, self.name)
                pio = oead.aamp.ParameterIO.from_text(raw_text)
                self.data.data_writer.files[new_name_baslist] = oead.aamp.ParameterIO.to_binary(pio)
            elif '.bas' in file:
                new_name = file.replace(template, self.name)
                pio = get_raw_data(data.data_sarc, file)
                self.data.data_writer.files[new_name] = oead.aamp.ParameterIO.to_binary(pio)
        duplicate_bfres(f'{get_def_path()}\\Model\\{template}_Animation.sbfres', f'{self.pack_name}\\content\\Model\\{self.name}_Animation.sbfres', template, self.name)
        return os.path.basename(new_AI).split('.')[0], os.path.basename(new_name_baslist).split('.')[0]

    def create_weapon(self):
        self.do_actorlink()
        self.get_recipe()
        self.do_gparam()
        self.do_model()
        self.do_sheath()
        Bfres_Dup(self.base, self.name, self.profile, self.pack_name).duplicate()
        actorpack = f'{self.pack_name}\\content\\Actor\\Pack\\{self.name}.sbactorpack'
        if not os.path.exists(actorpack):
            with open(actorpack, 'wb') as f:
                f.write(oead.yaz0.compress(self.data.data_writer.write()[1]))






    def print_sarc_cont(self):
        for elem in self.data.data_writer.files:
        #for elem in self.data.data_sarc.get_files():
            print(elem)

def get_internal_name(name, data):
    for file in data.data_writer.files:
        if name in file:
            return file
    return ''

def print_aamp(amp):
    try:
        print((amp.to_text()))
    except:
        pass



def update_sarc(pio, data, old_name, new_name, del_old=True):
    data.data_writer.files[new_name] = oead.aamp.ParameterIO.to_binary(pio)
    if del_old:
        del data.data_writer.files[old_name]


def get_raw_data(data_sarc, file):
    data = data_sarc.get_file(file).data.tobytes()
    pio = oead.aamp.ParameterIO.from_binary(data)
    return pio

def dict_to_binary(the_dict):
    str = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)
    return binary

def get_arr_index(arr, elem):
    for i in range(len(arr)):
        if arr[i] == elem:
            return i
    return 0

def create_hash(x):
    return ctypes.c_int32(binascii.crc32(bytes(x, 'utf-8'))).value

def changeParam(attr, param, res):
    try:
        if attr: param = res
    except:
        pass
    return param