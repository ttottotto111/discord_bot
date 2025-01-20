import discord
from configparser import ConfigParser

import item_dict

config = ConfigParser()
config.read('setting.ini', encoding='utf-8')
token = config['bot_setting']['token']
