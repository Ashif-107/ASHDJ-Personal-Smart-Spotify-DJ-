# TTS Configuration for Spotify DJ
# You can modify these settings to customize the voice behavior

# Default speech rate (-10 to 10, where 0 is normal speed)
DEFAULT_RATE = 0

# Anime/Japanese style rate (slower for effect)
ANIME_RATE = -2

# Fast speech rate for urgent notifications
FAST_RATE = 3

# Slow speech rate for emphasis
SLOW_RATE = -3

# Default voice index (0 for system default, 1 for alternate if available)
DEFAULT_VOICE = 0

# Volume level (0-100, only works with some TTS engines)
DEFAULT_VOLUME = 100

# Common phrases for your Spotify DJ
DJ_PHRASES = {
    "playing": "Now playing {}, senpai!",
    "paused": "Music paused, senpai!",
    "resumed": "Music resumed, senpai!",
    "next": "Skipping to the next track!",
    "previous": "Going back to the previous song!",
    "volume_up": "Volume increased!",
    "volume_down": "Volume decreased!",
    "shuffled": "Shuffle mode activated!",
    "repeat": "Repeat mode activated!",
    "error": "Oops! Something went wrong, senpai!",
    "greeting": "Hello! I'm your personal Spotify DJ assistant!",
    "goodbye": "Goodbye, senpai! Thanks for using Spotify DJ!"
}
