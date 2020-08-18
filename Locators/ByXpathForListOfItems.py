
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

driver =  Chrome(ChromeDriverManager().install())
driver.get("https://www.flipkart.com/")
driver.maximize_window()
# ABsulote xpath
time.sleep(4)
driver.find_element_by_xpath("//button[text()='✕']").click()
time.sleep(4)
driver.find_element_by_name("q").send_keys('iphone xr 64',Keys.ENTER)
time.sleep(3)

phone = driver.find_element_by_xpath("//*[text()='Apple iPhone XR (Black, 64 GB)']")
print(phone.text)
phone.click()
price = driver.find_element_by_xpath("//*[text()='₹52,500']").text
print(price)
#price=driver.find_element_by_class_name("_1vC4OE _3qQ9m1")


time.sleep(3)
driver.quit()
