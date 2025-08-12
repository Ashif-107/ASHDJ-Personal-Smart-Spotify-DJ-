# ElevenLabs Anime Voice Setup Guide 🎌

Your Spotify DJ now uses ElevenLabs API for authentic anime girl voices!

## Setup Steps:

### 1. Get ElevenLabs API Key
1. Go to [ElevenLabs](https://elevenlabs.io/)
2. Sign up for a free account
3. Go to your profile and copy your API key

### 2. Set Environment Variable
**Windows Command Prompt:**
```cmd
setx ELEVENLABS_API_KEY "your_api_key_here"
```

**Or add to your system environment variables:**
1. Right-click "This PC" → Properties
2. Advanced System Settings → Environment Variables
3. Add new variable: `ELEVENLABS_API_KEY` = `your_api_key_here`

### 3. Available Anime Voices:
- **sweet**: Gentle, kawaii voice (default for DJ phrases)
- **energetic**: Upbeat, excited anime voice
- **kawaii**: Super cute, high-pitched voice
- **default**: Clear, youthful anime voice

### 4. Test Your Setup:
```python
from elevenlabs_api import test_anime_voices, speak
speak("Hello senpai! I'm your anime DJ!", voice_type="sweet")
```

### 5. Usage Examples:
```python
# Basic anime speech
speak("Now playing your favorite song!", voice_type="sweet")

# DJ announcements
announce_playing("Anime Opening Theme")
announce_paused()

# Different voice styles
speak_fast("Quick notification!")  # Energetic voice
speak_slow("Important message...")  # Kawaii voice
```

## Free Tier Limits:
- 10,000 characters per month
- Perfect for DJ announcements!

## Fallback:
If ElevenLabs fails, it automatically falls back to Windows TTS.

Enjoy your anime DJ experience! (◕‿◕)
