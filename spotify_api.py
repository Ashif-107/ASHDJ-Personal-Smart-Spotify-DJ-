import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

def authenticate_spotify():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

    if not all([client_id, client_secret, redirect_uri]):
        raise ValueError("Missing Spotify credentials in environment variables")

    scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing streaming"

    sp_oauth = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        open_browser=True,
        show_dialog=True  # This forces the login dialog to appear
    )

    try:
        sp = spotipy.Spotify(auth_manager=sp_oauth)
        # Test the connection
        sp.current_user()
        return sp
    except Exception as e:
        print(f"Authentication failed: {e}")
        print("Please check your Spotify credentials and try again.")
        raise
