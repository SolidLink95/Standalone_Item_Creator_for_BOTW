import configparser
import os,sys
from copy import deepcopy

from files_manage import file_to_json, json_to_file, get_res

def validateConfig(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    Flag = False
    todo = ['lang','mode','switch_path','wiiu_path','wiiu_update']
    if 'path' in config['DEFAULT']:
        Flag = True
        del config['DEFAULT']['path']

    for set in todo:
        if not set in config['DEFAULT']:
            Flag = True
            config['DEFAULT'][set] = ''
    if not 'is_bcml_settings' in config['DEFAULT']:
        Flag = True
        config['DEFAULT']['is_bcml_settings'] = "True"

    if not 'mods_path' in config['DEFAULT']:
        Flag = True
        config['DEFAULT']['mods_path'] = "MODS"

    if Flag:
        with open(config_file, 'w') as f:  # save
            config.write(f)

def validateData(data, prompt_w, armors, mod_content):
    print('starting validation')
    upgradeables = get_res('upgradeable')
    armors_rev = rev_json(armors)
    flag = True
    for weapon in data['Weapons']:
        if data['Weapons'][weapon]['physics'] == data['Weapons'][weapon]['base']:
            data['Weapons'][weapon]['physics'] = ''
    errors = []
    for armor in data['Armors']:
        if data['Armors'][armor]['physics'] == data['Armors'][armor]['base']:
            data['Armors'][armor]['physics'] = ''
        if not data['Armors'][armor]['base'] in upgradeables and data['Armors'][armor]['upgradeable']:
            errors.append(data['Armors'][armor]['base'])
    prompt_w.setWindowTitle('Error')
    prompt_w.buttons()
    mess = 'There was an error in creating the mod. The following armors does not use upgradeable armor as template:\n\n'
    for elem in errors:
        mess += f'{elem}\n'
    mess += '\nPlease choose for them one of the following armors as templates:\n\n'
    for elem in upgradeables:
        mess += f'{armors[elem]}\n'
    prompt_w.message.setPlainText(mess)
    if errors:
        prompt_w.show()
        flag = False
        return data, flag
    to_add_armors = {}
    for armor in data['Armors']:
        if data['Armors'][armor]['upgradeable']:
            root_name = data['Armors'][armor]['name']
            data['Armors'][armor]['armorStarNum'] = 1
            upgrades = get_upgrades_ids(root_name)
            print(upgrades)
            data['Armors'][armor]['armorNextRankName'] = upgrades[0]
            for i in range(len(upgrades)):
                split_name = root_name.split('_')
                new_arm = deepcopy(data['Armors'][armor])
                new_arm['armorStarNum'] = i + 2
                if i == (len(upgrades)-1): new_arm['armorNextRankName'] = ''
                else: new_arm['armorNextRankName'] = upgrades[i+1]
                new_arm['bfres'] = split_name[0] + '_' + split_name[1]
                new_arm['mainmodel'] = root_name
                new_arm['name'] = upgrades[i]
                new_arm['bfres_template'] = 'None' #data['Armors'][armor]['base']
                stars = '★'*(i+1)
                base_name = armors_rev[data['Armors'][armor]['base']] + ' ' + stars
                new_base = armors[base_name]
                new_arm['upgradeable'] = False
                new_arm['base'] = new_base
                new_arm['itemUseIconActorName'] = root_name
                if i == 0: new_arm['Crafting']['item1'] = root_name
                else: new_arm['Crafting']['item1'] = upgrades[i-1]
                new_arm['Crafting']['item1_n'] = '1'
                to_add_armors[upgrades[i]] = new_arm
    for armor in to_add_armors:
        data['Armors'][armor] = to_add_armors[armor]
    json_to_file('jsons\\TEST.json', data)
    return data, flag

def add_weapon_json(window,base):
    window.data['Weapons'][window.name_2.text()] = {
        "shop": window.shops[window.shop.currentText()],
        "base": window.weapons[base],
        "name": window.name_2.text(),
        "attack": window.attack.text(),
        "dur": window.dur.text(),
        "islifeinfinite": window.islifeinfinite.isChecked(),
        "sheath": window.sheath.currentText(),
        "elink": window.elink_2.text(),
        "slink": window.slink_2.text(),
        "profile": window.profile_2.currentText(),
        "magic": window.magic.text(),
        "magicspeed": window.magicspeed.text(),
        "magicradius": window.magicradius.text(),
        "magicrange": window.magicrange.text(),
        "magicpower": window.magicpower.text(),
        "magicgravity": window.magicgravity.text(),
        "ismagicinf": window.ismagicinf.isChecked(),
        "subtype": '',
        "physics": window.physics_2.text(),
        "price": window.price_2.text(),
        "name_desc": window.name_desc_2.text(),
        "desc": window.desc_2.toPlainText(),
        "anims": bool(window.anims.isChecked()),
        "Crafting": {
            "item1": window.items[window.item1_2.currentText()],
            "item1_n": window.item1_n_2.text(),
            "item2": window.items[window.item2_2.currentText()],
            "item2_n": window.item2_n_2.text(),
            "item3": window.items[window.item3_2.currentText()],
            "item3_n": window.item3_n_2.text()
        }
    }
    return window.data

def edit_weapon(window,x):
    window.TabWidget.setCurrentIndex(1)
    for elem in window.weapons:
        if window.weapons[elem] == window.data['Weapons'][x]['base']:
            window.base_2.setCurrentText(elem)
            break
    wep = window.data['Weapons'][x]
    window.name_2.setText(wep['name'])
    window.attack.setText(wep['attack'])
    if 'shop' in wep:
        window.shop.setCurrentText(window.shops_rev[wep["shop"]])
    else:
        window.shop.setCurrentText(window.shop_default)
    window.dur.setText(wep['dur'])
    window.islifeinfinite.setChecked(bool(wep['islifeinfinite']))
    window.sheath.setCurrentText(wep['sheath'])
    window.elink_2.setText(wep['elink'])
    window.slink_2.setText(wep['slink'])
    window.profile_2.setCurrentText(wep['profile'])
    window.magic.setText(wep['magic'])
    window.magicspeed.setText(wep['magicspeed'])
    window.magicradius.setText(wep['magicradius'])
    window.magicrange.setText(wep['magicrange'])
    window.magicpower.setText(wep['magicpower'])
    window.magicgravity.setText(wep['magicgravity'])
    window.ismagicinf.setChecked(bool(wep['ismagicinf']))
    window.physics_2.setText(wep['physics'])
    window.price_2.setText(wep['price'])
    window.name_desc_2.setText(wep['name_desc'])
    window.desc_2.setPlainText(wep['desc'])
    window.anims.setChecked(bool(wep['anims']))
    window.item1_2.setCurrentText(window.items_rev[wep['Crafting']['item1']])
    window.item2_2.setCurrentText(window.items_rev[wep['Crafting']['item2']])
    window.item3_2.setCurrentText(window.items_rev[wep['Crafting']['item3']])
    window.item1_n_2.setText(wep['Crafting']['item1_n'])
    window.item2_n_2.setText(wep['Crafting']['item2_n'])
    window.item3_n_2.setText(wep['Crafting']['item3_n'])

def edit_armor(window,x):
    window.TabWidget.setCurrentIndex(0)
    for elem in window.armors:
        if window.armors[elem] == window.data['Armors'][x]['base']:
            window.base.setCurrentText(elem)
            break
    arm = window.data['Armors'][x]
    window.name.setText(arm['name'])
    window.defence.setText(arm['defence'])
    if 'bfres_template' in arm: window.bfres_template.setText(arm['bfres_template'])
    if 'bfres' in arm: window.bfres.setText(arm['bfres'])
    if 'mainmodel' in arm: window.mainmodel.setText(arm['mainmodel'])
    try:
        if 'shop' in arm:
            window.shop.setCurrentText(window.shops_rev[arm["shop"]])
        else:
            window.shop.setCurrentText(window.shop_default)
    except:
        pass
    if 'upgradeable' in arm: window.upgradeable.setChecked(bool(arm['upgradeable']))
    window.elink.setText(arm['elink'])
    window.slink.setText(arm['slink'])
    window.profile.setCurrentText(arm['profile'])
    window.effect.setCurrentText(arm['effect'])
    window.series.setCurrentText(arm['series'])
    window.effect_lv.setText(arm['effect_lv'])
    window.price.setText(arm['price'])
    window.physics.setText(arm['physics'])
    window.name_desc.setText(arm['name_desc'])
    window.desc.setPlainText(arm['desc'])
    window.korok_mask.setChecked(bool(arm['korok_mask']))
    window.item1.setCurrentText(window.items_rev[arm['Crafting']['item1']])
    window.item2.setCurrentText(window.items_rev[arm['Crafting']['item2']])
    window.item3.setCurrentText(window.items_rev[arm['Crafting']['item3']])
    window.item1_n.setText(arm['Crafting']['item1_n'])
    window.item2_n.setText(arm['Crafting']['item2_n'])
    window.item3_n.setText(arm['Crafting']['item3_n'])

def add_armor_json(window, shop_local, base, armorNextRankName, armorStarNum, itemUseIconActorName):
    window.data['Armors'][window.name.text()] = {
        "shop": shop_local,
        "base": window.armors[base],
        "name": window.name.text(),
        "armorNextRankName": armorNextRankName,
        "armorStarNum": armorStarNum,
        "itemUseIconActorName": itemUseIconActorName,
        "bfres_template": window.bfres_template.text(),
        "bfres": window.bfres.text(),
        "mainmodel": window.mainmodel.text(),
        "defence": window.defence.text(),
        "elink": window.elink.text(),
        "slink": window.slink.text(),
        "profile": window.profile.currentText(),
        "effect": window.effect.currentText(),
        "effect_lv": window.effect_lv.text(),
        "series": window.series.currentText(),
        "physics": window.physics.text(),
        "price": window.price.text(),
        "name_desc": window.name_desc.text(),
        "desc": window.desc.toPlainText(),
        "korok_mask": bool(window.korok_mask.isChecked()),
        "upgradeable": bool(window.upgradeable.isChecked()),
        "Crafting": {
            "item1": window.items[window.item1.currentText()],
            "item1_n": window.item1_n.text(),
            "item2": window.items[window.item2.currentText()],
            "item2_n": window.item2_n.text(),
            "item3": window.items[window.item3.currentText()],
            "item3_n": window.item3_n.text()
        }
    }
    return window.data

def validate_test(window):
    window.armors_rev = rev_json(window.armors)
    defence_step = 5
    to_add_armors = {}
    for armor in window.data['Armors']:
        if window.data['Armors'][armor]['upgradeable']:
            root_name = armor
            window.data['Armors'][armor]['armorStarNum'] = 1
            if not window.data['Armors'][armor]['defence']: window.data['Armors'][armor]['defence'] = '5'
            new_defence = int(window.data['Armors'][armor]['defence']) + defence_step
            upgrades = get_upgrades_ids(root_name)
            if not upgrades: return
            print(upgrades)
            window.data['Armors'][armor]['armorNextRankName'] = upgrades[0]
            window.items[window.data['Armors'][armor]['name_desc']] = armor
            window.armors[window.data['Armors'][armor]['name_desc']] = armor
            window.armors_rev[armor] = window.data['Armors'][armor]['name_desc']
            window.items_rev[armor] = window.data['Armors'][armor]['name_desc']
            window.item1.addItem(window.data['Armors'][armor]['name_desc'])
            for i in range(len(upgrades)):
                split_name = root_name.split('_')
                new_arm = deepcopy(window.data['Armors'][armor])
                new_arm['armorStarNum'] = i + 2
                if i == (len(upgrades) - 1):
                    new_arm['armorNextRankName'] = ''
                else:
                    new_arm['armorNextRankName'] = upgrades[i + 1]
                new_arm['bfres'] = split_name[0] + '_' + split_name[1]
                new_arm['mainmodel'] = root_name
                new_arm['defence'] = str(new_defence)
                new_arm['itemUseIconActorName'] = root_name
                new_arm['name'] = upgrades[i]
                new_arm['bfres_template'] = 'None'  # data['Armors'][armor]['base']
                stars = '★' * (i + 1)
                base_name = window.armors_rev[window.data['Armors'][armor]['base']] + ' ' + stars
                new_base = window.armors[base_name]
                new_arm['upgradeable'] = False
                new_arm['base'] = new_base
                new_arm['shop'] = f'Npc_DressFairy_0{str(i)}'
                if i == 0:
                    new_arm['Crafting']['item1'] = root_name
                else:
                    new_arm['Crafting']['item1'] = upgrades[i - 1]
                new_arm['Crafting']['item1_n'] = '1'
                new_defence += defence_step
                to_add_armors[upgrades[i]] = new_arm
                new_name = new_arm['name_desc'] + ' ' + stars
                window.items_rev[upgrades[i]] = new_name
                window.items[new_name] = upgrades[i]
                window.item1.addItem(new_name)
    for armor in to_add_armors:
        window.Mod_content.addItem(armor)
        window.data['Armors'][armor] = to_add_armors[armor]
    #json_to_file('jsons\\TEST.json', window.data)
    window.Upgrade_armors.setEnabled(False)

def rev_json(data):
    new_res = {}
    for elem in data:
        new_res[data[elem]] = elem
    return new_res

def get_upgrades_ids(id):
    try:
        slot = id.split('_')[1]
        print(slot)
        if slot[0] == '0':
            index = 1
            n = int(slot[:index])
        elif slot[0] == '0' and slot[1] == '0':
            index = 2
            n = int(slot[:index])
        else:
            index = 0
            n = int(slot)
        result = []
        for i in range(4):
            n+=1
            if index > 0: zeros = '0'*index
            else: zeros = ''
            result.append( id.split('_')[0] + '_' + zeros + str(n) + '_' + id.split('_')[-1])
    except:
        result = []
    return result