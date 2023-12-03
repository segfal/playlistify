#dotenv
import os,sys,subprocess,requests,json,time
from dotenv import load_dotenv

load_dotenv()



def json_print(json_data,filename):
    with open(filename,"w") as file:
        json.dump(json_data,file,indent=4)


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
    return response.json()["tracks"]["items"][0]["id"]



def get_track(song_name = None ,song_id = None):
    song = song_name if song_name else song_id
    #song = find_song(song)
    url = f"https://api.spotify.com/v1/tracks/{song}"
    headers = {
        "Authorization" : f"Bearer {get_token()}"
    }
    response = requests.get(url, headers=headers)
    return response.json()


json_print(get_track(song_id="11dFghVXANMlKmJXsNCbNl"),"hello.json")



