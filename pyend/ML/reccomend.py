import numpy as np
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity

'''
Still working on this, alot of this code is from chatgpt 
### Notes ###
- This is a collaborative filtering algorithm that uses cosine similarity to find the most similar user to the current user
- The most similar user's most listened to genre is used to recommend artists in that genre
- This is just an example of how you can use collaborative filtering to recommend artists

I am going to use this to reccomend songs based on the users listening history
we will create example data for the user and other users

'''









def find_most(playlist):
    data = Counter(playlist)
    return data.most_common(1)[0][0]

def build_playlist(user_data, all_users_data):
    # Get a union of all genres from user_data and all_users_data
    all_genres = set(user_data.keys()).union(*(data.keys() for data in all_users_data.values()))

    # Convert user data and all users data to arrays for similarity calculation
    user_data_array = np.array([user_data.get(genre, 0) for genre in all_genres]).reshape(1, -1)
    all_users_data_array = np.array([[data.get(genre, 0) for genre in all_genres] for data in all_users_data.values()])

    # Calculate cosine similarity between the user and all other users
    similarities = cosine_similarity(user_data_array, all_users_data_array)[0]

    # Find the most similar user
    most_similar_user_index = np.argmax(similarities)
    most_similar_user_data = list(all_users_data.values())[most_similar_user_index]

    # Get the most common genre listened to by the most similar user
    recommended_genre = find_most(most_similar_user_data)

    # Use the recommended genre to suggest artists in that genre
    recommended_artists = get_artists_in_genre(recommended_genre)

    print(f"Recommended artists based on collaborative filtering: {', '.join(recommended_artists)}")

def get_artists_in_genre(genre):
    # Replace this function with your logic to fetch Deezer artists based on the recommended genre
    # For example, you can use the Deezer API to search for artists in a particular genre
    # and return a list of artist names or IDs.
    return ['Artist1', 'Artist2', 'Artist3']

if __name__ == '__main__':
    # Example user data
    user_data = {'pop': 2, 'rock': 1, 'jazz': 1, 'hip-hop': 1}

    # Example data for other users
    all_users_data = {
        'user1': {'pop': 3, 'rock': 1, 'jazz': 2, 'hip-hop': 0},
        'user2': {'pop': 1, 'rock': 2, 'jazz': 0, 'hip-hop': 3},
        # Add more users and their listening data as needed
    }

    build_playlist(user_data, all_users_data)
