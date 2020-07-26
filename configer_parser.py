"""
    this is for configparser 
"""
import configparser

conf = configparser.ConfigParser()

conf.read('./config.ini')
print(conf.get('DEFAULT','DATABASE'))
# getboolean 0  no false off  都返回的是false
#            1  yes true on   都返回的是true
print(conf.getboolean('BOOL','flag'))