from LaunchingBrowser import OpenChromeWM as op
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
op.driver.get("https://www.facebook.com/")
op.driver.find_element_by_xpath("//a[text()='Create New Account']").click()
time.sleep(4)
op.driver.find_element_by_xpath("//input[@value='1']").click()
time.sleep(5)
op.driver.find_element_by_xpath("//input[@name='firstname']").send_keys("sara",Keys.ENTER)
op.driver.find_element_by_xpath("//input[@name='lastname']").send_keys("mark")
#op.driver.find_element_by_name("firstname").send_keys("sara")
#op.driver.find_element_by_name("lastname").send_keys("visu")
op.driver.quit()
