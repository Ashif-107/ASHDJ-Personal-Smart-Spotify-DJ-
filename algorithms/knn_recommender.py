# recommend/knn_recommender.py

from sklearn.neighbors import NearestNeighbors
import numpy as np

AUDIO_FEATURE_KEYS = [
    "danceability", "energy", "key", "loudness", "mode",
    "speechiness", "acousticness", "instrumentalness", 
    "liveness", "valence", "tempo"
]

def extract_features(track):
    return np.array([track[key] for key in AUDIO_FEATURE_KEYS])


def build_feature_matrix(sp, seed_features, sample_tracks):
    """Build matrix of features including seed song."""
    all_features = [seed_features]
    track_uris = []

    for track in sample_tracks:
        features = sp.audio_features(track['uri'])[0]
        if features:
            all_features.append(extract_features(features))
            track_uris.append((track['uri'], track['name'], track['artists'][0]['name']))

    return np.array(all_features), track_uris


def find_similar_tracks(sp, current_track_id):
    """Find 5 similar tracks to the current one using KNN."""

    # Get seed song's audio features
    seed_features = sp.audio_features(current_track_id)[0]
    if not seed_features:
        print("❌ Could not get audio features for the current track.")
        return []

    seed_vector = extract_features(seed_features)

    # Get a list of 50-100 tracks (top hits or similar genre)
    search_results = sp.search(q="year:2020-2024", type="track", limit=50)
    tracks = search_results['tracks']['items']

    feature_matrix, track_uris = build_feature_matrix(sp, seed_vector, tracks)

    # Run KNN to find similar tracks
    knn = NearestNeighbors(n_neighbors=6, algorithm='auto').fit(feature_matrix)
    distances, indices = knn.kneighbors([seed_vector])

    # Skip index 0 (it’s the song itself)
    similar_tracks = []
    for idx in indices[0][1:]:
        uri, name, artist = track_uris[idx - 1]
        similar_tracks.append((uri, name, artist))

    return similar_tracks
