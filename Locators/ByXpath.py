from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


driver=Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
#driver.find_element_by_xpath("//input[@class='gLFyf gsfi' and @name='q' and @type='text']").send_keys("Appium jobs",Keys.ENTER)

driver.find_element_by_xpath("//input[@class='gLFyf gsfi'and @name='q' and @type='text' ]").send_keys("Appium job",Keys.ENTER)






