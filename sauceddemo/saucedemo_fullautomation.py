from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
url = "https://www.saucedemo.com/"
driver.get(url)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
login_button =wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

username.send_keys("standard_user")
time.sleep(2)

password.send_keys("secret_sauce")
time.sleep(2)

action.click(login_button).perform()
time.sleep(2)

dropdown = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='header_container']/div[2]/div/span/select")))
dropdown.click()
select = Select(dropdown)
select.select_by_value("lohi")
time.sleep(2)

bike = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
action.click(bike).perform
time.sleep(2)

driver.execute_script("window.scrollBy(0,400);")

bagpack = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
action.click(bagpack).perform()
time.sleep(2)


cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a")))
action.click(cart).perform()
time.sleep(2)

driver.execute_script("window.scrollBy(0,400);")

checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
checkout.click()
time.sleep(2)

firstname = wait.until(EC.visibility_of_element_located((By.ID,"first-name")))
firstname.send_keys("Nisha")
time.sleep(2)

action.key_down(Keys.CONTROL).perform()
action.send_keys("a")
action.key_up(Keys.CONTROL).perform()
time.sleep(2)

action.key_down(Keys.CONTROL).perform()
action.send_keys("c")
action.key_up(Keys.CONTROL).perform
time.sleep(2)

# action.send_keys(Keys.CONTROL + "a").perform()

action.send_keys(Keys.TAB).perform()
time.sleep(2)

action.key_down(Keys.CONTROL).perform()
action.send_keys("v")
action.key_up(Keys.CONTROL).perform()
time.sleep(2)
# lastname = wait.until(EC.visibility_of_element_located((By.ID,"last-name")))


action.send_keys(Keys.TAB)

zipcode = wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))
zipcode.send_keys("4001")
time.sleep(2)

driver.execute_script("window.scrollBy(0,300);")
time.sleep(2)

continue_button = wait.until(EC.element_to_be_clickable((By.ID,"continue")))
continue_button.click()
time.sleep(2)



driver.execute_script("window.scrollTo(0,0)")
time.sleep(2)

driver.execute_script("window.scrollBy(0,500);")
time.sleep(2)

details = driver.find_element(By.XPATH,"//*[@id='checkout_summary_container']/div/div[2]")
details.screenshot("Product_details.png")
time.sleep(2)

finish = wait.until(EC.element_to_be_clickable((By.ID,"finish")))
finish.click()
time.sleep(2)

assert "checkout-complete" in driver.current_url,"Checkout failed"
print(f"Thankyou for your purchase!!!. Visit Again ;) ")

finishh = wait.until(EC.element_to_be_clickable((By.ID,"back-to-products")))
action.click(finishh).perform()

driver.execute_script("window.scrollBy(0,500);")
time.sleep(2)

driver.execute_script("window.scrollTo(0,0)")
time.sleep(2)

wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn"))).click()
time.sleep(2)

wait.until(EC.element_to_be_clickable((By.ID,"dynamic_catalog_sidebar_link"))).click()
time.sleep(2)

wait.until(EC.element_to_be_clickable((By.ID,"dynamic_catalog_spinner_link"))).click()
time.sleep(2)

wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn"))).click()
time.sleep(2)

wait.until(EC.element_to_be_clickable((By.ID,"dynamic_catalog_sidebar_link"))).click()
time.sleep(2)

wait.until(EC.element_to_be_clickable((By.ID,"dynamic_catalog_slider_link"))).click()
time.sleep(2)

wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn"))).click()
time.sleep(2)

wait.until(EC.element_to_be_clickable((By.ID,"inventory_sidebar_link"))).click()
time.sleep(2)

wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn"))).click()
time.sleep(2)

wait.until(EC.element_to_be_clickable((By.ID,"logout_sidebar_link"))).click()
time.sleep(2)

driver.quit()
