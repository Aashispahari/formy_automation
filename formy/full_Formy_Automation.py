from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
import time

driver = webdriver.Chrome()
url = "https://formy-project.herokuapp.com/"
driver.get(url)
driver.maximize_window()
wait = WebDriverWait(driver,10)
time.sleep(2)

#for Autocomplete form
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

print("Autocomplete Form Completed")

#Back to Main page
wait.until(EC.element_to_be_clickable((By.ID,"logo"))).click()
time.sleep(2)

#For button field
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/li[2]/a"))).click()

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


wait.until(EC.element_to_be_clickable((By.ID,"logo"))).click()

#For Checkbox
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/li[3]/a"))).click()
# wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/li[2]/a"))).click()
driver.get("https://formy-project.herokuapp.com/checkbox")

Checkbox1 = driver.find_element(By.ID,"checkbox-1")
Checkbox1.click()
time.sleep(2)

Checkbox2 = driver.find_element(By.ID,"checkbox-2")
Checkbox2.click()
time.sleep(2)

Checkbox3 = driver.find_element(By.ID,"checkbox-3")
Checkbox3.click()
time.sleep(2)

print("Checkbox Completed")

wait.until(EC.element_to_be_clickable((By.ID,"logo"))).click()

# wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/li[5]/a"))).click()

driver.get("https://formy-project.herokuapp.com/dragdrop")
source = driver.find_element(By.XPATH, "//*[@id='image']/img")
destination = driver.find_element(By.XPATH, "//*[@id='box']")
action = ActionChains(driver)
action.drag_and_drop(source,destination).perform()
time.sleep(2)
print("Drag and drop completed")

wait.until(EC.element_to_be_clickable((By.ID,"logo"))).click()
driver.execute_script("window.scrollBy(0,700);")

# wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/li[7]/a"))).click()

driver.get("https://formy-project.herokuapp.com/enabled")
print("For Enabled and Disabled button")

try:
    disabled = wait.until(EC.element_to_be_clickable((By.ID, "disabledInput")))
    disabled.send_keys("hello")
    print("The button is clickable")

except TimeoutException :
    print("Fail :the input field 1 is not clickable")

except ElementClickInterceptedException:
    print("Fail :another element is blocking the button")


time.sleep(2)

try:
    enabled =wait.until(EC.element_to_be_clickable((By.ID,"input")))
    enabled.send_keys("Pass")
    print("field 2 is enabled")

except TimeoutException:
    print("fail:element is not clickable")

wait.until(EC.element_to_be_clickable((By.ID,"logo"))).click()
time.sleep(2)
# wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/li[8]/a"))).click()
driver.get("https://formy-project.herokuapp.com/fileupload")

file_upload = driver.find_element(By.ID, "file-upload-field")
file_upload.send_keys(r"D:\selenium in class\login.png")
print("Field upload successfull")
time.sleep(2)

wait.until(EC.element_to_be_clickable((By.ID,"logo"))).click()
# wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/li[10]/a"))).click()
driver.get("https://formy-project.herokuapp.com/modal")

model_button = wait.until(EC.element_to_be_clickable((By.ID,"modal-button")))
action.click(model_button).perform()

ok_button = wait.until(EC.element_to_be_clickable((By.ID,"ok-button")))
action.click(ok_button).perform()

print("Sucessfully tested modal")

#for Scrollpage
# wait.until(EC.element_to_be_clickable((By.ID,"logo"))).click()
# wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/li[11]/a"))).click()
driver.get("https://formy-project.herokuapp.com/scroll")

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


#for web form
wait.until(EC.element_to_be_clickable((By.ID,"logo"))).click()
driver.get("https://formy-project.herokuapp.com/form")

# wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/li[14]/a"))).click()

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


print("THE END .....")

driver.quit()

