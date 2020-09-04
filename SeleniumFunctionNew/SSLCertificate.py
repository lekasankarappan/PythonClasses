# from browser import openChrome as lp

from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
ops = ChromeOptions()
ops.add_argument("--disable-notifications")
ops.add_argument("--incognito")
ops.add_argument('--ignore-certificate-errors')
driver = Chrome(ChromeDriverManager().install(),options=ops)

driver.get("https://cacert.org/")
time.sleep(4)
driver.close()


"""
SSL--> Secure Sockets Layer
https://chromedriver.chromium.org/capabilities
https://www.guru99.com/chrome-options-desiredcapabilities.html
"""