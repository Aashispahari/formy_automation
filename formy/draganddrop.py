from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://formy-project.herokuapp.com/dragdrop"
driver.get(url)

time.sleep(2)

wait = WebDriverWait(driver, 10)

from selenium.webdriver.common.action_chains import ActionChains

source = driver.find_element(By.XPATH, "//*[@id='image']/img")
destination = driver.find_element(By.XPATH, "//*[@id='box']")
action = ActionChains(driver)
action.drag_and_drop(source,destination).perform()
time.sleep(2)
driver.quit

