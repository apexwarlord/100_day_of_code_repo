from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Alexander")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Zacharias")

email = driver.find_element(By.NAME, "email")
email.send_keys("alexzacharias01@gmail.com")
# email.send_keys(Keys.ENTER)

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()


time.sleep(15)

driver.quit()
