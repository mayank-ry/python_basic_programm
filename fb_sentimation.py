from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

reviews = [
    "This product is absolutely amazing!",
    "Worst experience ever. Total waste of money.",
    "It's okay, nothing special."
]

for review in reviews:
    score = sia.polarity_scores(review)
    print(f"Review: {review}")
    print(f"Score: {score}\n")

# Positive score > 0   = Positive sentiment
# Negative score > 0   = Negative sentiment
# Compound -1 to +1    = Overall sentiment