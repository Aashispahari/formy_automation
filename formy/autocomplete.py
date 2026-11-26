from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://formy-project.herokuapp.com"
driver.get(url)
wait = WebDriverWait(driver,10)

autocomplete = wait.until(EC.element_to_be_clickable((By.XPATH ,"/html/body/div/div/li[1]/a")))
autocomplete.click()
time.sleep(2)

Address = driver.find_element(By.ID, "autocomplete")
Address.send_keys("Pokhara")

Street_address = driver.find_element(By.ID, "street_number")
Street_address.send_keys("Damside 404")

Street_address2 = driver.find_element(By.ID, "route")
Street_address2.send_keys("Amarshing")

city = driver.find_element(By.ID, "locality")
city.send_keys("Samakhusi")

State = driver.find_element(By.ID, "administrative_area_level_1")
State.send_keys("Gandaki")

Zipcode = driver.find_element(By.ID, "postal_code")
Zipcode.send_keys("40001")

country = driver.find_element(By.ID, "country")
country.send_keys("Nepal")
time.sleep(3)


driver.quit()