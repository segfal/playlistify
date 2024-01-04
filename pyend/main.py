from flask import Flask #Flask is used to create the server
from flask_cors import CORS #Cors is used to allow cross origin requests
from deezer import get_genre,get_album,get_artist,get_track #Import the functions from deezer.py

app = Flask(__name__) #Creates the server
CORS(app) #Allows cross origin requests

@app.route("/") #Creates a route for the server
def hello_world():
    return "Hello World!" #Returns the string "Hello World!"

@app.route("/user/<name>") #Creates a route for the server
def hello_name(name):
    return f"Hello {name}!"


#Routes for the deezer api
@app.route("/deezer/genre/<genre>")
def deezer_genre(genre):
    return get_genre(genre)

@app.route("/deezer/artist/<artist>")
def deezer_artist(artist):
    return get_artist(artist)

@app.route("/deezer/album/<album>")
def deezer_album(album):
    return get_album(album)

@app.route("/deezer/track/<track>")
def deezer_track(track):
    return get_track(track)



app.run()

