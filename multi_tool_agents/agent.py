"""
multi_tool_agents/agent.py
"""
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

from google.adk.agents import Agent

def get_weather(location: str) -> str:
    """Get the weather for a given location"""
    return f"The weather in {location} is sunny"

def get_news(location: str) -> str:
    """Get the news for a given location"""
    return f"The news in {location} is good"

def get_time(location: str) -> str:
    """Get the time for a given location"""
    return f"The time in {location} is 10:00"

def get_traffic(location: str) -> str:
    """Get the traffic for a given location"""
    return f"The traffic in {location} is good"


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash-exp",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "I can answer your questions about the time and weather in a city."
    ),
   tools=[get_weather, get_news, get_time, get_traffic],
)





if __name__ == "__main__":
    root_agent.run()
