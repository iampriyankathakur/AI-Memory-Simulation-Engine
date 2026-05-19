def emotional_score(text):

    emotional_keywords = [
        "love",
        "hate",
        "fear",
        "sad",
        "happy",
        "difficult",
        "excited"
    ]

    score = 0

    for word in emotional_keywords:
        if word in text.lower():
            score += 1

    return score
