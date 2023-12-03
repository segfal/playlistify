from flask import Flask #Flask is used to create the server
from flask_cors import CORS #Cors is used to allow cross origin requests


app = Flask(__name__) #Creates the server
CORS(app) #Allows cross origin requests

@app.route("/") #Creates a route for the server
def hello_world():
    return "Hello World!" #Returns the string "Hello World!"

@app.route("/user/<name>") #Creates a route for the server
def hello_name(name):
    return f"Hello {name}!"



app.run()

