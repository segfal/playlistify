# # from openai import OpenAI
# import openai


# from dotenv import load_dotenv
# from pprint import pprint

# load_dotenv()

# # client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))
# openai.api_key = os.getenv("OPEN_AI_KEY")

# genres = ["Pop", "Hip hop", "Rock", "Jazz", "R&B", "Bachata", "Trap", "Reggaeton"]
# years = [2017, 2018, 2019, 2020, 2021]
# playlist_names = [
#     "Vibrant Vibes",
#     "Serene Soundscape",
#     "Epic Energy Boost",
#     "Chill Lounge Escape",
#     "Midnight Melodies",
#     "Soulful Serenade",
#     "Eclectic Expedition",
#     "Rhythmic Reverie",
# ]


# def get_songs(genre, year):
#     message = f"Fill the list with 50 songs for {genre} from{year}.]return in array format so I can do artist = song[0], song = song[1], json format"

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-1106",
#         response_format={"type": "json_object"},
#         messages=[{"role": "user", "content": message}],
#     )

#     data_str = response.choices[0].message.content

#     lines = data_str.strip().split("\n")

#     # Extract the lines containing song data
#     song_lines = [line.strip() for line in lines if "[" in line and "]" in line]

#     # Combine the lines into a single string
#     cleaned_data_str = "[" + ",".join(song_lines) + "]"

#     # Using json.loads to convert the cleaned string into a list of lists
#     songs_list = json.loads(cleaned_data_str)

#     return songs_list


# pprint(get_songs(2017, "pop"))

import json
import os


def remove_playlist_name(json_file_path):
    with open(json_file_path, "r") as file:
        data = json.load(file)

    for song in data:
        if "playlist_name" in song:
            del song["playlist_name"]

    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=2,ensure_ascii=False)


def process_json_files():
    current_directory = os.getcwd()
    for filename in os.listdir(current_directory):
        if filename.endswith(".json"):
            json_file_path = os.path.join(current_directory, filename)
            remove_playlist_name(json_file_path)


process_json_files()
