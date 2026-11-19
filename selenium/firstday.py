#importing web driver
from selenium import webdriver 
#import time function
import time

#initialize chrome with web driver
driver = webdriver.Edge()

#to delay
time.sleep(3)

#to maximize window
driver.maximize_window()

#navigate to url
url = "https://www.google.com/"
driver.get(url)
time.sleep(2)

driver.get("https://www.mindrisers.com.np/")
#to refresh window
driver.refresh()
time.sleep(2)

#to check current url
print(f"the current url is {driver.current_url}")

#to check the title of page
print(f"The title of the page is {driver.title}")

#1step back inpage
driver.back()
time.sleep(2)

#to go 1 step forward
driver.forward()
time.sleep(2)


#to close , quit driver
driver.quit()