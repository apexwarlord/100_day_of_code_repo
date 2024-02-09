import requests
import smtplib
import re
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = "alexzacharias01@hotmail.com"
PASSWORD = os.getenv("PASSWORD")

STOCK_SYMBOL = "TSLA"
COMPANY_NAME = "Tesla Inc"

"""ALPHAVANTAGE"""
ACCESS_KEY = "0SOOTI6FNLJ7YBZJ"
AV_ENDPOINT = "https://www.alphavantage.co/query"
FUNCTION = "TIME_SERIES_DAILY"
# ❚ Required: function ❚ Required: symbol ❚ Optional: outputsize ❚ Optional: datatype ❚ Required: apikey
AV_PARAMETERS = {
    "function": FUNCTION,
    "symbol": STOCK_SYMBOL,
    "apikey": ACCESS_KEY,
}
"""NEWS API"""
NEWS_API = "9c200b05d3c44c92ade6f78dfe5c76ce"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_PARAMETERS = {
    "apiKey": NEWS_API,
    "q": STOCK_SYMBOL,
    "language": "en",
}

def send_letter(news, move, dir):
    with smtplib.SMTP('smtp.office365.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="alexzacharias01@gmail.com",
            msg=f"Subject:{STOCK_SYMBOL} MOVES {dir} {move}%!\n\n{news}"
        )



av_response = requests.get(AV_ENDPOINT, params=AV_PARAMETERS)
av_response.raise_for_status()
av_data = av_response.json()['Time Series (Daily)']
today_yesterday = []
for item in av_data:
    if len(today_yesterday) > 1:
        break
    today_yesterday.append(float(av_data[item]["4. close"]))

yesterday_close = today_yesterday[1]
today_close = today_yesterday[0]
stock_move = round((yesterday_close - today_close) / yesterday_close * 100)

news_update = ""

direction = "🔺"
if stock_move < 0:
    direction = "🔻"
if direction == "🔺":
    direction_text = "UP"
else:
    direction_text = "DOWN"

stock_move = abs(stock_move)
if stock_move >= 4:
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = []
    for article in news_data["articles"]:
        articles.append(article)
        if len(articles) > 2:
            break
    news_update += f'{STOCK_SYMBOL}: {direction_text} {stock_move}%'
    for article in articles:
        news_update += f'\nHeadline: {article["title"]}\nBrief: {article["description"]}\n'

    news_update = re.sub(u"([‘’])", "'", news_update)
    send_letter(news_update, stock_move, direction_text)



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

