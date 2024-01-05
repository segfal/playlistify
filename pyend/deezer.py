import requests
from flask import redirect, session
import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

'''
Its better to use the requests library to make the api calls instead of the deezer python library
because its more flexible to use requests library, its like axios in javascript
'''


class Deezer:
    

    #login
    def login():
        url = (f"https://connect.deezer.com/oauth/auth.php?app_id={os.getenv("DEZEER_APP_ID")}&redirect_uri={os.getenv("DEZEER_REDIRET_URI")}&perms=basic_access,email,manage_library,listening_history,offline_access")
        return redirect(url)
    
    #get access_token
    def get_access_token(code):
        url = (f"https://connect.deezer.com/oauth/access_token.php?app_id={os.getenv("DEZEER_APP_ID")}&secret={os.getenv("DEZEER_SECRET_KEY")}&code={code}&output=json")
        response = requests.get(url)
        return response.json();
        
    
    #get genre
    def get_genre(self, access_token):
        url = f"https://api.deezer.com/genre"
        response = requests.get(url)
        return response.json()
    
    #get artist
    def get_artist(self,artist):
        url = "https://api.deezer.com/artist/"+artist
        response = requests.get(url)
        return response.json()
    
    #get album
    def get_album(self,album):
        url = "https://api.deezer.com/album/"+album
        response = requests.get(url)
        return response.json()
    
    #get track
    def get_track(self,track):
        url = "https://api.deezer.com/track/"+track
        response = requests.get(url)
        return response.json()
    
# encapsulate the class in a function
    
'''
!!!READ THIS!!!
You dont need to edit the functions below 
because they are just calling the functions from the Deezer class
only edit the Deezer class

I only encapsulated the class in a function because its easier to import the functions from deezer.py

'''
def login():
    return Deezer.login()

def get_access_token(code):
    return Deezer.get_access_token(code)

def get_genre(access_token):
    return Deezer().get_genre(access_token=access_token)

def get_artist(artist):
    return Deezer().get_artist(artist)

def get_album(album):
    return Deezer().get_album(album)

def get_track(track):
    return Deezer().get_track(track)
