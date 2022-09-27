# wait to handle asynchronous loaded websites
# implicit vs explicit wait functions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.manutd.com"
driver = webdriver.Chrome()
driver.get(url)

# function will throw exception after 10secs if the condition we specify is not met
wait = WebDriverWait(driver, 10)
cookies = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/button')))
cookies.click()
subscribeLater = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/a[1]')))
subscribeLater.click()
