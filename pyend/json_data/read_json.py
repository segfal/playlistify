import json


with open("pop.json", "r") as file:
    data = json.load(file)

print(len(data[1]))