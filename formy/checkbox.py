from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://formy-project.herokuapp.com/"
driver.get(url)
wait = WebDriverWait(driver,10)

# wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/li[3]/a"))).click()
# driver.find_element(By.XPATH, "/html/body/div/div/li[3]/a").click()

driver.get("https://formy-project.herokuapp.com/checkbox")
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


