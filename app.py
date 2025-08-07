from spotify_api import authenticate_spotify
from menu import run_interactive_menu


def main():
    try:
        sp = authenticate_spotify()
        run_interactive_menu(sp)
    except Exception as e:
        print(f"❌ Error initializing Spotify: {e}")
        print("Please check your configuration and try again.")

if __name__ == "__main__":
    main()
