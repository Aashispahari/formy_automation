from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
import time

driver = webdriver.Chrome()
url = "https://demoqa.com/frames"
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollBy(0,300);")
time.sleep(2)
frame2= driver.find_element(By.ID, "frame2")
driver.switch_to.frame(frame2)
driver.execute_script("window.scrollBy(50,50);")
time.sleep(3)

driver.switch_to.default_content()
driver.execute_script("window.scrollBy(0,-300)")
time.sleep(2)
driver.quit()

