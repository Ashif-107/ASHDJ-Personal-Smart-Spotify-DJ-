import os
import tempfile
import pygame
from elevenlabs import ElevenLabs, save

# Import TTS configuration
try:
    from tts_config import DJ_PHRASES
except ImportError:
    # Fallback values if config file is missing
    DJ_PHRASES = {
        "playing": "Now playing {}, Ashif senpai!",
        "paused": "Music paused, Ashif senpai!",
        "error": "Oops! Something went wrong, Ashif senpai!"
    }

# ====== ElevenLabs Setup ======
api_key = os.getenv("ELEVENLABS_API_KEY")
if not api_key:
    raise ValueError("❌ ELEVENLABS_API_KEY not found in environment variables.")

client = ElevenLabs(api_key=api_key)

# Initialize pygame mixer for audio playback
pygame.mixer.init()

def speak(text, voice="gARvXPexe5VF3cKZBian", model="eleven_multilingual_v2"):
    """
    Speak text in Javenglish style using ElevenLabs TTS.
    """
    try:
        # Generate audio from ElevenLabs
        audio = client.text_to_speech.convert(
            voice_id=voice,
            model_id=model,
            text=text
        )

        # Save temporary file
        temp_path = os.path.join(tempfile.gettempdir(), "tts_eleven.mp3")
        save(audio, temp_path)

        # Load and play using pygame (works reliably on Windows)
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()
        
        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)

    except Exception as e:
        print(f"❌ ElevenLabs TTS error: {e}")

def speak_dj_phrase(phrase_key, *args):
    """Speak a predefined DJ phrase with anime voice"""
    if phrase_key in DJ_PHRASES:
        text = DJ_PHRASES[phrase_key].format(*args)
        speak(text)
    else:
        speak(f"Unknown phrase: {phrase_key}")

# Convenience functions for common DJ actions
def announce_playing(song_name):
    """Announce that a song is now playing with cute anime voice"""
    speak_dj_phrase("playing", song_name)

def announce_paused():
    """Announce that music is paused with anime voice"""
    speak_dj_phrase("paused")

def announce_error():
    """Announce an error occurred with anime voice"""
    speak_dj_phrase("error")
