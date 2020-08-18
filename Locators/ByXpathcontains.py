from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


driver=Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com")
driver.find_element_by_xpath("//a[contains(text(),'Deals')]").click()
#time.sleep(2)
driver.find_element_by_xpath("//input[contains(@id,'two')]").send_keys("iphone",Keys.ENTER)
time.sleep(4)
driver.find_element_by_xpath("//a[text()='Gift Cards']").click()
time.sleep(4)

driver.quit()





