from pprint import pprint

import requests
import os
from dotenv import load_dotenv
import smtplib
from datetime import datetime

from data_manager import DataManager
from flight_search import FlightSearch


# This file will need to use the DataManager,Ffrom pprint import pprintlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

load_dotenv()

MY_EMAIL = "alexzacharias01@hotmail.com"
PASSWORD = os.getenv("PASSWORD")

"""SHEETY"""
SHEETY_ENDPOINT = "https://api.sheety.co/"
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_GET_POST = f"{SHEETY_ENDPOINT}{SHEETY_USERNAME}/flightDeals/prices"

response = requests.get(url=SHEETY_GET_POST)
sheet_data = response.json()["prices"]

sheet_data_searched = []
for row in sheet_data:
    flight_search = FlightSearch(row)
    new_row = flight_search.iata_insert()
    sheet_data_searched.append(new_row)

pprint(sheet_data_searched)

sheet_data_searched = sheet_data

final_data = []

data_manager = DataManager(sheet_data_searched)
data_manager.put_data(SHEETY_GET_POST)
for row in sheet_data_searched:
    flight_search = FlightSearch(row)
    new_row = flight_search.search_flights()
    try:
        test = new_row["data"][0]
    except IndexError:
        new_row = flight_search.search_flights(max=1)
        try:
            test = new_row["data"][0]
        except IndexError:
            continue
    final_data.append(new_row)

alert_details = []
for data in final_data:
    print(data)
    # print(data)
    # print(sheet_data_searched)

    if data["data"][0]["price"] < sheet_data_searched[final_data.index(data)]["lowestPrice"]:
        alert_details.append(data["data"][0])
        print(data["data"][0])


response = requests.get("https://api.sheety.co/39c09421760e3a0abbabb5310e7efde1/flightDeals/users")
data = response.json()
for user in data:

    for alert in alert_details:
        Price = alert["price"]
        Departure_City_Name = alert["cityFrom"]
        Departure_Airport_IATA_Code = alert["flyFrom"]
        Arrival_City_Name = alert["cityTo"]
        Arrival_Airport_IATA_Code = alert["flyTo"]
        Outbound_Date = str(datetime.fromtimestamp(alert["route"][0]["dTime"])).split()
        Inbound_Date = str(datetime.fromtimestamp(alert["route"][1]["dTime"])).split()
        print(f"Subject:Flight deal alert for {Arrival_City_Name}!\n\nLow price alert! Only ${Price} to fly from {Departure_City_Name}-{Departure_Airport_IATA_Code} to {Arrival_City_Name}-{Arrival_Airport_IATA_Code},"
              f"from {Outbound_Date[0]} to {Inbound_Date[0]}")


        # with smtplib.SMTP('smtp.office365.com') as connection:
        #     connection.starttls()
        #     connection.login(user=MY_EMAIL, password=PASSWORD)
        #     connection.sendmail(
        #         from_addr=MY_EMAIL,
        #         to_addrs="alexzacharias01@gmail.com",
        #         msg=f"Subject:Flight deal alert for {Arrival_City_Name}!\n\nLow price alert! Only ${Price} to fly from {Departure_City_Name}-{Departure_Airport_IATA_Code} to {Arrival_City_Name}-{Arrival_Airport_IATA_Code},"
        #             f"from {Outbound_Date[0]} to {Inbound_Date[0]}"
        #     )
