import requests
from datetime import datetime, timedelta

TEQ_API = "9IRv7Fy0Du6Ma-rmslFNBIBhlpugNt1U"
LOC_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/search"
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    "apikey": "9IRv7Fy0Du6Ma-rmslFNBIBhlpugNt1U",
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self, data_row):
        self.data_row = data_row

    def iata_insert(self):
        city = self.data_row["city"]
        loc_response = self.city_code_seach(city)
        self.data_row["iataCode"] = loc_response["locations"][0]["code"]
        if not self.data_row["iataCode"]:
            self.data_row["iataCode"] = "TESTING"
        return self.data_row

    def city_code_seach(self, city):
        params = {
            "accept": "application/json",
            "term": city,
            "location_types": "city",
            "active_only": "true",
        }
        response = requests.get(url=LOC_ENDPOINT, params=params, headers=HEADERS)
        return response.json()

    def search_flights(self, max=0):
        now = datetime.now()
        plus_six_months = now + timedelta(days=180)
        params = {
            "fly_from": "CLT",
            "fly_to": self.data_row["iataCode"],
            "date_from": now.strftime("%d/%m/%Y"),
            "date_to": plus_six_months.strftime("%d/%m/%Y"),
            "return_from": now.strftime("%d/%m/%Y"),
            "return_to": plus_six_months.strftime("%d/%m/%Y"),
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "max_fly_duration": "15",
            "max_stopovers": max,
            "adults": "1",
            "price_from": "0",
            "price_to": "1000",
            "curr": "USD",
            "sort": "price",
            "limit": "1",
        }
        response = requests.get(url=SEARCH_ENDPOINT, params=params, headers=HEADERS)
        # print(response.json())
        return response.json()
