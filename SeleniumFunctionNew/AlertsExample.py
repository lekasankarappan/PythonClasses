from LaunchingBrowser import OpenChromeWM as op
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
op.driver.get("https://mypage.rediff.com/login/dologin")

op.driver.find_element_by_xpath("//*[@type='submit']").click()
time.sleep(4)

alert = op.driver.switch_to.alert
# accept is clicking on OK button
alert.accept()
time.sleep(4)
op.driver.find_element_by_id("txtlogin").send_keys("aravind@gmail.com")




op.driver.quit()
