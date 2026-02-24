import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv(override=True)

BASE_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
WEATHER_API = os.getenv("WEATHER_API")
QC_LOC = (14.676041, 121.043701)
RAIN_LOC = (13.900343, 121.988602)

params_weather = {
    "lat": RAIN_LOC[0],
    "lon": RAIN_LOC[1],
    "appid": WEATHER_API,
    "cnt": 4,
}

r = requests.get(BASE_ENDPOINT, params=params_weather)
r.raise_for_status()
weather_data = r.json()
# print(weather_data)

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


def check_if_rain():
    for hour in weather_data["list"]:
        weather_id = hour["weather"][0]["id"]
        if weather_id <= 600:
            return True
    return False

if check_if_rain():
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It is possible to rain later today. Remember to bring an umbrella.☔",
        from_="+12202091923",
        to="+18777804236",
    )
    print(message.status)