"""
Menu and User Interface Functions
================================
This module contains the CLI menu and user interaction functions.
"""

import sys
from commands.spotify_controls import (
    play_song, pause_song, next_track, previous_track, 
    current_status, toggle_shuffle, toggle_repeat, add_to_queue,
    play_similar_song, play_mood_songs
)

from algorithms.knn_recommender import find_similar_tracks
from algorithms.intent_parser import parse_intent

def print_help():
    """Display the help menu with available commands."""
    print("""
🎧 Spotify CLI Assistant — Commands:
-------------------------------------
play [song name]      ▶️  Plays the song or resumes playback
pause                 ⏸️  Pauses the music
next                  ⏭️  Skips to next track
previous              ⏮️  Goes to previous track
shuffle               🔀  Toggles shuffle on/off
repeat                🔁  Toggles repeat mode (off → context → track)
queue [song name]     ➕  Adds song to playback queue
status                🎵  Shows current playing song
help                  📜  Shows this message
exit                  ❌  Exits the app

🤖 Smart Commands (Natural Language):
-------------------------------------
"play something like [song] by [artist]"  🎯  Find similar songs
"play songs like [song]"                  🎯  Find similar songs  
"play happy/sad/chill music"              🎭  Mood-based playlists

Examples:
- "play something like starboy by the weeknd"
- "play songs like bohemian rhapsody"
- "play happy music"
- "play chill songs"
""")


def process_command(sp, command):
    """Process user commands and execute corresponding functions."""
    command = command.strip().lower()
    
    if command.startswith("play "):
        song = command[5:]
        play_song(sp, song)
    
    elif command == "play":
        play_song(sp)

    elif command == "pause":
        pause_song(sp)

    elif command == "next":
        next_track(sp)

    elif command == "previous":
        previous_track(sp)

    elif command == "help":
        print_help()

    elif command.startswith("queue "):
        song = command[6:]
        add_to_queue(sp, song)

    elif command == "shuffle":
        toggle_shuffle(sp)

    elif command == "repeat":
        toggle_repeat(sp)

    elif command == "status":
        current_status(sp)

    elif command == "exit":
        print("👋 Exiting. Goodbye!")
        sys.exit()

    else:
        intent_data = parse_intent(command)

        if intent_data["intent"] == "play_similar":
            play_similar_song(sp, intent_data["track_query"])
        elif intent_data["intent"] == "play_mood":
            play_mood_songs(sp, intent_data["mood"])
        elif intent_data["intent"] == "play_exact":
            play_song(sp, intent_data["query"])
        else:
            print("❓ Unknown command. Type 'help' to see options.")

def run_interactive_menu(sp):
    """Run the main interactive command loop."""
    print("🎵 Welcome to Spotify CLI Assistant!")
    print("Type 'help' to see available commands.\n")

    while True:
        try:
            command = input("> ")
            process_command(sp, command)

        except KeyboardInterrupt:
            print("\n👋 Exiting. Goodbye!")
            break
