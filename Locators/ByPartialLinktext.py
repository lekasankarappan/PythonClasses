from LaunchingBrowser import OpenChromeWM as op
from selenium.webdriver.common.keys import Keys
import time
op.driver.get("http://www.google.com")
op.driver.maximize_window()
op.driver.find_element_by_partial_link_text("Ima").click()

time.sleep(3)
op.driver.quit()