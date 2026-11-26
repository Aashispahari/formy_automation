from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
url = "https://formy-project.herokuapp.com/form"
driver.get(url)
driver.maximize_window()
wait =WebDriverWait(driver,10)

first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Aashish")
time.sleep(2)

last_name = driver.find_element(By.ID,"last-name")
last_name.send_keys("Pahari")
time.sleep(2)

job_title = driver.find_element(By.ID,"job-title")
job_title.send_keys("QA")
time.sleep(2)

driver.execute_script("window.scrollBy(0,500);")

high_scool = driver.find_element(By.ID,"radio-button-1")
high_scool.click()
time.sleep(2)

male = driver.find_element(By.ID,"checkbox-1")
male.click()
time.sleep(2)


dropdown = wait.until(EC.element_to_be_clickable((By.ID,"select-menu")))
dropdown.click()
select = Select(dropdown)
select.select_by_value("1")
time.sleep(2)
# driver.execute_script("window.scrollBy(0,300);")



date = driver.find_element(By.ID,"datepicker")
date.send_keys("11/11/2002")
time.sleep(2)

submit = driver.find_element(By.XPATH,"/html/body/div/form/div/div[8]/a")
submit.click()
time.sleep(2)

assert "thanks" in driver.current_url ,"Submission failed"
print("Form submitted sucessfully")

time.sleep(2)
driver.quit()



