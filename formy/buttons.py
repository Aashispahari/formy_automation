from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
url ="https://formy-project.herokuapp.com/buttons"
driver.get(url)
driver.maximize_window()

try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/form/div[1]/div/div/button[1]"))).click()
    print("Primary button Clicked")

except TimeoutException:
    print("Button not clicked")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/form/div[1]/div/div/button[2]"))).click()
    print("Sucess button Clicked")

except TimeoutException:
    print("Button not clicked")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/form/div[1]/div/div/button[3]"))).click()
    print("Info button Clicked")

except TimeoutException:
    print("Button not clicked")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/form/div[1]/div/div/button[4]"))).click()
    print("Waring button Clicked")

except TimeoutException:
    print("Button not clicked")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/form/div[1]/div/div/button[5]"))).click()
    print("Danzer button Clicked")

except TimeoutException:
    print("Button not clicked")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/form/div[1]/div/div/button[6]"))).click()
    print("Link  Clicked")

except TimeoutException:
    print("Button not clicked")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/form/div[2]/div/div/div/button[1]"))).click()
    print("left button Clicked")

except TimeoutException:
    print("left Button not clicked")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/form/div[2]/div/div/div/button[2]"))).click()
    print("Middle button Clicked")

except TimeoutException:
    print("Middle Button not clicked")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/form/div[2]/div/div/div/button[3]"))).click()
    print("Right button Clicked")

except TimeoutException:
    print("Right Button not clicked")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/form/div[3]/div/div/div/button[1]"))).click()
    print("1 button Clicked")

except TimeoutException:
    print("1 Button not clicked")

try:
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/form/div[3]/div/div/div/button[2]"))).click()
    print("2 button Clicked")

except TimeoutException:
    print("2 Button not clicked")

try:
    dropdown = wait.until(EC.element_to_be_clickable((By.ID,"btnGroupDrop1")))
    dropdown.click()
    print("dropdown menu Clicked")

except TimeoutException:
    print("Button not clicked")


driver.quit()