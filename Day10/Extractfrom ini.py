from configparser import ConfigParser

conf=ConfigParser() #object of the class
print(conf.read("data.ini"))
print("sections:",conf.sections())
print("results:",conf.get('TC001','url'))