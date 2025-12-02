import requests
from datetime import datetime



GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 183
AGE = 21

API_KEY = "your_api_key_here" # Replace with your actual API key
APP_ID = "your_app_id_here" # Replace with your actual App ID   
USER_NAME = "your_username_here" # Replace with your actual username
USER_PASSWD = "your_password_here" # Replace with your actual password
USER_TOKEN = "your_user_token_here" # Replace with your actual user token

EXERCISE_URL = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/your_project/workouts" # Replace with your actual Sheety endpoint
EXERCISE_TEXT = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

app_params = {
    "query": EXERCISE_TEXT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

app_response = requests.post(EXERCISE_URL, json=app_params, headers=headers)
# print("STATUS:", app_response.status_code)
# print("RESPONSE TEXT:", app_response.text)
result = app_response.json()
# print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        SHEET_ENDPOINT,
        json=sheet_inputs,
        auth=(
            USER_NAME,
            USER_PASSWD,
        )
    )


    print(sheet_response.text)