from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

ops=ChromeOptions()
ops.add_argument("--disable-notifications")
driver=Chrome(ChromeDriverManager().install(),options=ops)
driver.get("https://www.google.in/")
tag = driver.find_elements_by_tag_name("a")
print("Total no of links" , len(tag))
for link in tag:
   print(link.text+" --- "+ link.get_attribute("href"))
driver.quit()





