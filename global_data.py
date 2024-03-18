import configparser

"""
读取配置
"""
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
for item in config.items('basic'):
    globals()[item[0]] = item[1]
