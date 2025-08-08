# command/intent_parser.py

import re

def parse_intent(user_input):
    user_input = user_input.lower()

    # Play similar to a given track - improved pattern matching
    similar_patterns = [
        r"play\s+(something\s+like|songs\s+like|music\s+like)\s+(.*)",
        r"(something\s+like|songs\s+like|music\s+like)\s+(.*)",
        r"play\s+(similar\s+to|like)\s+(.*)",
        r"(similar\s+to|like)\s+(.*)"
    ]
    
    for pattern in similar_patterns:
        match = re.search(pattern, user_input)
        if match:
            # Extract the track query from the matched groups
            if len(match.groups()) >= 2:
                track_query = match.group(2).strip()
            else:
                track_query = match.group(1).strip()
            
            if track_query:  # Make sure we have a valid query
                return {"intent": "play_similar", "track_query": track_query}

    # Mood-based triggers
    moods = {
        "sad": ["sad", "depressed", "blue"],
        "happy": ["happy", "joy", "cheerful"],
        "romantic": ["romantic", "love", "valentine"],
        "dance": ["dance", "party", "move"],
        "chill": ["chill", "relax", "lofi", "calm"]
    }

    for mood, keywords in moods.items():
        if any(word in user_input for word in keywords):
            return {"intent": "play_mood", "mood": mood}

    # Play specific fallback
    if user_input.startswith("play "):
        return {"intent": "play_exact", "query": user_input[5:].strip()}

    return {"intent": "unknown"}
