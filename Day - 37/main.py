import requests
from datetime import datetime

TOKEN = "your_token_here"
USER = "your_username_here"
GRAPH_ID = "coding-graph"
GRAPH_NAME = "Coding Graph"

today = datetime(year=2025, month=11, day=30)
LIVE_DATE = today.strftime("%Y%m%d")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_ENDPOINT_GRAPHS = f"{PIXELA_ENDPOINT}/{USER}/graphs"
PIXELA_ENDPOINT_POST = f"{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}"
PIXELA_ENDPOINT_PUT = f"{PIXELA_ENDPOINT_POST}/{LIVE_DATE}"
PIXELA_ENDPOINT_DELETE = f"{PIXELA_ENDPOINT_POST}/{LIVE_DATE}"

# ---------------- USER CREATION ---------------- #
user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# ---------------- GRAPH CREATION ---------------- #
graph_params = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}

headers = { "X-USER-TOKEN": TOKEN }

# graph_response = requests.post(url=PIXELA_ENDPOINT_GRAPHS, json=graph_params, headers=headers)
# print(graph_response.text)

# ---------------- POST PIXEL ---------------- #
pixel_data = {
    "date": LIVE_DATE,
    "quantity": "5"
}

# pixel_response = requests.post(url=PIXELA_ENDPOINT_POST, json=pixel_data, headers=headers)
# print(pixel_response.text)

# ---------------- UPDATE PIXEL ---------------- #
put_params = {"quantity": "500"}
# put_response = requests.put(url=PIXELA_ENDPOINT_PUT, json=put_params, headers=headers)
# print(put_response.text)

# ---------------- DELETE PIXEL ---------------- #
delete_response = requests.delete(url=PIXELA_ENDPOINT_DELETE, headers=headers)
print(delete_response.text)
