from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
ops=ChromeOptions()
ops.add_argument("--disable-notifications")

driver=Chrome(ChromeDriverManager().install(),options=ops)
driver.get("https://www.amazon.in")
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("Apple iPhone XR (128GB)-Yellow",Keys.ENTER)
#driver.fi  e XR (128GB) - Yellow").click()
#driver.find_element_by_class_name("nav-input")[0].click()
time.sleep(5)
amazon_price = driver.find_element_by_class_name("a-price-whole")[1].text
amazon_price = int(amazon_price.replace(",", ""))
print(amazon_price)


driver.get("https://www.flipkart.com")
driver.find_element_by_xpath("//button[text()='✕']").click()
driver.find_element_by_class_name("LM6RPg").send_keys("Apple iPhone XR (128GB)-Yellow",Keys.ENTER)
flip_price=driver.find_element_by_class_name("_1vC4OE").text
flip_price=flip_price.replace(",", "")
flip_price=int(flip_price("₹", ""))
print(flip_price)
#driver.find_element_by_xpath("//input[@type='text' and @name='firstname']").send_keys("leka")
#time.sleep(4)
#driver.quit()





