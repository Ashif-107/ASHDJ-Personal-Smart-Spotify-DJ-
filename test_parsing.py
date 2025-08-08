"""
Test Intent Parser
=================
Simple test script to verify intent parsing works correctly.
"""

from algorithms.intent_parser import parse_intent
from algorithms.artist_corrections import correct_artist_name

def test_intent_parsing():
    """Test various user inputs to ensure they're parsed correctly."""
    
    test_cases = [
        "play something like starboy by weekend",
        "play songs like bohemian rhapsody",
        "something like blinding lights",
        "play similar to shape of you",
        "play happy music",
        "play chill songs",
        "play starboy",
    ]
    
    print("🧪 Testing Intent Parsing:")
    print("=" * 50)
    
    for test_input in test_cases:
        result = parse_intent(test_input)
        print(f"Input: '{test_input}'")
        print(f"Intent: {result['intent']}")
        if 'track_query' in result:
            print(f"Track Query: '{result['track_query']}'")
        elif 'mood' in result:
            print(f"Mood: '{result['mood']}'")
        elif 'query' in result:
            print(f"Query: '{result['query']}'")
        print("-" * 30)

def test_artist_corrections():
    """Test artist name corrections."""
    
    test_queries = [
        "starboy by weekend",
        "blinding lights by the weekend", 
        "shape of you by ed",
        "lucid dreams by juice world",
        "old town road by lil nas"
    ]
    
    print("\n🎨 Testing Artist Corrections:")
    print("=" * 50)
    
    for query in test_queries:
        corrected = correct_artist_name(query)
        print(f"Original: '{query}'")
        print(f"Corrected: '{corrected}'")
        print("-" * 30)

if __name__ == "__main__":
    test_intent_parsing()
    test_artist_corrections()
