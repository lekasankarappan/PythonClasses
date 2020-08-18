
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

driver =  Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/")
driver.maximize_window()
# ABsulote xpath

driver.find_element_by_xpath("//input[@type='text' and @name='firstname']").send_keys("Arvind")

time.sleep(4)

driver.get("https://www.amazon.com")
time.sleep(2)
driver.find_element_by_xpath("//span[contains(text(),'Hello, Sign in') or contains(text(),'Hello. Sign in')]").click()


time.sleep(4)
driver.quit()
