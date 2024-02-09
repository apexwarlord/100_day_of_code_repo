from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import os
from dotenv import load_dotenv

load_dotenv()


PROMISED_UP = 10
PROMISED_DOWN = 100
TWITTER_USERNAME = "Talresious"
PASSWORD = os.getenv("PASSWORD")
SPEED_TEST_WEBSITE = 'https://www.speedtest.net/'
SPECTRUM_TWITTER = '@Ask_Spectrum'
ANGRY_TWEET = "Spectrum, I am signed up for {DOWN} mb/s down and {UP} mb/s up, however in my latest hardwire test I am only recieving {REALDOWN} mb/s down and {REALUP} mb/s up. Please advise."


class InternetSpeedTwitter:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_WEBSITE)
        time.sleep(6)
        start_test = self.driver.find_element(By.CSS_SELECTOR, 'span[class="start-text"]')
        start_test.click()
        time.sleep(120)

        self.up = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div'
                                                     '/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                                       'div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(self.up, self.down)

    def tweet_at_provider(self):

        try:
            self.up = float(self.up.strip())
            self.down = float(self.down.strip())
        except ValueError or TypeError:
            sys.exit("Error retrieving up/down values")

        if self.down >= (PROMISED_DOWN-5):
            sys.exit("Provider speed satisfactory!")

        self.driver.get("https://twitter.com/")
        time.sleep(3)
        sign_in = self.driver.find_element(By.XPATH,
                                           '/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span')
        sign_in.click()
        time.sleep(3)
        username = self.driver.find_element(By.XPATH,
                                            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)
        time.sleep(3)
        password = self.driver.find_element(By.XPATH,
                                            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(18)

        tweet_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/a')
        tweet_box.click()
        time.sleep(3)
        tweet_popup = self.driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_popup.send_keys(
            ANGRY_TWEET.format(UP=PROMISED_UP, DOWN=PROMISED_DOWN, REALUP=self.up, REALDOWN=self.down))

        post_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]')
        post_button.click()

        time.sleep(10)




ist = InternetSpeedTwitter()

ist.get_internet_speed()

ist.tweet_at_provider()

ist.driver.close()
