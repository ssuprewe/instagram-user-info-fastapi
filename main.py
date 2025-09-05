# main.py
import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Basic API Scraper Template",
    description="A minimal API to fetch JSON data for a given username from an external source.",
    version="0.1.0"
)

@app.get("/api/{username}")
def get_user_data(username: str):
    # NOTE: This Instagram endpoint is for demonstration. It may become unavailable or require authentication.
    target_url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
    
    # A standard User-Agent header can prevent being blocked immediately.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(target_url, headers=headers, timeout=8)

        # Handle 404 specifically for a clear user-not-found message
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"User '{username}' not found.")

        # Raise an exception for other bad status codes (like 429, 500, etc.)
        response.raise_for_status()

        # If the request is successful, return the raw JSON from the response
        return response.json()

    except requests.exceptions.RequestException as e:
        # Catch any network-related errors (e.g., connection timeout, DNS error)
        raise HTTPException(status_code=503, detail=f"Failed to connect to the external service: {e}")