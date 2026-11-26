from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

import time


driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
url = "https://formy-project.herokuapp.com/enabled"
driver.get(url)
driver.maximize_window()
time.sleep(2)

try:
    disabled = wait.until(EC.element_to_be_clickable((By.ID, "disabledInput")))
    disabled.send_keys("hello")
    print("The button is clickable")

except TimeoutException :
    print("Fail :the input field is not clickable")

except ElementClickInterceptedException:
    print("Fail :another element is blocking the button")


time.sleep(2)

try:
    enabled =wait.until(EC.element_to_be_clickable((By.ID,"input")))
    enabled.send_keys("Pass")
    print("field is enabled")

except TimeoutException:
    print("fail:element is not clickable")

time.sleep(2)
driver.quit()



