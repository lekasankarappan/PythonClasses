from LaunchingBrowser import OpenChromeWM as op

import time

op.driver.get("http://the-internet.herokuapp.com/upload")
op.driver.find_element_by_id("file-upload").send_keys("C:/Users/Lenovo/Pictures/Camera Roll/scene.jpg")
time.sleep(2)
op.driver.find_element_by_id("file-submit").click()

time.sleep(2)
op.driver.quit()
