from mcp_server.mock_api.flights import search_flights, book_flight


def search_flights_tool(origin: str, destination: str):
    """
    MCP Tool: Search flights between two locations
    """
    return search_flights(origin, destination)


def book_flight_tool(flight_id: int, user_name: str):
    """
    MCP Tool: Book a flight for a user
    """
    return book_flight(flight_id, user_name)
