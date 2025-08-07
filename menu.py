"""
Menu and User Interface Functions
================================
This module contains the CLI menu and user interaction functions.
"""

import sys
from spotify_controls import (
    play_song, pause_song, next_track, previous_track, 
    current_status, toggle_shuffle, toggle_repeat, add_to_queue
)


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
