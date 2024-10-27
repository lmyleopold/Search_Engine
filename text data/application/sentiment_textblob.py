# sentiment_textblob.py

from textblob import TextBlob
from collections import defaultdict
import numpy as np

def analyze_sentiment_textblob(text):
    """Use TextBlob for sentiment analysis."""
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Sentiment score between -1 and 1

def analyze_reviews_with_textblob(reviews):
    """
    Analyze sentiment fluctuation in the given list of reviews.
    :param reviews: Dictionary containing review texts {date: [review_texts]}
    :return: Average sentiment scores grouped by date
    """
    sentiment_by_date = defaultdict(list)

    for date, texts in reviews.items():
        for text in texts:
            sentiment_score = analyze_sentiment_textblob(text)
            sentiment_by_date[date].append(sentiment_score)

    # Calculate average sentiment score per date
    avg_sentiment_by_date = {date: np.mean(scores) for date, scores in sentiment_by_date.items()}

    return avg_sentiment_by_date
