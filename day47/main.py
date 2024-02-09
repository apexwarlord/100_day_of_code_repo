import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = "alexzacharias01@hotmail.com"
PASSWORD = os.getenv("PASSWORD")

browser_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
url = ("https://www.amazon.com/Logitech-Wireless-Headset-Black-Tico/dp/B08141GQQG/ref=sr_1_3?crid=21EFFS7Y1LPI3&dib=ey"
       "J2IjoiMSJ9.izWiBwi1PvaXD0BcJzhXxzWWVkYMSoIVapVL3gUS0Wna3VA61Te9driTGJJDRwPyGEaD5-TZLQMqbtbhiaebxKcqO_jfkIjuFxz"
       "WCfQ1rxpRLpaNuh5i9gpQRNi2P4V0WOHV1H9FweQCj0sPR1VH6SfwHyxJnz31NEqdFMTp0dFcIKu0MSadNn9DBxzCkOWY4SI7C42bgQKdqNu09"
       "3yGrVXLK_7a4Q7G-JLrpXesPpk.wYlm4ie4nx0wOcClwt0ri_SNXfYrgUD9T2_2An6-4f8&dib_tag=se&keywords=logitech%2Bwireless"
       "%2Bheadset&qid=1705766719&sprefix=logitech%2Bwireless%2Bheadse%2Caps%2C315&sr=8-3&th=1")


request = requests.get(url, headers=browser_headers)

soup = BeautifulSoup(request.text, "lxml")

title = soup.find("span", id="productTitle").getText().strip()
price = float((soup.find("span", class_="a-offscreen").getText())[1:])


if price < 110:
    with smtplib.SMTP('smtp.office365.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="alexzacharias01@gmail.com",
            msg=f"Subject: Amazon Price Alert!\n\n{title} now ${price}!\n\n{url}".encode("utf-8")
        )
