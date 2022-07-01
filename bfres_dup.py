import configparser
from shutil import copyfile
import sys
import os
import oead
from files_manage import create_folder, get_def_path, file_to_dict, calc_profile, get_res, get_endianness, get_file_path


class Bfres_Dup:
    def __init__(self, base, name, profile, target_path):
        self.name = name
        self.base = base
        self.profile = profile
        self.pack_name = target_path

    def duplicate(self):
        base, name = check_base(self.base, self.name, self.profile)

        if get_endianness():
            base_bfres = [get_file_path(os.path.join('Model', f'{base}.sbfres')),
                          get_file_path(os.path.join('Model', f'{base}.Tex1.sbfres')),
                          get_file_path(os.path.join('Model', f'{base}.Tex2.sbfres'))]
        else:
            base_bfres = [get_file_path(os.path.join('Model', f'{base}.sbfres')),
                          get_file_path(os.path.join('Model', f'{base}.Tex.sbfres'))]

        for file in [ff for ff in base_bfres if os.path.exists(ff)]:
            output = os.path.join(self.pack_name, r'content\Model', file.split('\\')[-1].replace(base, name))
            duplicate_bfres(file, output, old_bfres_name=base, new_bfres_name=name)

        icon = get_file_path(os.path.join(r'UI\StockItem', f'{self.base}.sbitemico'))
        if os.path.exists(icon):
            output = os.path.join(self.pack_name, r'content\UI\StockItem', icon.split('\\')[-1].replace(self.base, self.name))
            duplicate_bfres(icon, output, old_bfres_name=self.base, new_bfres_name=self.name)

        icon_01_base = get_file_path(os.path.join(r'UI\StockItem', f'{self.base}.01.sbitemico'))
        icon_01_out = os.path.join(self.pack_name, r'content\UI\StockItem', f'{self.name}.01.sbitemico')
        duplicate_bfres(icon_01_base, icon_01_out, old_bfres_name=self.base, new_bfres_name=self.name)

    def duplicate_armor(self):
        pass


def check_base(base, name, profile):
    try:
        if profile == '':
            profile = calc_profile(name)
        if 'Weapon' in profile:
            if not len(base) == len(name):
                n = (name.split("_")[-1])
                size = (-1) * len(n)
                base = name[:size] + '001'
        elif 'Armor' in profile:
            a = get_res('armors_bfres')
            base = a['Armors'][base]
            name = name[:len(base)]
    except:
        print(f'Error for checking base: {base}, {name}')
    return base, name


def try_copy(file1, file2):
    if os.path.exists(file1):
        copyfile(file1, file2)


def remove_ext(file):
    ext = file.split('.')[-1]
    size = (-1) * (len(ext) + 1)
    return file[:size]


def duplicate_bfres(old_file, new_file, old_bfres_name=None, new_bfres_name=None):
    if old_bfres_name is None:
        old_bfres_name = remove_ext(os.path.basename(old_file))
        old_bfres_name = old_bfres_name.replace('.Tex1', '').replace('.Tex2', '').replace('.Tex', '')
    if new_bfres_name is None:
        new_bfres_name = remove_ext(os.path.basename(new_file))
        new_bfres_name = new_bfres_name.replace('.Tex1', '').replace('.Tex2', '').replace('.Tex', '')

    if not os.path.exists(old_file) or os.path.exists(new_file) or len(old_bfres_name) != len(new_bfres_name):
        return

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
