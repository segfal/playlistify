from surprise.dump import load
import pandas as pd 
import json
# test file to test if the model is making any predictions...
loaded_model = load("colab_filter.ipynb")
with open("test_data.json", "r") as json_file:
    user_data = json.load(json_file)


past_songs = user_data.get("user_past_songs", [])

# to store the recomendations for this user
user_recommendations = []
for past_song in past_songs:
    song = past_song.get("song", "")
    artist = past_song.get("artist", "")
    
    if song and artist:
        predicted_rating = loaded_model.predict(song, artist).est
        user_recommendations.append((song, artist, predicted_rating))


user_recommendations.sort(key=lambda x: x[2], reverse=True)

if user_recommendations:
    top_recommendation = user_recommendations[0]
    print(f"Top recommended song based on past listening history:")
    print(f"{top_recommendation[0]} by {top_recommendation[1]}")
else:
    print("No recommendations available based on past listening history.")