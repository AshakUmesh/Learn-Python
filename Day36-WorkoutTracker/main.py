import requests
from datetime import *
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="token.env")

NUTRITIONIX_API = os.getenv("NUTRITIONIX_API")

NUTRITIONIX_ID = os.getenv("NUTRITIONIX_ID")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/a1e4f5f40fe7a70d07bfd9d8f7865e5a/workoutMonitor/sheet1"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API,
}
token = os.getenv("SHEET_TOKEN")
sheet_headers = {
    "Authorization": f"Bearer {token}"
}
parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 175,
    "age": 22
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheet_headers)
    print(sheet_response.text)