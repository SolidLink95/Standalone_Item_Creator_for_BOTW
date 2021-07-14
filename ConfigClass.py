import configparser
import os, sys
from files_manage import file_to_json


class Config:
    def __init__(self, config='config.ini'):
        self.config_file = config
        self.wiiu_base = ''
        self.wiiu_update = ''
        self.switch = ''
        self.lang = ''
        self.bcml_path = os.path.expandvars(r'%LOCALAPPDATA%\bcml')
        self.settings = os.path.join(self.bcml_path, 'settings.json')

    def get_paths(self):
        data = file_to_json(self.settings)
        self.wiiu_base = data['game_dir']
        self.wiiu_update = data['update_dir']
        self.switch = data['game_dir_nx']
        self.lang = data['lang']

    def save_to_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        config['DEFAULT']['wiiu_path'] = self.wiiu_base
        config['DEFAULT']['wiiu_update'] = self.wiiu_update
        config['DEFAULT']['switch_path'] = self.switch
        config['DEFAULT']['lang'] = f'Bootup_{self.lang}'
        Flag = False
        if not 'is_bcml_settings' in config['DEFAULT']: config['DEFAULT']['is_bcml_settings'] = "True"
        else: Flag = bool(config['DEFAULT']['is_bcml_settings'])
        if Flag:
            with open(self.config_file, 'w') as f:  # save
                config.write(f)
                print('config imported from bcml')
