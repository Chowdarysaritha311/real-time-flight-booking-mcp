from fastapi import FastAPI
from mcp_server.tools import search_flights_tool, book_flight_tool

app = FastAPI()

@app.post("/search")
def search(origin: str, destination: str):
    return search_flights_tool(origin, destination)

@app.post("/book")
def book(flight_id: int, user_name: str):
    return book_flight_tool(flight_id, user_name)
