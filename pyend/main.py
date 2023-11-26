#dotenv
import os,sys,subprocess,requests
from dotenv import load_dotenv

load_dotenv()


CREDENTIALS = {
    "CLIENT_ID" : os.getenv("CLIENT_ID"),
    "CLIENT_SECRET" : os.getenv("CLIENT_SECRET")
}


def get_token():
    url = "https://accounts.spotify.com/api/token"
    payload = {
        "grant_type" : "client_credentials"
    }
    response = requests.post(url, data=payload, auth=(CREDENTIALS["CLIENT_ID"], CREDENTIALS["CLIENT_SECRET"]))
    return response.json()["access_token"]



# find a song
def find_song(song_name):
    url = "https://api.spotify.com/v1/search"
    params = {
        "q" : song_name,
        "type" : "track",
        "limit" : 1
    }
    headers = {
        "Authorization" : f"Bearer {get_token()}"
    }
    response = requests.get(url, params=params, headers=headers)
    return response.json()["tracks"]["items"]



song = find_song("hello")