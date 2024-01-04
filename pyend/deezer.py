import requests

'''
Its better to use the requests library to make the api calls instead of the deezer python library
because its more flexible to use requests library, its like axios in javascript
'''


class Deezer:
    #get genre
    def get_genre(self,genre):
        url = "https://api.deezer.com/genre/"+genre
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
def get_genre(genre):
    return Deezer().get_genre(genre)

def get_artist(artist):
    return Deezer().get_artist(artist)

def get_album(album):
    return Deezer().get_album(album)

def get_track(track):
    return Deezer().get_track(track)
