from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
#from Selenium_Functions import Generic as gs
from SeleniumFunctionNew import GenericNew as gs
driver = Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.in")

#driver.save_screenshot("screenShot.png")

gs.takeScreenShot(driver,"Sc")
time.sleep(5)
driver.quit()