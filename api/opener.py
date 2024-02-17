import json,os

t = 'playlist_folder'



folder_name = 'playlist_folder/'
x= os.listdir('playlist_folder')
file_url = folder_name + x[0]


with open(file_url) as f:
    data = json.load(f)

print(data)