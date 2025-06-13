import requests
import os
from twilio.rest import Client
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
API_KEY = os.environ.get("WEATHER_API")
weather_params = {
    "lat":11.899391,
    "lon":75.420224,
    "appid":API_KEY,
    "cnt":4
}

res = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
data = res.json()

print(data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in data["list"]:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella ☔")
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="🌧 It's going to rain today. Remember to bring an umbrella ☔!",
        to="whatsapp:+919745179901"
    )





