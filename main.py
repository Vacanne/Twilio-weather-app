import requests
from twilio.rest import Client


PHONE_NUMBER = "YOUR_NUMBER_HERE"
TWILIO_NUMBER = "YOUR_TWILIO_NUMBER_HERE"
TWILIO_SID = "YOUR_SID_HERE"
API_KEY = "YOUR_API_KEY_HERE"
AUTH_TOKEN = "YOUR_TOKEN_HERE"
MY_LAT = 38.423733
MY_LONG = 27.142826
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = TWILIO_SID
auth_token = AUTH_TOKEN
api_key = API_KEY

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OMW_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for hour_data in data["list"]:
    code = hour_data["weather"][0]["id"]
    if int(code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Don't forget to bring an umbrella",
        from_=TWILIO_NUMBER,
        to=PHONE_NUMBER
    )
print(message.status)

