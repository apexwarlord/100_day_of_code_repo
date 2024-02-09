import requests
from datetime import datetime

MY_LAT = 38.396719
MY_LONG = 22.367714


parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
    'tzId': 'Europe/Athens',
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

current_time = datetime.now()
print(current_time)
print(current_time.time())
