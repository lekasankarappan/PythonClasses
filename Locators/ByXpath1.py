from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
ops=ChromeOptions()
ops.add_argument("--disable-notifications")

driver=Chrome(ChromeDriverManager().install(),options=ops)
driver.get("https://www.amazon.com")
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("iphone",Keys.ENTER)

time.sleep(2)

driver.get("https://www.facebook.com")
driver.find_element_by_xpath("//input[@type='text' and @name='firstname']").send_keys("leka")
time.sleep(4)
driver.quit()





