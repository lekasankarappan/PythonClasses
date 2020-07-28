from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager

driver =Firefox(GeckoDriverManager().install())
driver.get("https://www.google.com")