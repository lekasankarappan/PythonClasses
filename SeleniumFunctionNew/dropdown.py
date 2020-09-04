from LaunchingBrowser import OpenChromeWM as op
from selenium.webdriver.support.select import Select
import time
op.driver.get("https://www.wikipedia.org/")
dd = op.driver.find_element_by_xpath("//select[@id='searchLanguage']")

sel = Select(dd)
sel.select_by_visible_text("فارسی")
time.sleep(4)
sel.select_by_index("45")
time.sleep(5)
sel.select_by_value("be")
time.sleep(4)
dd.send_keys("ภาษาไทย")
time.sleep(4)
op.driver.quit()