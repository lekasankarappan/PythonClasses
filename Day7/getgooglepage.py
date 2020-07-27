#from selenium import webdriver

from selenium.webdriver import Chrome
#from selenium.webdriver import firefox
import time
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
driver = Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")
#//TAGNAME[@Attribute='value'/TAGNAME
#lang = driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")
#print("list of lang:",len(lang))
#for l in lang:
 #   print(l.text)
#time.sleep(1)
driver.close()

