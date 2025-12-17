# AI Flight Booking Agent using MCP

This project demonstrates an AI Agent that uses Model Context Protocol (MCP)
to search and book flights using external tools.

## Features
- Search flights
- Book cheapest flight
- MCP-based tool integration
- Agent-driven workflow

## How to Run
1. Start MCP Server:
   uvicorn mcp_server.server:app --reload

2. Run Agent:
   python agent/agent.py
