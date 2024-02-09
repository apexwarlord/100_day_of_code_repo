import requests
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC52bf63b025b926822638d02c0ed24ac0'
auth_token = '1dcae5dd5a4212321d94ec3e21e33abe'

API_KEY = "a642ac8d064e27b340bee6212b39d1bb"
PARAMETERS = {
    'lat': '60',  # '38.4',
    'lon': '10.5',  # '22.4',
    'appid': API_KEY,
}

response = requests.get(url='http://api.openweathermap.org/data/2.5/forecast', params=PARAMETERS)
print(response.status_code)
response.raise_for_status()
data = response.json()["list"][0:5]
weather_codes = []
weather_details = ""
for list_item in data:
    for i in range(len(list_item["weather"])):
        weather_codes.append(list_item["weather"][i]["id"])
        weather_details += f"{list_item['dt_txt']} : {list_item['weather'][i]}\n"

umbrella_needed = False
for code in weather_codes:
    if code < 800 and code != 500 and code != 300:
        umbrella_needed = True

if umbrella_needed:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="🌧️☔️🌧",
        from_='+12058511865',
        to='+17049152436'
    )

    print(message.status)

# http://api.openweathermap.org/data/2.5/forecast?lat=38.4&lon=22.4&appid=a642ac8d064e27b340bee6212b39d1bb
