from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from Day10 import Generic as gs


driver=Chrome(ChromeDriverManager().install())
url=gs.getvalue("TC001","url")
driver.get(url)
driver.close()
