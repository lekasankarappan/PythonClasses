from LaunchingBrowser import OpenChromeWM as op
from selenium.webdriver.common.keys import Keys
import time
op.driver.get("http://www.amazon.in")
op.driver.find_element_by_id("twotabsearchtextbox").send_keys("iphone",Keys.ENTER)

time.sleep(3)
op.driver.quit()