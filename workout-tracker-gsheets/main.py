import requests
from datetime import datetime
import os

USER_INFO = {
    "weight_kg": 58,
    "height_cm": 165,
    "age": 26,
    "gender": "male"
}

API_HEADER = {
    "x-app-id": os.environ.get("API_ID"),
    "x-app-key": os.environ.get("API_KEY")
}

BASE_URL = "https://app.100daysofpython.dev"
workout_post_endpoint = BASE_URL + "/v1/nutrition/natural/exercise"

user_input = str(input("What exercises you did today?: "))

workout_post_params = {
    "query": user_input,
    "weight_kg": USER_INFO["weight_kg"],
    "height_cm": USER_INFO["height_cm"],
    "age": USER_INFO["age"],
    "gender": USER_INFO["gender"]
}

print(API_HEADER)

r_workout = requests.post(workout_post_endpoint, json=workout_post_params, headers=API_HEADER)
workout_data = r_workout.json()["exercises"]
# print(workout_data)

today = datetime.now()
# print(today.strftime("%m/%d/%Y"))
sheety_post_endpoint = "https://api.sheety.co/93697e62e046e8072155653409168db3/workoutTracking/workouts"

SHEETY_HEADER = {
    "Authorization": f"Bearer {os.environ.get("SHEETY_TOKEN")}",
}

for exercise in workout_data:
    sheety_post_params = {
        "workout": {
            "date": today.strftime("%m/%d/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    r_log = requests.post(sheety_post_endpoint, json=sheety_post_params, headers=SHEETY_HEADER)
    print(r_log.text)
