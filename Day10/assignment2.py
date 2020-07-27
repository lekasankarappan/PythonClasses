# from selenium.webdriver import Chrome
# from webdriver_manager.chrome import ChromeDriverManager
# driver=Chrome(ChromeDriverManager().install())
# driver.get("https://www.wikipedia.org/")
# #//TAGNAME[@Attribute='value'/TAGNAME
# lang = driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")
# name=[]
# print("list of lang:",len(lang))
# for l in lang:
#     name.append(l.text)
# #print(name)
# file=open("demo2.txt","a")
# file.writelines(str(name))
# #file.write(str(name))
# file.close()
# #time.sleep(1)
# driver.close()
#from Aravinda nath to everyone:
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
driver = Chrome(ChromeDriverManager().install())
driver.get("https://www.wikipedia.org/")
lang =driver.find_elements_by_css_selector("#searchLanguage>option")
name =[]
for i in lang:
    name.append(i.text)
driver.close()
file=open("demo2.txt",'a')

file.write(str(name))
file.close()

