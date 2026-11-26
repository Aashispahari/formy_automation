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
url = "https://formy-project.herokuapp.com/fileupload"
driver.get(url)
driver.maximize_window()
time.sleep(2)
file_upload = driver.find_element(By.ID, "file-upload-field")
file_upload.send_keys(r"D:\selenium in class\login.png")
# file_upload.send_keys(r"D:/selenium in class/login.png")
# file_upload.send_keys(r"D:\\selenium in class\\login.png")





time.sleep(2)

driver.quit()
