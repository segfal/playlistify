import json


with open("hip_hop.json", "r") as file:
    data = json.load(file)

print(len(data[1]))