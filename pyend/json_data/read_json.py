import json
import os


json_files = os.listdir()
json_files = [file for file in json_files if file.endswith('.json')]


lens = 0
table = []
# remove country.json
json_files.remove('country.json')
for file in json_files:
    with open(file, 'r') as f:
        data = json.load(f)
        lens += len(data[1])
        table.append(data[1])

#print(table[0])
x = len(table[0])

num = 0
for i in table:
    num += len(i)
print(num)