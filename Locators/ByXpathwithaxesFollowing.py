from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


driver=Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/tables")

time.sleep(3)
name = "Bach"
val =driver.find_element_by_xpath("//table[@id='table1']/tbody/tr/td[contains(text(),'"+name+"')]//following::td[3]").text
print(val)

driver.quit()


