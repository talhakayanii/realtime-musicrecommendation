from pymongo import MongoClient
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['music_db']
collection = db['audio_features']

# Query for similar tracks
query_track_id = 38899  # ID of the track for which you want to find similar tracks
query_track_mfcc = np.array(collection.find_one({'track_id': query_track_id})['mfcc'][0]).reshape(1, -1)  # Assuming only one set of MFCC features per track

similar_tracks = []
cursor = collection.find({})
for document in cursor:
    track_id = document['track_id']
    track_mfcc = np.array(document['mfcc'][0]).reshape(1, -1)  # Assuming only one set of MFCC features per track
    print(track_id)

    # Calculate cosine similarity
    similarity = cosine_similarity(query_track_mfcc, track_mfcc)[0][0]

    # Add track if similar
    if similarity > 0.8 and track_id != query_track_id:  # Adjust threshold as needed
        similar_tracks.append(track_id)

# Print the similar track IDs
print("Similar tracks for track", query_track_id, ":", similar_tracks)

client.close()

