from LaunchingBrowser import OpenChromeWM as op
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
op.driver.get("https://www.facebook.com/")
op.driver.find_element_by_xpath("//a[text()='Create New Account']").click()
time.sleep(4)
op.driver.find_element_by_xpath("//input[@value='1']").click()
time.sleep(5)
op.driver.quit()
