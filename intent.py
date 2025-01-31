import re

def get_intent(user_input):
    user_input = user_input.lower()

    # Define patterns and corresponding intents
    patterns = {
        r"(hello|hi|hey|howdy)": "greeting",
        r"(?:what can you do\??|(?:tell me your|what are your) abilit(?:y|ies))": "ability",
        r"(bye|goodbye|see you)": "farewell",
        r"(\b(?:search|find)\b.*)": "search",
        r"(\b(?:book|reserve)\b.*)": "booking",
        r"(\b(?:weather|forecast|climate)\b.*)": "weather",
        r"(\b(?:help|support)\b.*)": "help"
    }

    # Iterate over the patterns and check for matches
    for pattern, intent in patterns.items():
        if re.search(pattern, user_input):
            return intent
    
    # If no match is found, assume it as a general inquiry intent
    return "inquiry"