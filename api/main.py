from flask import Flask, request, session  # Flask is used to create the server
from flask_cors import CORS  # Cors is used to allow cross origin requests
from deezer import (
    get_genre,
    get_album,
    get_artist,
    get_track,
    login,
    get_access_token,
)  # Import the functions from deezer.py
import os

app = Flask(__name__)  # Creates the server
CORS(app)  # Allows cross origin requests
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")  # Creates a route for the server
def hello_world():
    return "Hello World!"  # Returns the string "Hello World!"


@app.route("/user/<name>")  # Creates a route for the server
def hello_name(name):
    return f"Hello {name}!"


# Routes for the deezer api
@app.route("/deezer/login/")
def deezer_login():
    return login()


@app.route("/deezer/redirect")
def deezer_redirect():
    code = request.args["code"]
    access_token = get_access_token(code)["access_token"]
    session["access_token"] = access_token
    return "Access_Token Retrive Successfully"


@app.route("/deezer/genre")
def deezer_genre():
    return get_genre(access_token=session.get("access_token"))


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
