from elevenlabs import ElevenLabs
import os

try:
    client = ElevenLabs(api_key="sk_a60a1c35a2c895d348cc953511136ef08a293e4eee0c6d97")
    voices = client.voices.search()
    print(f"Found {len(voices.voices)} voices:")
    for v in voices.voices:
        print(f"{v.name} -> ID: {v.voice_id}")
except Exception as e:
    print(f"Error occurred: {e}")
    