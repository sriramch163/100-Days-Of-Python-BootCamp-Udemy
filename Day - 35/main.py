
import requests
from twilio.rest import Client

account_sid = "aaaaaaaaaaaaaaaaaaaaaaaaa" # Your Account SID from www.twilio.com/console
auth_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"  # Your Auth Token from www.twilio.com/console
api_key = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"  # Your OpenWeatherMap API Key 
OWN_ENDPOINT = ("http://api.openweathermap.org/data/2.5/forecast")
# http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=92e9e26b2ab8e36d7fac64e8a0b6b504
weather_params = {
    "lat": 15.912900,
    "lon": 79.739990,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWN_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+15551234567", # Your Twilio number
        to="+15558675310",
    )

    print(message.status)