from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


driver=Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/tables")


time.sleep(4)

val =driver.find_element_by_xpath("//table[@id='table1']/tbody/tr/td[contains(text(),'tconway@earthlink.net')]//preceding-sibling::td[2]").text
print(val)
driver.quit()

#//table[@class='table instruments no-margin-bottom']/tbody/tr/td[contains(text(),'280.26')]//preceding::td[1]


