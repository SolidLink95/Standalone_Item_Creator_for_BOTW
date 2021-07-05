import configparser
from shutil import copyfile
import sys
import os
import oead
from files_manage import create_folder, get_def_path, file_to_json, calc_profile, get_res, get_endianness, get_file_path


class Bfres_Dup:
    def __init__(self, base, name, profile, target_path):
        self.name = name
        self.base = base
        self.profile = profile
        self.pack_name = target_path
    
    
    def duplicate(self):
        base, name = self.base, self.name
        try:
            base, name = check_base(base, name, self.profile)
        except:
            pass
        #path = f'{get_def_path()}\\Model\\'
        #if get_endianness():
        #    base_bfres = [path + base + '.sbfres', path + base + '.Tex1.sbfres', path + base + '.Tex2.sbfres']
        #else:
        #    base_bfres = [path + base + '.sbfres', path + base + '.Tex.sbfres']

        if get_endianness():
            base_bfres = [get_file_path(f'Model\\{base}.sbfres'),
                     get_file_path(f'Model\\{base}.Tex1.sbfres'),
                     get_file_path(f'Model\\{base}.Tex2.sbfres')]
        else:
            base_bfres = [get_file_path(f'Model\\{base}.sbfres'),
                     get_file_path(f'Model\\{base}.Tex.sbfres')]

        for file in base_bfres:
            if os.path.exists(file):
                output = self.pack_name + '\\content\\Model\\' + file.split('\\')[-1].replace(base, name)
                duplicate_bfres(file, output, old_bfres_name=base, new_bfres_name=name)


        #icon = get_def_path() + '\\UI\\StockItem\\' + self.base + '.sbitemico'
        icon = get_file_path(f'UI\\StockItem\\{self.base}.sbitemico')
        if os.path.exists(icon):
            output = self.pack_name + '\\content\\UI\\StockItem\\' + icon.split('\\')[-1].replace(self.base, self.name)
            duplicate_bfres(icon, output, old_bfres_name=self.base, new_bfres_name=self.name)
        #try_copy(f'{get_def_path()}\\UI\\StockItem\\{self.base}.01.sbitemico', f'{self.pack_name}\\content\\UI\\StockItem\\{self.name}.01.sbitemico')
        
        #icon_01_base = f'{get_def_path()}\\UI\\StockItem\\{self.base}.01.sbitemico'
        icon_01_base = get_file_path(f'UI\\StockItem\\{self.base}.01.sbitemico')
        icon_01_out = f'{self.pack_name}\\content\\UI\\StockItem\\{self.name}.01.sbitemico'
        duplicate_bfres(icon_01_base, icon_01_out, old_bfres_name=self.base, new_bfres_name=self.name)
        
        
    def duplicate_armor(self):
        pass

def check_base(base, name, profile):
    if profile == '':
        profile = calc_profile(name)
    if 'Weapon' in profile:
        if not len(base) == len(name):
            n = (name.split("_")[-1])
            size = (-1) * len(n)
            base = name[:size] + '001'
    elif 'Armor' in profile:
        a =  get_res('armors_bfres')
        base = a['Armors'][base]
        name = name[:len(base)]
    return base, name

def try_copy(file1, file2):
    if os.path.exists(file1):
        copyfile(file1, file2)

def remove_ext(file):
    ext = file.split('.')[-1]
    size = (-1) * (len(ext) + 1)
    return file[:size]

def duplicate_bfres(old_file, new_file, old_bfres_name='', new_bfres_name=''):
    if not old_bfres_name:
        old_bfres_name = remove_ext(os.path.basename(old_file))
        old_bfres_name = old_bfres_name.replace('.Tex1','').replace('.Tex2','').replace('.Tex','')
    if not new_bfres_name:
        new_bfres_name = remove_ext(os.path.basename(new_file))
        new_bfres_name = new_bfres_name.replace('.Tex1','').replace('.Tex2','').replace('.Tex','')

    if not os.path.exists(old_file):
        #print("'" + old_file +"' does not exist")
        return
    if os.path.exists(new_file):
        #print("'" + new_file +"' already exists")
        return
    if len(old_bfres_name) != len(new_bfres_name):
        #print("'" + old_bfres_name + "' --> '" + new_bfres_name + "' - New name must be same length as old name")
        return
    #print(old_bfres_name + ' --> ' + new_bfres_name)
    
    with open(old_file, "rb") as f:
        bfres_rawdata = f.read()
        if not bfres_rawdata[:4] == b"Yaz0":
            print(f'File {old_file} is not yaz0 archive')
            return
        content = oead.yaz0.decompress(bfres_rawdata)
    to_write = content.replace(old_bfres_name.encode(), new_bfres_name.encode())
    to_write = oead.yaz0.compress(to_write)
    with open(new_file, "wb") as f:
        f.write(to_write)

