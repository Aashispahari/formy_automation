#to scroll page

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
url = "https://formy-project.herokuapp.com/scroll"
driver.get(url)
driver.maximize_window()
time.sleep(2)
# content = driver.find_element(By.TAG_NAME,"body")
# content.send_keys(Keys.END)
# time.sleep(2)
action = ActionChains(driver)


#for scroll 
driver.execute_script("window.scrollBy(0,700);")
username = driver.find_element(By.ID, "name")
username.send_keys("Aashish")
time.sleep(2)

action.send_keys(Keys.TAB)
action.send_keys("11/11/2002")
action.perform()


# date = driver.find_element(By.ID, "date")
# date.send_keys("12/12/4444")
driver.execute_script("window.scrollTo(0,0);")
time.sleep(2)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

time.sleep(2)
driver.quit()