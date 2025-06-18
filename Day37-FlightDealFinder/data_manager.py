import requests
from pprint import pprint
SHEET_ENDPOINT = "https://api.sheety.co/a1e4f5f40fe7a70d07bfd9d8f7865e5a/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.SHEETY_TOKEN = "Bearer vsdcgfedrtgsdvhgdgsadfgfnascx"
        self.sheety_headers = {
            "Authorization": f"{self.SHEETY_TOKEN}"
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT, headers= self.sheety_headers)
        spreadsheet_data = response.json()
        self.destination_data = spreadsheet_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.sheety_headers
            )
            print(response.text)