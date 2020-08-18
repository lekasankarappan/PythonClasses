from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


driver=Chrome(ChromeDriverManager().install())
driver.get("https://www.flipkart.com")

driver.find_element_by_xpath("//button[text()='✕']").click()

driver.find_element_by_xpath("//span[text()='Cart']").click()
time.sleep(3)
driver.back()
time.sleep(5)
driver.find_element_by_xpath("//span[text()='Cart']").click()
time.sleep(5)
driver.quit()





