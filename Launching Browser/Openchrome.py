from selenium.webdriver import Chrome

path = "/Users/Lenovo/Desktop/PycharmProjects/Tutorial programs/driver/chromedriver"
#winPath = "/driver/chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("https://www.google.com")