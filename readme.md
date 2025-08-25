# Spotify DJ - Intelligent Music Recommendation System

A CLI-based music recommendation system that acts as an intelligent DJ, understanding natural language requests and providing sophisticated audio feature-based recommendations.

With Voice Command controls and a Live GUI 

## How the Algorithms Work

### 1. **Enhanced Audio Feature Analysis (KNN Recommender)**

#### When Spotify's audio features API is limited, we created an intelligent estimation system that analyzes track metadata, genres, artist information, and temporal patterns to generate realistic audio features.

- Uses **K-Nearest Neighbors (KNN)** with 11 audio features: danceability, energy, valence, tempo, acousticness, etc.
- **Fallback Feature Estimation**: When Spotify's audio analysis API fails, the system intelligently estimates features using:
  - **Genre-based weights** (e.g., electronic music gets higher danceability/energy scores)
  - **Temporal adjustments** (newer songs tend to be more danceable)
  - **Artist characteristics** (popularity, follower count influence features)
  - **Track metadata** (duration, release year, popularity affect feature estimation)

            Core Audio Features Used
            The system analyzes 11 key audio characteristics:

            Danceability: How suitable a track is for dancing (0.0-1.0)
            Energy: Perceptual measure of intensity and power (0.0-1.0)
            Key: The key the track is in (0-11, normalized to 0.0-1.0)
            Loudness: Overall loudness in dB (normalized to 0.0-1.0)
            Mode: Modality (major=1, minor=0)
            Speechiness: Presence of spoken words (0.0-1.0)
            Acousticness: Confidence measure of acoustic nature (0.0-1.0)
            Instrumentalness: Predicts whether track contains no vocals (0.0-1.0)
            Liveness: Detects presence of audience in recording (0.0-1.0)
            Valence: Musical positivity/happiness (0.0-1.0)
            Tempo: Overall estimated tempo in BPM (normalized to 0.0-1.0)

### 2. **Natural Language Intent Parser**
- Parses conversational input like "play something like Summertime Sadness" or "play sad music"
- Extracts intent types: `play_similar`, `play_mood`, `play_exact`
- Supports mood-based requests (happy, sad, chill, dance, romantic)

### 3. **Smart Track Discovery**
- Searches using multiple strategies: related artists, genre-based queries, temporal ranges
- Builds diverse candidate pools for better recommendations
- Uses Euclidean distance in feature space to find most similar tracks

## What Makes This Unique

Unlike typical music recommendation systems that rely solely on:
- **Simple popularity rankings**
- **Basic genre matching**

This system provides:

1. **Authentic Audio Analysis**: Deep feature estimation when APIs fail, using sophisticated genre knowledge and musical theory
2. **Conversational Interface**: Natural language understanding instead of rigid commands
3. **Resilient Architecture**: Multiple fallback methods ensure recommendations even with API limitations
4. **Musical Intelligence**: Genre-aware feature weighting based on actual musical characteristics
5. **Real-time Adaptation**: Dynamically adjusts to current track context and user mood

The combination of advanced NLP intent parsing with sophisticated audio feature analysis creates a more intelligent and reliable music discovery experience.


## Cool GUI 
![alt text](assets/anime_girl.gif)

