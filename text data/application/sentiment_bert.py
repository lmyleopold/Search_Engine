from transformers import pipeline
from collections import defaultdict
import numpy as np

# Load pre-trained BERT model for sentiment analysis
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment_bert(text):
    """
    Calculate a continuous sentiment score for a single text using BERT.
    :param text: Review text
    :return: Continuous sentiment score based on confidence
    """
    # Truncate text to fit within BERT's token limit (approx. 512 tokens)
    truncated_text = text[:512]

    result = sentiment_analyzer(truncated_text)[0]
    confidence = result['score']  # Model's confidence in its label
    
    # Map POSITIVE to positive score, NEGATIVE to negative score
    if result['label'] == 'POSITIVE':
        return confidence  # positive score
    else:
        return -confidence  # negative score

def analyze_reviews_with_bert(reviews):
    """
    Analyze sentiment for a collection of reviews using BERT with continuous scores.
    :param reviews: Dictionary with dates as keys and lists of review texts as values
    :return: Dictionary with dates as keys and average sentiment scores as values
    """
    sentiment_by_date = defaultdict(list)

    for date, texts in reviews.items():
        for text in texts:
            sentiment_score = analyze_sentiment_bert(text)
            sentiment_by_date[date].append(sentiment_score)

    return {date: np.mean(scores) for date, scores in sentiment_by_date.items()}
