from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

messageField = driver.find_element("xpath",'/html/body/div[2]/div/div[2]/div[1]/div[2]/form/div/input')
messageField.send_keys("hello world mparticle!")
showMessageButton = driver.find_element("xpath",'/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
showMessageButton.click()

enterA = driver.find_element("xpath", '/html/body/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/input')
enterB = driver.find_element("xpath", '/html/body/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/input')
enterA.send_keys('200')
enterB.send_keys('23')
getTotal = driver.find_element("xpath", '/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
getTotal.click()