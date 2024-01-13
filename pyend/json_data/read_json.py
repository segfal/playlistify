import json


with open("country.json", "r") as file:
    data = json.load(file)

print(len(data))