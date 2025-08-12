# 🎤 Windows Built-in Text-to-Speech for Spotify DJ

## Overview
Your Spotify DJ now uses Windows' built-in text-to-speech capabilities instead of requiring external libraries like ElevenLabs. This means **no additional installations required**!

## Features

### 🎯 Multiple TTS Methods
- **Primary**: Windows SAPI (Speech API) via `win32com.client`
- **Fallback**: PowerShell with System.Speech
- **Ultimate Fallback**: Text output if audio fails

### 🎭 Speaking Styles
- `speak(text)` - Normal speech
- `speak_japanese_style(text)` - Slower rate for anime effect
- `speak_fast(text)` - Quick announcements
- `speak_slow(text)` - Emphasis and dramatic effect

### 🎵 DJ-Specific Functions
- `announce_playing(song_name)` - "Now playing [song], senpai!"
- `announce_paused()` - "Music paused, senpai!"
- `announce_error()` - "Oops! Something went wrong, senpai!"
- `speak_dj_phrase(key, *args)` - Use predefined phrases

### ⚙️ Customization
Edit `tts_config.py` to customize:
- Speech rates for different styles
- Default voice selection
- DJ phrases and responses
- Volume levels

## Usage Examples

```python
from elevenlabs_api import speak, announce_playing, speak_japanese_style

# Basic usage
speak("Hello from your Spotify DJ!")

# Announce song
announce_playing("Your favorite song")

# Anime style
speak_japanese_style("Konnichiwa, senpai!")

# Custom rate and voice
speak("Custom speech", rate=2, voice_index=1)
```

## Testing

Run the demo scripts to test functionality:

```bash
python demo_tts.py          # Full feature demo
python test_tts.py          # Basic functionality test
```

## Requirements
- Windows operating system
- Python 3.6+
- No external libraries needed!

## Troubleshooting

If you don't hear audio:
1. Check your system volume
2. Ensure Windows audio services are running
3. Try running as administrator if permissions are an issue
4. The system will fall back to text output if audio completely fails

## Benefits
- ✅ No internet connection required
- ✅ No API keys needed
- ✅ No external library installations
- ✅ Works offline
- ✅ Uses system's default voice settings
- ✅ Lightweight and fast
- ✅ Always available on Windows systems
