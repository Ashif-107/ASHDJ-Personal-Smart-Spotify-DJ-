import os
import sys
import io
import pygame
from elevenlabs import ElevenLabs

# ====== ElevenLabs Setup ======
api_key = os.getenv("ELEVENLABS_API_KEY")
if not api_key:
    raise ValueError("❌ ELEVENLABS_API_KEY not found in environment variables.")

client = ElevenLabs(api_key=api_key)

# Initialize pygame mixer for audio playback
pygame.mixer.init()

def speak(text, voice="gARvXPexe5VF3cKZBian", model="eleven_multilingual_v2"):
    """
    Speak text in anime-style voice using ElevenLabs TTS without saving to disk.
    """
    try:
        # Generate audio from ElevenLabs (streaming response as bytes)
        audio = client.text_to_speech.convert(
            voice_id=voice,
            model_id=model,
            text=text
        )

        # Convert audio generator to bytes in memory
        audio_bytes = b"".join(audio)

        # Load audio directly from memory (BytesIO)
        audio_stream = io.BytesIO(audio_bytes)

        # Play audio directly
        pygame.mixer.music.load(audio_stream, "mp3")
        pygame.mixer.music.play()

        # Wait until audio finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)

    except Exception as e:
        print(f"❌ ElevenLabs TTS error: {e}", file=sys.__stderr__)

# Example usage
if __name__ == "__main__":
    print("Hello Ashif! Your anime DJ is ready to rock!")
