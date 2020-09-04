

def acceptalert(driver):
    alert = driver.switch_to.alert
    print("Alert Title ", alert.text)
    alert.accept()

def Dismissalert(driver):
    alert = driver.switch_to.alert
    print("Alert Title ", alert.text)
    alert.dismiss()

def AcceptalertandSendkeys(driver,text):
    alert = driver.switch_to.alert
    print("Alert Title ", alert.text)
    alert.send_keys(text)
    alert.accept()

def dismissAlertAndSendKeys(driver, text):
    alert = driver.switch_to.alert
    print("Alert Title ", alert.text)
    alert.send_keys(text)
    alert.dismiss()
