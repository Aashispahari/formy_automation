from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
action =ActionChains(driver)
url = "https://formy-project.herokuapp.com/modal"
driver.get(url)
driver.maximize_window()
model_button = wait.until(EC.element_to_be_clickable((By.ID,"modal-button")))
action.click(model_button).perform()

ok_button = wait.until(EC.element_to_be_clickable((By.ID,"ok-button")))
action.click(ok_button).perform()


time.sleep(2)
driver.quit()