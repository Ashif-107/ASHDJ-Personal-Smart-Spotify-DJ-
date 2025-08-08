"""
Artist Name Corrections
=====================
This module contains common artist name corrections for better search results.
"""

# Common artist name misspellings and variations
ARTIST_CORRECTIONS = {
    'weekend': 'weeknd',
    'the weekend': 'the weeknd',
    'drake': 'drake',
    'eminem': 'eminem',
    'kanye': 'kanye west',
    'ye': 'kanye west',
    'taylor': 'taylor swift',
    'beyonce': 'beyoncé',
    'justin': 'justin bieber',
    'ariana': 'ariana grande',
    'billie': 'billie eilish',
    'ed': 'ed sheeran',
    'post': 'post malone',
    'travis': 'travis scott',
    'kendrick': 'kendrick lamar',
    'j cole': 'j. cole',
    'future': 'future',
    'lil wayne': 'lil wayne',
    'chance': 'chance the rapper',
    'childish': 'childish gambino',
    'frank': 'frank ocean',
    'the beatles': 'the beatles',
    'beatles': 'the beatles',
    'queen': 'queen',
    'coldplay': 'coldplay',
    'radiohead': 'radiohead',
    'nirvana': 'nirvana',
    'ac dc': 'ac/dc',
    'acdc': 'ac/dc'
}

def correct_artist_name(query):
    """
    Apply common artist name corrections to improve search results.
    
    Args:
        query (str): The original search query
        
    Returns:
        str: The corrected search query
    """
    query_lower = query.lower()
    
    for incorrect, correct in ARTIST_CORRECTIONS.items():
        if incorrect in query_lower:
            # Replace the incorrect artist name while preserving case in other parts
            corrected_query = query_lower.replace(incorrect, correct)
            return corrected_query
    
    return query
