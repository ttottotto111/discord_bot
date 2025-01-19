import discord
from configparser import ConfigParser

config = ConfigParser()
config.read('setting.ini', encoding='utf-8')
token = config['bot_setting']['token']