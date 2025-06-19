import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv(dotenv_path="API_keys.env")

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/a1e4f5f40fe7a70d07bfd9d8f7865e5a/flightDeals/prices"


class DataManager:

    def __init__(self):
        self._user = os.getenv("SHEETY_USRERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self.header = {"Authorization": "Bearer vsdcgfedrtgsdvhgdgsadfgfnascx"}
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url="https://api.sheety.co/a1e4f5f40fe7a70d07bfd9d8f7865e5a/flightDeals/prices",
                                headers=self.header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            headers = {
                "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}",
                "Content-Type": "application/json"
            }
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"https://api.sheety.co/a1e4f5f40fe7a70d07bfd9d8f7865e5a/flightDeals/prices/{city['id']}",
                json=new_data,
                headers=headers)


