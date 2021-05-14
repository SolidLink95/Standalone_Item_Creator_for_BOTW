import os,sys
from copy import deepcopy

from files_manage import file_to_json, json_to_file, get_res

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
            data['Armors'][armor]['armorStarNum'] = 1
            upgrades = get_upgrades_ids(data['Armors'][armor]['base'])
            print(upgrades)
            data['Armors'][armor]['armorNextRankName'] = upgrades[0]
            for i in range(len(upgrades)):
                split_name = upgrades[i].split('_')
                new_arm = deepcopy(data['Armors'][armor])
                new_arm['armorStarNum'] = i + 2
                if i == (len(upgrades)-1): new_arm['armorNextRankName'] = ''
                else: new_arm['armorNextRankName'] = upgrades[i+1]
                new_arm['bfres'] = split_name[0] + '_' + split_name[1]
                new_arm['mainmodel'] = upgrades[i]
                new_arm['name'] = upgrades[i]
                new_arm['bfres_template'] = data['Armors'][armor]['base']
                stars = '★'*(i+2)
                base_name = armors_rev[data['Armors'][armor]['base']] + ' ' + stars
                new_base = armors[base_name]
                new_arm['base'] = new_base
                data['Armors'][upgrades[i]] = new_arm
    json_to_file('jsons\\TEST.json', data)
    return data, flag


def validate_test(data):
    upgradeables = get_res('upgradeable')
    armors=get_res('armors')
    armors_rev = rev_json(armors)
    flag=True
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
                if i == 0: new_arm['Crafting']['item1'] = root_name
                else: new_arm['Crafting']['item1'] = upgrades[i-1]
                new_arm['Crafting']['item1_n'] = '1'
                to_add_armors[upgrades[i]] = new_arm
    for armor in to_add_armors:
        data['Armors'][armor] = to_add_armors[armor]
    json_to_file('jsons\\TEST.json', data)
    return data, flag

def rev_json(data):
    new_res = {}
    for elem in data:
        new_res[data[elem]] = elem
    return new_res

def get_upgrades_ids(id):
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
    return result