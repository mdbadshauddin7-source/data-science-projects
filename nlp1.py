import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

sentences = [
    "I hate this product!",
    "This is awesome!",
    "It is okay, not good.",
    "bad experience!",
    "I like this!"
]

for sentence in sentences:
    score = sia.polarity_scores(sentence)
    if score['compound'] >= 0.05:
        print(sentence, "→ Positive 😊")
    elif score['compound'] <= -0.05:
        print(sentence, "→ Negative 😞")
    else:
        print(sentence, "→ Neutral 😐")