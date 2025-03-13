'''
获取配置文件的相关信息
'''

import configparser
import pathlib
#定义conf.ini的路径
file=pathlib.Path(__file__).parents[0].resolve()/'conf.ini'
#此处读取到上级文件的路径

#读取配置信息
def read(section,option):
    conf=configparser.ConfigParser()
    conf.read(file)
    values=conf.get(section,option)
    return values

#写入配置项
def write(section,option,value):
    conf=configparser.ConfigParser()
    conf.read(file)
    #如果配置结构中section存在则不进行任何操作
    if not conf.has_section(section):
        conf.add_section(section)
    conf.set(section,option,value)
    with open(file,'w')as f:
        conf.write(f)
        