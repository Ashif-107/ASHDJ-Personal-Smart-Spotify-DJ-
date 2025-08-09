"""
Spotify Control Functions
========================
This module contains all the Spotify playback control functions.
"""

from algorithms.knn_recommender import find_similar_tracks


def play_song(sp, query=None):
    """Play a song by search query or resume current playback."""
    playback = sp.current_playback()

    if query:
        # Try multiple search strategies to find the song
        tracks = []
        
        # Strategy 1: Search with track: prefix (most restrictive)
        results = sp.search(q=f"track:{query}", limit=5, type='track')
        tracks = results['tracks']['items']
        
        # Strategy 2: Search without prefix if first attempt fails
        if not tracks:
            results = sp.search(q=query, limit=5, type='track')
            tracks = results['tracks']['items']
        
        # Strategy 3: Handle common artist name variations
        if not tracks and 'weekend' in query.lower():
            modified_query = query.lower().replace('weekend', 'weeknd')
            results = sp.search(q=modified_query, limit=5, type='track')
            tracks = results['tracks']['items']

        if tracks:
            # Pick the top result
            track = tracks[0]
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            track_uri = track['uri']
            album_uri = track['album']['uri']

            # Try to get user's liked songs for better shuffle experience
            try:
                # Play from album context but start with the specific track for continuous playback
                sp.shuffle(True)
                sp.start_playback(context_uri=album_uri, offset={"uri": track_uri})
                
                # Add some popular tracks from the same artist to the queue for immediate variety
                artist_id = track['artists'][0]['id']
                top_tracks = sp.artist_top_tracks(artist_id)
                
                # Add top 5 tracks from the same artist to queue (excluding the current one)
                added_count = 0
                for top_track in top_tracks['tracks']:
                    if top_track['uri'] != track_uri and added_count < 5:
                        sp.add_to_queue(top_track['uri'])
                        added_count += 1
                
                print(f"▶️ Now playing: {track_name} by {artist_name}")
                
            except Exception:
                # Fallback: play from album context with shuffle only
                sp.shuffle(True)
                sp.start_playback(context_uri=album_uri, offset={"uri": track_uri})
                print(f"▶️ Now playing: {track_name} by {artist_name}")

        else:
            print("❌ No song found. Try a simpler name or artist.")
    else:
        if playback and not playback['is_playing']:
            sp.start_playback()
            print("▶️ Resumed playback")
        elif playback and playback['is_playing']:
            print("⚠️ Music is already playing.")
        else:
            print("❌ No active device found. Play a song by name first.")


def pause_song(sp):
    """Pause the current playback."""
    playback = sp.current_playback()
    if playback and playback['is_playing']:
        sp.pause_playback()
        print("⏸️ Paused playback")
    else:
        print("⚠️ Already paused or nothing is playing.")


def next_track(sp):
    """Skip to the next track."""
    playback = sp.current_playback()
    if playback:
        sp.next_track()
        print("⏭️ Skipped to next track")
    else:
        print("❌ No active playback found.")


def previous_track(sp):
    """Go back to the previous track."""
    playback = sp.current_playback()
    if playback:
        sp.previous_track()
        print("⏮️ Reverted to previous track")
    else:
        print("❌ No active playback found.")


def current_status(sp):
    """Display the currently playing song information."""
    playback = sp.current_playback()
    if playback and playback['item']:
        song = playback['item']['name']
        artist = playback['item']['artists'][0]['name']
        print(f"🎵 Now playing: {song} by {artist}")
    else:
        print("🔇 Nothing is currently playing.")


def toggle_shuffle(sp):
    """Toggle shuffle mode on/off."""
    playback = sp.current_playback()
    if playback:
        current_shuffle = playback['shuffle_state']
        sp.shuffle(not current_shuffle)
        print(f"🔀 Shuffle turned {'ON' if not current_shuffle else 'OFF'}")
    else:
        print("❌ No active device found to toggle shuffle.")


def toggle_repeat(sp):
    """Cycle through repeat modes: off → context → track → off."""
    playback = sp.current_playback()
    if playback:
        current_repeat = playback['repeat_state']
        new_state = {
            'off': 'context',
            'context': 'track',
            'track': 'off'
        }[current_repeat]
        sp.repeat(new_state)
        print(f"🔁 Repeat mode set to: {new_state.upper()}")
    else:
        print("❌ No active playback to toggle repeat mode.")


def add_to_queue(sp, query):
    """Add a song to the playback queue by search query."""
    results = sp.search(q=query, limit=1, type='track')
    tracks = results['tracks']['items']
    if tracks:
        track_uri = tracks[0]['uri']
        sp.add_to_queue(track_uri)
        print(f"➕ Added to queue: {tracks[0]['name']} by {tracks[0]['artists'][0]['name']}")
    else:
        print("❌ No matching song found to add to queue.")


# For the ML based Smart Algoritms


def play_similar_song(sp, track_query):
    """
    Search for a track and play 5 similar tracks based on audio features.
    """
    try:
        print(f"🔎 Searching for track: {track_query}")
        result = sp.search(q=track_query, type='track', limit=1)

        if not result['tracks']['items']:
            print("❌ Track not found.")
            return

        track = result['tracks']['items'][0]
        track_id = track['id']
        track_name = track['name']
        artist_name = track['artists'][0]['name']

        print(f"🎯 Found: {track_name} by {artist_name}")
        print("🎧 Finding similar tracks...")

        similar_tracks = find_similar_tracks(sp, track_id)

        if not similar_tracks:
            print("⚠️ No similar tracks found.")
            return

        for uri, name, artist in similar_tracks:
            print(f"➕ Queuing: {name} by {artist}")
            sp.add_to_queue(uri)

        # Start playback from the first recommended track
        sp.start_playback(uris=[similar_tracks[0][0]])

    except Exception as e:
        print(f"❌ Error in play_similar_song: {e}")


def play_mood_songs(sp, mood):
    """Play a set of songs based on mood using Spotify genre search."""
    genre_map = {
        "sad": "sad",
        "happy": "happy",
        "romantic": "romance",
        "dance": "dance",
        "chill": "chill"
    }

    genre = genre_map.get(mood, "pop")
    results = sp.search(q=f"genre:{genre}", type='track', limit=10)
    tracks = results['tracks']['items']
    if tracks:
        uris = [track['uri'] for track in tracks[:5]]
        sp.start_playback(uris=uris)
        print(f"💫 Playing {mood.capitalize()} mood playlist.")
    else:
        print("❌ Couldn't find mood-based songs.")