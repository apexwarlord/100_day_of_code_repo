from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# chromedriver_path = "/Users/zachz/Desktop/chromedriver-mac-x64/chromedriver"
driver = webdriver.Chrome()

url = "https://www.python.org/"

driver.get(url)

event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

event_dict = {}
for i in range(len(event_names)):
    event_dict.update({i: {"date": event_times[i].text, "name": event_names[i].text}})

print(event_dict)

# driver.close() closes a tab
driver.quit()