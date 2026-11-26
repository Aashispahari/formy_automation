from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://formy-project.herokuapp.com/checkbox"
driver.get(url)

Checkbox1 = driver.find_element(By.ID, "checkbox-1")
Checkbox1.click()
time.sleep(2)

Checkbox2 = driver.find_element(By.ID,"checkbox-2")
Checkbox2.click()
time.sleep(2)

Checkbox3 = driver.find_element(By.ID,"checkbox-3")
Checkbox3.click()
time.sleep(2)

driver.quit()


