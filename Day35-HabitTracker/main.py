import requests
from datetime import *
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="token.env")

GRAPH_ID = "graph1"
TOKEN = os.getenv("TOKEN")
USERNAME = "ashaku"
pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

res = requests.post(url=pixela_endpoint, json=pixela_params)
graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
res1 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74"
}
res2 = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)

