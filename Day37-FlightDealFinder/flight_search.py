import requests
from datetime import datetime
import os
from dotenv import load_dotenv

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    def __init__(self):
        self.amadeus_api_key = "TNKaouYxySccuK9M2oWdcNkYohVyyPAA"
        self.amadeus_api_secret = "u4BqMs5bBkLtGh8e"
        self.token = self.get_new_token()

    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.amadeus_api_key,
            'client_secret': self.amadeus_api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_destination_code(self, city_name):
        print(f"Using this token to get destination {self.token}")
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {
            "keyword": city_name,
            "subType": "CITY,AIRPORT",
            "page[limit]": 2
        }
        response = requests.get(
            url="https://test.api.amadeus.com/v1/reference-data/locations",
            headers=headers,
            params=params
        )

        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            return response.json()["data"][0]['iataCode']
        except (IndexError, KeyError):
            print(f"No IATA code found for {city_name}.")
            return "N/A"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": "Bearer fdgfsdbfdsgfdgdfgfdgdfgfdgdfvbbb"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url="https://test.api.amadeus.com/v2/shopping/flight-offers",
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()

