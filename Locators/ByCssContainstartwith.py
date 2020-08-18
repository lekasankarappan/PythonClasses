
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

driver =  Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")
driver.maximize_window()
driver.find_element_by_css_selector("input[id^='twot']").send_keys("kindle",Keys.ENTER)
time.sleep(4)



driver.quit()
