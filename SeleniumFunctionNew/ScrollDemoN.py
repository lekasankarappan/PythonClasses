from LaunchingBrowser import OpenChromeWM as op
from selenium.webdriver.common.keys import Keys
import time

op.driver.get("https://www.amazon.in/")

#backtoTop= op.driver.find_element_by_xpath("//span[text()='Back to top']")
backtotop=op.driver.find_element_by_class_name("navFooterBackToTopText")
#Java Script
op.driver.execute_script("arguments[0].scrollIntoView();",backtotop)

time.sleep(5)
backtotop.click()
time.sleep(5)
op.driver.quit()


