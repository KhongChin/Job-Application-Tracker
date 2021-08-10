# ------------------------------------ Pixela - JOB APPLICATION SUBMITTED TRACKER ------------------------------------ #
import requests
from datetime import datetime

# ---------------------------------- Step 1: Create a Username & Token ---------------------------------- #
with open("data.txt", "r") as data:
    data_list = data.readlines()
    USERNAME = data_list[0].strip("\n")
    TOKEN = data_list[1].strip("\n")
    GRAPH_NAME = data_list[2]

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
# TOKEN = "YOUR_TOKEN"
# USERNAME = "YOUR_USERNAME"
# GRAPH_NAME = "YOUR_GRAPH_NAME"
PIXELA_PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# Commented as token and username has been created previously
# response = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_PARAMS)
# print(response.text)

# -------------------------------------- Step 2: Create a Graph -------------------------------------- #
GRAPH_PARAMS = {
    "id": GRAPH_NAME,
    "name": "Job Application Submitted Tracker",
    "unit": "quantity",
    "type": "int",
    "color": "shibafu"
}

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# Commented as graph has been created previously
# graph_response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_PARAMS, headers=HEADERS)
# print(graph_response.text)

# ------------------------------------- Step 3: Input Pixels/Data into the Graph ------------------------------------- #
today = datetime.now()
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_NAME}"
PIXEL_PARAMS = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many job applications did you submit today?\n")
}

pixel_response = requests.post(url=PIXEL_ENDPOINT, json=PIXEL_PARAMS, headers=HEADERS)
print(pixel_response.text)

# ---------------------------------------- Update Registered Pixels in Graph ---------------------------------------- #
# PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_NAME}/{today.strftime('%Y%m%d')}"
# PIXEL_UPDATE_PARAMS = {
#     "quantity": "2",
# }
#
# pixel_update_response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=PIXEL_UPDATE_PARAMS, headers=HEADERS)
# print(pixel_update_response.text)

# ---------------------------------------- Delete Registered Pixels in Graph ---------------------------------------- #
# pixel_delete_response = requests.delete(url=PIXEL_UPDATE_ENDPOINT, headers=HEADERS) # Same endpoint as pixel update
# print(pixel_delete_response.text)
