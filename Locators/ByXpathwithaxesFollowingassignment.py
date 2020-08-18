from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


driver=Chrome(ChromeDriverManager().install())
driver.get("https://markets.businessinsider.com/")

time.sleep(3)
#name="Microsoft"
val=driver.find_element_by_xpath("//table[@class='table instruments no-margin-bottom']/tbody/tr/td[contains(text(),Microsoft)]//following::td[1]").text
#val = driver.find_element_by_xpath("//table[@class='table instruments no-margin-bottom']/tbody/tr/td[contains(text(),'"+name+"',Microsoft)]//following::td[1]").text

print(val)
driver.quit()

#for n in name: