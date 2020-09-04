from LaunchingBrowser import OpenChromeWM as op
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
from SeleniumFunctionNew import MyGeneric as gs
op.driver.get("http://the-internet.herokuapp.com/javascript_alerts")
op.driver.find_element_by_xpath("//button[text()='Click for JS Alert']").click()
alert = op.driver.switch_to_alert()
print("Alert text",alert.text)
alert.accept()

op.driver.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()
time.sleep(2)
gs.Dismissalert(op.driver)


time.sleep(2)

op.driver.find_element_by_xpath("//button[text()='Click for JS Prompt']").click()
time.sleep(2)
gs.AcceptalertandSendkeys(op.driver,"Hello Neel")
time.sleep(2)

msg =op.driver.find_element_by_xpath("//p[@id='result']")
print(msg.text)

op.driver.quit()



time.sleep(5)

op.driver.quit()
