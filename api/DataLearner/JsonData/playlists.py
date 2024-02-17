import json
import random
import os
import sys



#print(random.randint(12,50))




def file_creator(filename,data):
    path = './temp_playlist'
    with open(f'{path}/{filename}','w') as f:
        json.dump(data,f,ensure_ascii=False,indent=4)
    return None

def file_reader(filename):

    path = './json_files/'
    key = filename.replace(".json","")
    filename = path+filename
    value = None
    with open(filename,'r') as f:
        value = json.load(f)
        return [key,value]
genres = {}
for i in os.listdir('./json_files'):
    x = file_reader(i)
    genres[x[0]] = x[1]





