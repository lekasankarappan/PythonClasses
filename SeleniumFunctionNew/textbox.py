from LaunchingBrowser import OpenChromeWM as op
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
op.driver.get("https://www.wikipedia.org/")
op.driver.find_element_by_xpath("//input[@id='searchInput']").send_keys("hindi",Keys.ENTER)
time.sleep(4)
op.driver.quit()
