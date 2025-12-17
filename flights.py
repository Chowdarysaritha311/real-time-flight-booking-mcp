FLIGHTS = [
    {"id": 1, "from": "SFO", "to": "JFK", "price": 300, "airline": "Delta"},
    {"id": 2, "from": "SFO", "to": "JFK", "price": 250, "airline": "United"},
    {"id": 3, "from": "SFO", "to": "JFK", "price": 280, "airline": "JetBlue"}
]

def search_flights(origin, destination):
    return [f for f in FLIGHTS if f["from"] == origin and f["to"] == destination]

def book_flight(flight_id, user_name):
    return {
        "booking_id": f"BOOK-{flight_id}-{user_name}",
        "status": "confirmed"
    }
