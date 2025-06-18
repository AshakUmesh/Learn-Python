import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import *
import os
from notification_manager import NotificationManager
from dotenv import load_dotenv
load_dotenv(dotenv_path="token.env")

ORIGIN_CITY_IATA = "LON"
AMADEUS_API_KEY = "TNKaouYxySccuK9M2oWdcNkYohVyyPAA"
AMADEUS_API_SECRET = "u4BqMs5bBkLtGh8e"

sheety = DataManager()
sheet_data = sheety.get_destination_data()
print(sheet_data)
flight_search = FlightSearch()


if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n{sheet_data}")

    sheety.destination_data = sheet_data
    sheety.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))




for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    cheapest_flight = FlightData.find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    time.sleep(2)


