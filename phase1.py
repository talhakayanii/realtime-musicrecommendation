import os
import ast
import librosa
from pymongo import MongoClient
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['music_db']
collection = db['audio_features']

# Delete all documents from the collection
collection.delete_many({})

# Load track metadata
tracks = pd.read_csv('/home/hdoop/Downloads/project/metadata/tracks.csv', index_col=0, skiprows=[1, 2, 3])

# Process audio files and extract features
success_count = 0
for root, _, files in os.walk('/home/hdoop/Downloads/project/small'):
    for file in files:
        track_id = int(os.path.splitext(file)[0])  # Extract track_id from filename
        track_path = os.path.join(root, file)
        try:
            y, sr = librosa.load(track_path, duration=30)
            mfcc = librosa.feature.mfcc(y=y, sr=sr)
            
            # Perform PCA for dimensionality reduction
            pca = PCA(n_components=10)  # number of components as needed
            mfcc_reduced = pca.fit_transform(mfcc.T)  # Transpose for correct shape
            
            # Standardize the features
            scaler = StandardScaler()
            mfcc_standardized = scaler.fit_transform(mfcc_reduced)
            
            # Get track genres from the metadata
            track_genres = ast.literal_eval(tracks.loc[track_id, 'trackgenres'])
            
            # Store features in MongoDB
            collection.insert_one({
                'track_id': track_id,
                'mfcc': mfcc_standardized.tolist(),
                'track_genres': track_genres,
                # Add more features here
            })
            success_count += 1
        except Exception as e:
            print(f'Error processing track {track_id}: {e}')

print(f'Processed tracks successfully')
client.close()

