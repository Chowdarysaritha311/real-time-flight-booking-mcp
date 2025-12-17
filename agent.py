import requests

MCP_URL = "http://localhost:8000"

def find_cheapest_flight(origin, destination):
    flights = requests.post(
        f"{MCP_URL}/search",
        params={"origin": origin, "destination": destination}
    ).json()
    return min(flights, key=lambda x: x["price"])

def book(flight_id, user):
    return requests.post(
        f"{MCP_URL}/book",
        params={"flight_id": flight_id, "user_name": user}
    ).json()

flight = find_cheapest_flight("SFO", "JFK")
booking = book(flight["id"], "Saritha")

print("Flight:", flight)
print("Booking:", booking)
