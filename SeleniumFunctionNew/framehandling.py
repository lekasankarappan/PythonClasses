from LaunchingBrowser import OpenChromeWM as op

import time

op.driver.get("https://docs.oracle.com/javase/8/docs/api/")

op.driver.switch_to_frame("packageListFrame")

op.driver.find_element_by_link_text("java.applet").click()
time.sleep(3)

op.driver.switch_to_default_content()

op.driver.switch_to_frame("packageFrame")

op.driver.find_element_by_link_text("AudioClip").click()

op.driver.switch_to_default_content()
op.driver.switch_to.frame("classFrame")
time.sleep(2)
op.driver.find_element_by_xpath("//a[text()='loop']").click()

time.sleep(2)
op.driver.quit()

