from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
ops=ChromeOptions()
ops.add_argument("--disable-notifications")

driver=Chrome(ChromeDriverManager().install(),options=ops)
driver.get("https://www.amazon.in")
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("Apple iPhone XR black 64 ",Keys.ENTER)
time.sleep((5))
driver.find_element_by_xpath("//*[text()='Apple iPhone XR (64GB) - Black']").click()

amazon_price=driver.find_element_by_xpath("//span[text()='₹ 51,500.00']").text

time.sleep(5)
#amazon_price = driver.find_element_by_xpath("//*[text()='51,500']").text
amazon_price = int(amazon_price.replace(",", ""))
amazon_price=int(amazon_price.replace("₹", ""))
print(amazon_price)
time.sleep(4)

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
price =price.replace(",", "")
price=int(price.replace("₹", ""))
print(price)
#price=driver.find_element_by_class_name("_1vC4OE _3qQ9m1")

if(amazon_price>=price):
    print("Go with Flipkart")
elif(amazon_price==price):
    print("Both are same")
else:
    print("Amazon price is cheap")
time.sleep(3)
driver.quit()




