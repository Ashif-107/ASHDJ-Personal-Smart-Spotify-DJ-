import os
import sys
import requests
import pygame
import io
import tempfile
from pathlib import Path

# Import TTS configuration
try:
    from tts_config import DJ_PHRASES
except ImportError:
    # Fallback values if config file is missing
    DJ_PHRASES = {
        "playing": "Now playing {}, senpai!",
        "paused": "Music paused, senpai!",
        "error": "Oops! Something went wrong, senpai!"
    }

# ElevenLabs Configuration
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')  # Set this in your environment variables
ELEVENLABS_URL = "https://api.elevenlabs.io/v1/text-to-speech"

# Anime girl voice IDs from ElevenLabs (you can change these)
ANIME_VOICES = {
    "default": "gARvXPexe5VF3cKZBian",  # Bella - clear, youthful voice
    "sweet": "21m00Tcm4TlvDq8ikWAM",   # Dorothy - sweet, gentle voice
    "energetic": "XB0fDUnXU5powFXDhCwa", # Charlotte - energetic voice
    "kawaii": "pNInz6obpgDQGcFmaJgB",   # Adam - can be pitched higher for kawaii effect
}

# Current voice setting
CURRENT_VOICE = "sweet"  # Change this to switch voices

def initialize_audio():
    """Initialize pygame mixer for audio playback"""
    try:
        pygame.mixer.init()
        return True
    except Exception as e:
        print(f"Failed to initialize audio: {e}")
        return False

def speak(text, voice_type="default", stability=0.5, similarity_boost=0.8):
    """
    Speak text using ElevenLabs anime girl voice
    
    Args:
        text (str): Text to speak
        voice_type (str): Type of voice from ANIME_VOICES
        stability (float): Voice stability (0.0-1.0)
        similarity_boost (float): Voice similarity boost (0.0-1.0)
    """
    if not ELEVENLABS_API_KEY:
        print("❌ ElevenLabs API key not found! Set ELEVENLABS_API_KEY environment variable")
        print(f"🔊 Would say: {text}")
        return False
    
    try:
        # Get voice ID
        voice_id = ANIME_VOICES.get(voice_type, ANIME_VOICES["default"])
        
        # Prepare the request
        url = f"{ELEVENLABS_URL}/{voice_id}"
        
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": ELEVENLABS_API_KEY
        }
        
        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",  # Good for anime-style speech
            "voice_settings": {
                "stability": stability,
                "similarity_boost": similarity_boost,
                "style": 0.2,  # Adds more emotion
                "use_speaker_boost": True
            }
        }
        
        # Make request to ElevenLabs
        print(f"🎌 Anime girl says: {text}")
        response = requests.post(url, json=data, headers=headers, timeout=30)
        
        if response.status_code == 200:
            # Initialize audio if not already done
            if not pygame.mixer.get_init():
                if not initialize_audio():
                    return False
            
            # Play audio directly from memory
            audio_data = io.BytesIO(response.content)
            pygame.mixer.music.load(audio_data)
            pygame.mixer.music.play()
            
            # Wait for playback to finish
            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)
            
            return True
        else:
            print(f"❌ ElevenLabs API error: {response.status_code} - {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ ElevenLabs API timeout - trying local TTS fallback")
        return _fallback_tts(text)
    except Exception as e:
        print(f"❌ ElevenLabs error: {e}")
        return _fallback_tts(text)

def _fallback_tts(text):
    """Fallback to Windows TTS if ElevenLabs fails"""
    try:
        import win32com.client
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Rate = -2  # Slightly slower for anime effect
        speaker.Speak(text)
        return True
    except:
        print(f"🔊 TTS: {text}")
        return False

def speak_japanese_style(text):
    """Speak with sweet anime girl voice"""
    speak(text, voice_type="sweet", stability=0.3, similarity_boost=0.9)

def speak_fast(text):
    """Speak with energetic anime voice for urgent notifications"""
    speak(text, voice_type="energetic", stability=0.7, similarity_boost=0.8)

def speak_slow(text):
    """Speak with gentle kawaii voice for emphasis"""
    speak(text, voice_type="kawaii", stability=0.2, similarity_boost=1.0)

def speak_dj_phrase(phrase_key, *args):
    """Speak a predefined DJ phrase with anime voice"""
    if phrase_key in DJ_PHRASES:
        text = DJ_PHRASES[phrase_key].format(*args)
        speak_japanese_style(text)
    else:
        speak(f"Unknown phrase: {phrase_key}", voice_type="default")

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

def set_voice_type(voice_type):
    """Change the default anime voice type"""
    global CURRENT_VOICE
    if voice_type in ANIME_VOICES:
        CURRENT_VOICE = voice_type
        speak(f"Voice changed to {voice_type} style!", voice_type=voice_type)
    else:
        speak("Invalid voice type!", voice_type="default")

def test_anime_voices():
    """Test all available anime voices"""
    test_text = "Hello senpai! I'm your anime DJ assistant!"
    
    for voice_name, voice_id in ANIME_VOICES.items():
        print(f"\n🎌 Testing {voice_name} voice...")
        speak(f"This is the {voice_name} voice style!", voice_type=voice_name)
        input("Press Enter to continue to next voice...")

# Initialize audio system when module is imported
initialize_audio()
