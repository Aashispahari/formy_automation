#windows handel

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
url = "https://formy-project.herokuapp.com/switch-window"
driver.get(url)
driver.maximize_window()
time.sleep(2)

switch_window = driver.find_element(By.ID ,"new-tab-button")
switch_window.click()
time.sleep(2)
#window handeling
print(driver.window_handles)
windows = driver.window_handles

#shows current window
print(driver.current_window_handle)

#switch handels
driver.switch_to.window(windows[1])
#or
#driver.switch_to.window(driver.window_handels[1])
driver.find_element(By.XPATH ,"/html/body/div/div/li[1]/a").click()

# print(driver.current_window_handle)
time.sleep(2)

driver.quit()
