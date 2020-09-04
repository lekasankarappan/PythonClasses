from LaunchingBrowser import OpenChromeWM as op
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
op.driver.get("https://demoqa.com/automation-practice-form")
op.driver.find_element_by_id("dateOfBirthInput").click()
month=op.driver.find_element_by_class_name("react-datepicker__month-select")
year=op.driver.find_element_by_class_name("react-datepicker__year-select")
sel=Select(month)
sel.select_by_visible_text("April")
sel=Select(year)
sel.select_by_visible_text("2000")
time.sleep(4)

listDate = op.driver.find_element_by_xpath("//div[contains(@class,'react-datepicker__day react-datepicker__day--022')]").click()
#listDate[4].click()
time.sleep(4)
#op.driver.find_element_by_xpath("//input[@id='hobbies-checkbox-1'and@value='1']").click()
time.sleep(4)

op.driver.quit()
