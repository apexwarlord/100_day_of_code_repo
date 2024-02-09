import smtplib
import time
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

MY_LAT = 38.396719
MY_LONG = 22.367714

MY_EMAIL = "alexzacharias01@hotmail.com"
PASSWORD = os.getenv("PASSWORD")

iss_latitude = None
iss_longitude = None
current_time = None


def iss_overhead():
    global iss_latitude, iss_longitude
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT + 5 > iss_latitude > MY_LAT - 5 and MY_LONG + 5 > iss_longitude > MY_LONG - 5:
        return True


def is_night():
    global current_time
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
        'tzId': 'Europe/Athens',
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour < sunrise or time_now.hour > sunset:
        current_time = time_now.time()
        return True


while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        print("Sending email...")
        with smtplib.SMTP('smtp.office365.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="alexzacharias01@gmail.com",
                msg=f"Subject:The ISS is overhead!\n\nLook up into the night sky and see if you can find the ISS."
                    f"It was at {iss_latitude}N and {iss_longitude}E at {current_time}")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.

# BONUS: run the code every 60 seconds.
