# Spotify DJ - Intelligent Music Recommendation System

A CLI-based music recommendation system that acts as an intelligent DJ, understanding natural language requests and providing sophisticated audio feature-based recommendations.

## How the Algorithms Work

### 1. **Enhanced Audio Feature Analysis (KNN Recommender)**
- Uses **K-Nearest Neighbors (KNN)** with 11 audio features: danceability, energy, valence, tempo, acousticness, etc.
- **Fallback Feature Estimation**: When Spotify's audio analysis API fails, the system intelligently estimates features using:
  - **Genre-based weights** (e.g., electronic music gets higher danceability/energy scores)
  - **Temporal adjustments** (newer songs tend to be more danceable)
  - **Artist characteristics** (popularity, follower count influence features)
  - **Track metadata** (duration, release year, popularity affect feature estimation)

### 2. **Natural Language Intent Parser**
- Parses conversational input like "play something like Bohemian Rhapsody" or "play sad music"
- Extracts intent types: `play_similar`, `play_mood`, `play_exact`
- Supports mood-based requests (happy, sad, chill, dance, romantic)

### 3. **Smart Track Discovery**
- Searches using multiple strategies: related artists, genre-based queries, temporal ranges
- Builds diverse candidate pools for better recommendations
- Uses Euclidean distance in feature space to find most similar tracks

## What Makes This Unique

Unlike typical music recommendation systems that rely solely on:
- **Collaborative filtering** (what others like you listen to)
- **Simple popularity rankings**
- **Basic genre matching**

This system provides:

1. **Authentic Audio Analysis**: Deep feature estimation when APIs fail, using sophisticated genre knowledge and musical theory
2. **Conversational Interface**: Natural language understanding instead of rigid commands
3. **Resilient Architecture**: Multiple fallback methods ensure recommendations even with API limitations
4. **Musical Intelligence**: Genre-aware feature weighting based on actual musical characteristics
5. **Real-time Adaptation**: Dynamically adjusts to current track context and user mood

The combination of advanced NLP intent parsing with sophisticated audio feature analysis creates a more intelligent and reliable music discovery experience.
