
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

driver =  Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")
driver.maximize_window()
# ABsulote xpath
time.sleep(4)
search = driver.find_element_by_css_selector("#twotabsearchtextbox")
search.send_keys("Iphone xr", Keys.ENTER)

print("first search accomplished")
time.sleep(3)
#driver.delete_cookie()
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("samsung ", Keys.ENTER)
print("second search accomplished")
time.sleep(3)
driver.find_element_by_id("twotabsearchtextbox").send_keys("ipad pro ", Keys.ENTER)
time.sleep(3)
driver.quit()
