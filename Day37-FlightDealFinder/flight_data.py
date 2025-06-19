class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data: dict) -> FlightData:
    if not data or not data.get("data"):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    def parse_date(ts):
        return ts.split("T")[0] if ts else "N/A"

    cheapest = None
    lowest = float("inf")

    for f in data["data"]:
        try:
            price = float(f["price"]["grandTotal"])
        except (KeyError, ValueError):
            continue

        if price < lowest:
            lowest = price
            out_seg = f["itineraries"][0]["segments"][0]
            ret_seg = f["itineraries"][1]["segments"][0]

            cheapest = FlightData(
                price,
                out_seg["departure"]["iataCode"],
                out_seg["arrival"]["iataCode"],
                parse_date(out_seg["departure"].get("at")),
                parse_date(ret_seg["departure"].get("at")),
            )
            print(f"New lowest price to {cheapest.destination_airport}: £{lowest}")

    if cheapest is None:
        print("No valid flight offers found")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    return cheapest

