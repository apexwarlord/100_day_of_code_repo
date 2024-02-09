from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_EMAIL = "alexzacharias01@gmail.com"
ACCOUNT_PASSWORD = os.getenv("PASSWORD")
driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3690886553&f_SB2=1&geoId=102264677&keywords=drinking%20"
           "water&location=Charlotte%2C%20North%20Carolina%2C%20United%20States&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&r"
           "efresh=true")

time.sleep(2)

sign_in = driver.find_element(By.CSS_SELECTOR,
                              "a[class='cta-modal__primary-btn btn-md btn-primary inline-block w-full mt-3']")
sign_in.click()

time.sleep(3)

username_field = driver.find_element(By.CSS_SELECTOR, "#username")
password_field = driver.find_element(By.CSS_SELECTOR, "#password")
username_field.send_keys(ACCOUNT_EMAIL)
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(3)

jobs = driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results-list a')

for job in jobs:
    job.click()

    time.sleep(1)

    try:
        save_button = driver.find_element(By.CSS_SELECTOR, 'button[class="jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary"]')
        if save_button.text[:5] != "Saved":
            save_button.click()
            time.sleep(2)
            pop_up_x = driver.find_element(By.CSS_SELECTOR, 'button')
            pop_up_x.click()

    except NoSuchElementException:
        pass

    time.sleep(1)



driver.quit()