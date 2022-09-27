from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source = driver.find_element("xpath", '/html/body/div[3]/div[2]/div/div[14]')
destination = driver.find_element("xpath", '/html/body/div[3]/div[3]/div[2]')

# actionchains extends selenium by allowing more complex tasks like drag and drop
# methods called on actionchains obj, actions are stored in a queue
# perform fires the events in the order they were queued
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()