import requests
from twilio.rest import Client

# Your personal phone number
PHONE_NUMBER = "YOUR_NUMBER_HERE"
# Your Twilio phone number
TWILIO_NUMBER = "YOUR_TWILIO_NUMBER_HERE"
# Your Twilio Account SID
TWILIO_SID = "YOUR_SID_HERE"
# Your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY_HERE"
# Your Twilio Auth Token
AUTH_TOKEN = "YOUR_TOKEN_HERE"
# Latitude for the location you want to check the weather for
MY_LAT = 38.423733
# Longitude for the location you want to check the weather for
MY_LONG = 27.142826
# Endpoint for the OpenWeatherMap API
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# Twilio account SID
account_sid = TWILIO_SID
# Twilio auth token
auth_token = AUTH_TOKEN
# OpenWeatherMap API key
api_key = API_KEY

# Parameters for the API request
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4  # Number of forecast data points to retrieve
}

# Send a request to the OpenWeatherMap API
response = requests.get(OMW_Endpoint, params=parameters)
# Raise an exception if there is an error with the request
response.raise_for_status()
# Parse the JSON response
data = response.json()

# Initialize a variable to determine if it will rain
will_rain = False
# Loop through each forecast data point
for hour_data in data["list"]:
    # Get the weather condition code
    code = hour_data["weather"][0]["id"]
    # Check if the weather condition code indicates rain (codes less than 700)
    if int(code) < 700:
        will_rain = True

# If it will rain, send a text message
if will_rain:
    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # Send a text message
    message = client.messages.create(
        body="Don't forget to bring an umbrella",  # Message body
        from_=TWILIO_NUMBER,  # Twilio phone number
        to=PHONE_NUMBER  # Your personal phone number
    )

# Print the status of the message
print(message.status)
