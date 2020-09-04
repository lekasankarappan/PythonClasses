# from browser import openChrome as lp

from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
ops = ChromeOptions()
ops.add_argument("--disable-notifications")
#ops.add_argument("--incognito")
#ops.add_argument('--ignore-certificate-errors')
driver = Chrome(ChromeDriverManager().install(),options=ops)

driver.get("https://www.icicibank.com/")
driver.find_element_by_class_name("pl-login-ornage-box").click()

time.sleep(4)
driver.close()


"""

https://chromedriver.chromium.org/capabilities

"""