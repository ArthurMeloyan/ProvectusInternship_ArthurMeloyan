import os
import requests
from dotenv import load_dotenv


load_dotenv()

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

assert SERPAPI_API_KEY, 'SerpAPI key not set in .env'

def search_concerts(artist_name: str) -> str:
    params = {
        "engine": "google",
        "q": f"{artist_name} upcoming concerts",
        "api_key": SERPAPI_API_KEY,
        "hl": "en",
        "gl": "us"
    }


    url = "https://serpapi.com/search"

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        events = data.get("events", [])

        if not events:
            return f"No upcoming concerts found for {artist_name}"
        
        result_lines = [f"Upcoming concerts for {artist_name}:"]

        for event in events[:3]:
            title = event.get("title")
            date = event.get("date")
            location = event.get("location")
            result_lines.append(f' - {title} on {date} at {location}')

        return "\n".join(result_lines)
    except Exception as e:
        return f"Error during concert search: {str(e)}"
    
