from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

import requests
from bs4 import BeautifulSoup
import lxml


browser_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "upgrade-insecure-requests": "1"
}

response_form_link = 'https://docs.google.com/forms/d/e/1FAIpQLSeD-AugPwwbX90yJpr684xvTlxYHH6qtjLaaf6yVkFtO6i5Fw/viewform?usp=sf_link'
zillow_search_link = 'https://www.zillow.com/charlotte-nc/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A35.28891807253254%2C%22south%22%3A35.13801027692789%2C%22east%22%3A-80.74043553041982%2C%22west%22%3A-80.97183506655263%7D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A239330%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A1200%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%2C%22sche%22%3A%7B%22value%22%3Afalse%7D%2C%22schm%22%3A%7B%22value%22%3Afalse%7D%2C%22schh%22%3A%7B%22value%22%3Afalse%7D%2C%22schp%22%3A%7B%22value%22%3Afalse%7D%2C%22schr%22%3A%7B%22value%22%3Afalse%7D%2C%22schc%22%3A%7B%22value%22%3Afalse%7D%2C%22schu%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A24043%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A12%7D'

response = requests.get(zillow_search_link).text
soup = BeautifulSoup(response, "lxml")

print(soup)

rentals = soup.find_all(".list-card_for-rent")

print(len(rentals))
print(rentals)

