import os,sys
from files_manage import file_to_json, json_to_file, get_res

def validateData(data, prompt_w, armors):
    upgradeables = get_res('upgradeable')
    flag = True
    for weapon in data['Weapons']:
        if data['Weapons'][weapon]['physics'] == data['Weapons'][weapon]['base']:
            data['Weapons'][weapon]['physics'] = ''
    errors = []
    for armor in data['Armors']:
        if data['Armors'][armor]['physics'] == data['Armors'][armor]['base']:
            data['Armors'][armor]['physics'] = ''
        if not data['Armors'][armor]['base'] in upgradeables:
            errors.append(data['Armors'][armor]['base'])
    prompt_w.setWindowTitle('Error')
    prompt_w.buttons()
    mess = 'There was an error in creating the mod. The following armors does not use upgradeable armor as template:\n\n'
    for elem in errors:
        mess += f'{elem}\n'
    mess += '\nPlease choose for them one of the following armors as templates:\n\n'
    for elem in upgradeables:
        mess += f'{armors[elem]}\n'
    prompt_w.message.setPlainText('There was')
    if errors: flag = False
    return data, flag
