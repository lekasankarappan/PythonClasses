from configparser import ConfigParser

def getvalue(section,option):
    conf=ConfigParser()
    conf.read("data.ini")
    value=conf.get(section,option)
    return value
