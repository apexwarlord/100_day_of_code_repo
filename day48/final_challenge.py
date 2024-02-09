from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

time.sleep(4)

big_cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")


def get_money():
    money = driver.find_element(By.CSS_SELECTOR, "#money")
    return int(money.text.replace(",", ""))


def buy_upgrades():
    upgrade_costs = driver.find_elements(By.CSS_SELECTOR, "#store > div > b")
    money = get_money()
    high_cost = 0
    high_index = None
    for i in range(len(upgrade_costs)):
        try:
            n = int(driver.find_elements(By.CSS_SELECTOR, "#store > div > b")[i].text.split()[-1].replace(",", ""))
        except IndexError:
            pass
        else:
            if high_cost < n < money:
                high_cost, high_index = n, i

    if high_index is not None:
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#store > div")
        upgrades[high_index].click()


# def main_loop():
#     for _ in range(10):
#         for _ in range(20):
#             big_cookie.click()
#             big_cookie.click()
#             big_cookie.click()
#             big_cookie.click()
#         buy_upgrades()

timeout = time.time() + 5
start_time = time.time()
end_time = start_time + 60
while True:
    big_cookie.click()

    current_time = time.time()
    if current_time > timeout:
        timeout += 5
        buy_upgrades()

    if current_time > end_time:
        break

duration = (time.time() - start_time) / 60
print(f"{driver.find_element(By.CSS_SELECTOR, '#cps').text}"
      f"\nTotal time elapsed: {duration:.2f} minutes")

driver.close()
