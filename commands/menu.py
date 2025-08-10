import sys
from commands.spotify_controls import (
    play_song, pause_song, next_track, previous_track, 
    current_status, toggle_shuffle, toggle_repeat, add_to_queue,
    play_similar_song, play_mood_songs
)

from algorithms.knn_recommender import find_similar_tracks
from algorithms.intent_parser import parse_intent


def print_help(output_func=print):
    """Display the help menu with available commands."""
    output_func("""
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


def process_command(sp, command, output_func=print):
    """Process user commands and execute corresponding functions."""
    command = command.strip().lower()

    base_commands = {
        "pause": pause_song,
        "next": next_track,
        "previous": previous_track,
        "shuffle": toggle_shuffle,
        "repeat": toggle_repeat,
        "status": current_status,
        "help": lambda sp: print_help(output_func),
        "exit": lambda sp: sys.exit("👋 Exiting. Goodbye!")
    }

    if command in base_commands:
        base_commands[command](sp)
        return

    if command.startswith("queue "):
        song = command[6:]
        add_to_queue(sp, song)
        return

    intent_data = parse_intent(command)
    print(f"🔍 Detected intent: {intent_data}")

    if intent_data["intent"] == "play_similar":
        play_similar_song(sp, intent_data["track_query"])
    elif intent_data["intent"] == "play_mood":
        play_mood_songs(sp, intent_data["mood"])
    elif intent_data["intent"] == "play_exact":
        play_song(sp, intent_data["query"])
    elif command == "play":
        play_song(sp)
    else:
        output_func("❓ Unknown command. Type 'help' to see options.")


def run_interactive_menu(sp, single_command=None, output_func=print):
    """
    Run the main interactive command loop.
    If single_command is provided, runs just that command (for GUI mode).
    """
    if not single_command:
        output_func("🎵 Welcome to Spotify CLI Assistant!")
        output_func("Type 'help' to see available commands.\n\n")

    if single_command:
        process_command(sp, single_command, output_func)
        return
    
    while True:
        try:
            command = input("> ")
            process_command(sp, command, output_func)
        except KeyboardInterrupt:
            output_func("\n👋 Exiting. Goodbye!")
            break
