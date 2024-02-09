import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

"""SHEETY"""
SHEETY_ENDPOINT = "https://api.sheety.co/"
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_POST = f"{SHEETY_ENDPOINT}{SHEETY_USERNAME}/myWorkouts/workouts"
SHEETY_AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")

SHEETY_HEADERS = {
    "Authorization": f"Basic {SHEETY_AUTH_TOKEN}"
}


"""NUTRITIONIX"""
GENDER = "male"
WEIGHT_KG = "76"
HEIGHT_CM = "170"
AGE = "32"

# NUTRITIONIX_API = "9c200b05d3c44c92ade6f78dfe5c76ce"
APP_ID = os.getenv("APP_ID")  # "6f838b9a"
APP_KEY = os.getenv("APP_KEY")  # "30e5b7913f24d716b7be5fff39c09dc5"

ENDPOINT_BASE = "https://trackapi.nutritionix.com/"
EXERCISE_ENDPOINT = f"{ENDPOINT_BASE}/v2/natural/exercise"

user_exercise = input("Tell me which exercises you did: ")
try:
    how_long_ago = int(input("how many hours ago? "))
    how_long_ago = 6 if how_long_ago > 6 else how_long_ago
except ValueError:
    how_long_ago = 0

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

EXERCISE_QUERY = {
    "query": user_exercise,
    "age": AGE,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "gender": GENDER,
}
current_date = datetime.now()
date = current_date.strftime("%d/%m/%Y")
time = f"{(int(current_date.strftime('%H'))-how_long_ago):02d}:{(round(int(current_date.strftime('%M'))/5)*5):02d}"
response = requests.post(url=EXERCISE_ENDPOINT, json=EXERCISE_QUERY, headers=HEADERS)
data = response.json()
upload_data = []
for exercise in data['exercises']:
    upload_data.append({"name": exercise['name'], "duration": exercise['duration_min'], "calories": exercise['nf_calories']})

for exercise in upload_data:
    exercise_json = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration'],
            "calories": exercise['calories']

        }
    }
    response = requests.post(url=SHEETY_POST, json=exercise_json, headers=SHEETY_HEADERS)
    print(response)
