import json
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def get_user_playlist(user_id, data):
    for user_data in data:
        if user_data["user_id"] == user_id:
            return user_data["playlist"]
    return None

def get_all_songs(data):
    all_songs = []
    for user_data in data:
        all_songs.extend([f"{song['artist']} - {song['song']}" for song in user_data["playlist"]])
    return all_songs

def collaborative_filtering(target_user_id, data):
    # Get the playlists of the target user and all other users
    target_playlist = get_user_playlist(target_user_id, data)
    all_playlists = [user_data["playlist"] for user_data in data]

    # Convert playlists to text representations for CountVectorizer
    vectorizer = CountVectorizer()
    all_playlists_text = [' '.join([f"{song['artist']} {song['song']} {song['genre']}" for song in playlist]) for playlist in all_playlists]
    target_playlist_text = ' '.join([f"{song['artist']} {song['song']} {song['genre']}" for song in target_playlist])

    # Transform text data using CountVectorizer
    playlists_matrix = vectorizer.fit_transform(all_playlists_text)
    target_matrix = vectorizer.transform([target_playlist_text])

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(target_matrix, playlists_matrix).flatten()

    # Find the most similar user
    most_similar_user_index = similarity_scores.argsort()[-2]
    most_similar_user_id = data[most_similar_user_index]["user_id"]

    # Recommend songs from the most similar user's playlist
    recommended_songs = get_user_playlist(most_similar_user_id, data)

    return recommended_songs

if __name__ == "__main__":
    # Load the JSON data from the file
    with open("playlists.json", "r") as json_file:
        playlists_data = json.load(json_file)

    # Choose a target user (e.g., user_id=1)
    target_user_id = 1

    # Get recommendations for the target user
    recommendations = collaborative_filtering(target_user_id, playlists_data)

    print(f"Recommendations for User {target_user_id}:\n")
    for song in recommendations:
        print(f"{song['artist']} - {song['song']} ({song['genre']})")
