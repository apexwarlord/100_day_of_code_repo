from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(url)

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount").text

print(article_count.split()[0])

driver.quit()