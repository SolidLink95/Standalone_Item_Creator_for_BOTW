import os
import sys
import oead, copy

from bfres_dup import Bfres_Dup, duplicate_bfres
from files_manage import get_def_path, get_res
from sarc_class import Sarc_file
from shutil import copyfile

class Armor:
    def __init__(self, data, armor, pack_name):
        self.bfres = ''
        self.mainmodel = ''
        self.bfres_template = ''

        self.base = str(data['Armors'][armor]['base'])
        self.name = str(data['Armors'][armor]['name'])
        self.defence = str(data['Armors'][armor]['defence'])
        self.elink = str(data['Armors'][armor]['elink'])
        self.effect = str(data['Armors'][armor]['effect'])
        if str(data['Armors'][armor]['effect_lv']) == '': self.effect_lv = 0
        else: self.effect_lv = str(data['Armors'][armor]['effect_lv'])
        self.slink = str(data['Armors'][armor]['slink'])
        self.profile = str(data['Armors'][armor]['profile'])
        self.series = str(data['Armors'][armor]['series'])
        self.price = str(data['Armors'][armor]['price'])
        if 'bfres' in data['Armors'][armor]: self.bfres = str(data['Armors'][armor]['bfres'])
        if 'mainmodel' in data['Armors'][armor]: self.mainmodel = str(data['Armors'][armor]['mainmodel'])
        if 'bfres_template' in data['Armors'][armor]: self.bfres_template = str(data['Armors'][armor]['bfres_template'])
        self.name_desc = str(data['Armors'][armor]['name_desc'])
        self.desc = str(data['Armors'][armor]['desc'])
        self.item1 = data['Armors'][armor]['Crafting']['item1']
        self.item1_n = data['Armors'][armor]['Crafting']['item1_n']
        self.item2 = data['Armors'][armor]['Crafting']['item2']
        self.item2_n = data['Armors'][armor]['Crafting']['item2_n']
        self.item3 = data['Armors'][armor]['Crafting']['item3']
        self.item3_n = data['Armors'][armor]['Crafting']['item3_n']
        self.data = self.get_actorpack_data()
        self.bfres_folder = self.get_model_folder()
        self.pack_name = pack_name
        self.physics = ''
        self.korok_mask = False
        if 'physics' in data['Armors'][armor]:
            self.physics = data['Armors'][armor]['physics']
        if 'korok_mask' in data['Armors'][armor]:
            self.korok_mask = bool(data['Armors'][armor]['korok_mask'])

    def get_actorpack_data(self):
        file = get_def_path() + '\\Actor\\Pack\\' + self.base + '.sbactorpack'
        if os.path.exists(file):
            return Sarc_file(file)
        else:
            print(f'Cant find base actor {file}')
            sys.exit()


    def do_actorlink(self):
        old_name = f'Actor/ActorLink/{self.base}.bxml'
        new_name = f'Actor/ActorLink/{self.name}.bxml'
        pio = get_raw_data(self.data.data_sarc, old_name)
        PhysicsUser = None

        pio.objects['LinkTarget'].params['ActorNameJpn'] = 'asdf'
        if self.elink: pio.objects['LinkTarget'].params['ElinkUser'] = self.elink
        if self.slink: pio.objects['LinkTarget'].params['SlinkUser'] = self.slink
        if self.profile: pio.objects['LinkTarget'].params['ProfileUser'] = self.profile
        pio.objects['LinkTarget'].params['GParamUser'] = self.name
        pio.objects['LinkTarget'].params['ModelUser'] = self.name
        pio.objects['LinkTarget'].params['RecipeUser'] = self.name
        if self.korok_mask and 'Head' in self.name:
            #if self.base != 'Armor_176_Head':
            print(f'Adding korok anims to {self.name}...')
            self.do_korok_mask()
            pio.objects['LinkTarget'].params['AIProgramUser'] = 'Armor_Korok_Head'
            pio.objects['LinkTarget'].params['ASUser'] = self.name

        OldPhysicsUser = str(pio.objects['LinkTarget'].params['PhysicsUser'])
        if self.physics != self.base: PhysicsUser = self.do_physics(OldPhysicsUser)
        if PhysicsUser: pio.objects['LinkTarget'].params['PhysicsUser'] = PhysicsUser

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
        eff_lv = int(self.effect_lv)
        if eff_lv > 3: eff_lv = 3
        old_name = self.get_name_from_sarc('bgparamlist')
        new_name = f'Actor/GeneralParamList/{self.name}.bgparamlist'
        pio = get_raw_data(self.data.data_sarc, old_name)

        if self.price: pio.objects['Item'].params["BuyingPrice"] = int(self.price)
        if self.defence: pio.objects['Armor'].params["DefenceAddLevel"] = int(self.defence)
        if self.series: pio.objects['SeriesArmor'].params["SeriesType"] = oead.FixedSafeString32(self.price)

        if self.effect:
            if self.effect == 'None':pio.objects['ArmorEffect'].params["EffectType"] = oead.FixedSafeString32('')
            else: pio.objects['ArmorEffect'].params["EffectType"] = oead.FixedSafeString32(self.effect)

        if self.effect_lv: pio.objects['ArmorEffect'].params["EffectLevel"] = eff_lv
        pio.objects['Armor'].params["NextRankName"] = oead.FixedSafeString64('')

        update_sarc(pio, self.data, old_name, new_name)

    def do_model(self):
        old_name = self.get_name_from_sarc('bmodellist')
        new_name = f'Actor/ModelList/{self.name}.bmodellist'
        pio = get_raw_data(self.data.data_sarc, old_name)
        if self.bfres: bfres = self.bfres
        else: bfres = self.bfres_folder
        if self.mainmodel: mainmodel = self.mainmodel
        else: mainmodel = self.name

        pio.lists['ModelData'].lists['ModelData_0'].objects['Base'].params['Folder'] \
            = oead.FixedSafeString64(bfres)
        pio.lists['ModelData'].lists['ModelData_0'].lists['Unit'].objects['Unit_0'].params['UnitName'] \
            = oead.FixedSafeString64(mainmodel)

        update_sarc(pio, self.data, old_name, new_name)

    def get_recipe(self):
        template = 'Weapon_Shield_038'
        recipe = f'{self.name}.brecipe'
        path = f'cache\\{template}.sbactorpack'
        if not os.path.exists(path):
            copyfile(f'{get_def_path()}\\Actor\\Pack\\{template}.sbactorpack', path)
        
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
    
    def do_korok_mask(self):
        if not 'Head' in self.name: return
        template = 'Armor_176_Head'
        path = f'cache\\{template}.sbactorpack'
        if not os.path.exists(path):
            copyfile(f'{get_def_path()}\\Actor\\Pack\\{template}.sbactorpack', path)
            
        data = Sarc_file(path)
        if 'Actor/AS/Head_Common_ColorChange.bas' in self.data.data_writer.files:
            ColorChange = True
        else:
            ColorChange = False
        #removing misc files
        if 'Actor/ASList/Head_ColorChangeOnly.baslist' in self.data.data_writer.files:
            del self.data.data_writer.files['Actor/ASList/Head_ColorChangeOnly.baslist']
        for file in self.data.data_writer.files:
            if file == 'Actor/AS/Head_Common_ColorChange.bas': continue
            if '.bas' in file:
                del self.data.data_writer.files[file]
            if '.baiprog' in file or '.baslist' in file:
                del self.data.data_writer.files[file]
        
        for file in data.data_writer.files:
            if '.baiprog' in file:
                pio = get_raw_data(data.data_sarc, 'Actor/AIProgram/Armor_Korok_Head.baiprog')
                self.data.data_writer.files['Actor/AIProgram/Armor_Korok_Head.baiprog'] = oead.aamp.ParameterIO.to_binary(pio)
           
            elif '.baslist' in file:
                new_name = file.replace(template,self.name)
                pio = get_raw_data(data.data_sarc, file)
                if ColorChange:
                    pio.lists['ASDefines'].objects['ASDefine_2'] = copy.deepcopy(pio.lists['ASDefines'].objects['ASDefine_0'])
                    pio.lists['ASDefines'].objects['ASDefine_2'].params['Name'] = oead.FixedSafeString64('ColorChange')
                    pio.lists['ASDefines'].objects['ASDefine_2'].params['Filename'] = oead.FixedSafeString64('Head_Common_ColorChange')
                raw_text = pio.to_text()
                raw_text = raw_text.replace(template, self.name)
                pio = oead.aamp.ParameterIO.from_text(raw_text)
                self.data.data_writer.files[new_name] = oead.aamp.ParameterIO.to_binary(pio)
            
            elif '.bas' in file:
                new_name = file.replace(template, self.name)
                pio = get_raw_data(data.data_sarc, file)
                raw_text = pio.to_text()
                raw_text = raw_text.replace(template, self.name)
                pio = oead.aamp.ParameterIO.from_text(raw_text)
                self.data.data_writer.files[new_name] = oead.aamp.ParameterIO.to_binary(pio)
        duplicate_bfres(f'{get_def_path()}\\Model\\{template}_Animation.sbfres', f'{self.pack_name}\\content\\Model\\{self.name}_Animation.sbfres', template, self.name)
        
        
        
    
    def create_armor(self):
        self.do_actorlink()
        self.get_recipe()
        self.do_gparam()
        self.do_model()
        if self.bfres_template: base = self.bfres_template
        else: base = self.base
        if self.bfres: name = self.bfres
        else: name = self.name

        Bfres_Dup(base, name, self.profile, self.pack_name).duplicate()
        actorpack = f'{self.pack_name}\\content\\Actor\\Pack\\{self.name}.sbactorpack'
        if not os.path.exists(actorpack):
            with open(actorpack, 'wb') as f:
                f.write(oead.yaz0.compress(self.data.data_writer.write()[1]))

    def get_name_from_sarc(self, ext):
        for elem in self.data.data_writer.files:
            if ext in elem:
                return elem
        sys.exit(f'No file with extension {ext}')

    def get_model_folder(self):
        p = self.name.split('_')
        res = 'Armor_' + p[1]
        return res


def update_sarc(pio, data, old_name, new_name):
    data.data_writer.files[new_name] = oead.aamp.ParameterIO.to_binary(pio)
    if old_name in data.data_writer.files:
        del data.data_writer.files[old_name]

def get_raw_data(data_sarc, file):
    data = data_sarc.get_file(file).data.tobytes()
    pio = oead.aamp.ParameterIO.from_binary(data)
    return pio

def make_armors_upgradeable(data):
    ups = get_res('upgradeable')
    for elem in data['Armors']:
        if not elem in ups:
            pass