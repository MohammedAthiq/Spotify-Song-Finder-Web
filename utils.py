import requests
import base64
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

def get_access_token():
    try:
        auth_str = f"{client_id}:{client_secret}"
        b64_auth_str = base64.b64encode(auth_str.encode()).decode()

        headers = {
            "Authorization": f"Basic {b64_auth_str}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials"
        }

        response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
        if response.status_code != 200:
            return None
        return response.json().get("access_token")
    except Exception as e:
        return None

def search_song(lyrics):
    token = get_access_token()
    if not token:
        return {
            "name": "Error: No token",
            "artist": "-",
            "url": "#"
        }

    try:
        headers = {
            "Authorization": f"Bearer {token}"
        }

        params = {
            "q": lyrics,
            "type": "track",
            "limit": 1
        }

        response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
        if response.status_code != 200:
            return {
                "name": f"Error: {response.status_code}",
                "artist": "-",
                "url": "#"
            }

        result = response.json()
        track = result["tracks"]["items"][0]
        return {
            "name": track["name"],
            "artist": track["artists"][0]["name"],
            "url": track["external_urls"]["spotify"],
            "image": track["album"]["images"][0]["url"],
            "preview": track["preview_url"]
        }

    except IndexError:
        return {
            "name": "No song found with those lyrics",
            "artist": "-",
            "url": "#"
        }
    except Exception as e:
        return {
            "name": f"Error: {e}",
            "artist": "-",
            "url": "#"
        }