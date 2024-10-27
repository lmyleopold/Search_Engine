# utils.py

import lucene
from java.nio.file import Paths
from org.apache.lucene.store import FSDirectory
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.analysis.standard import StandardAnalyzer
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.ndimage import gaussian_filter1d
import os

def init_lucene():
    """Initialize Lucene virtual machine."""
    lucene.initVM()

def load_reviews(index_path, business_id):
    """
    Load reviews for the specified business.
    :param index_path: Path to the index.
    :param business_id: ID of the target business.
    :return: Dictionary in the format {date: [review_texts]}, representing reviews for the business on each date.
    """
    print(f"Loading reviews for business ID: {business_id}")

    # Open index directory
    index_directory = FSDirectory.open(Paths.get(index_path))
    index_reader = DirectoryReader.open(index_directory)
    index_searcher = IndexSearcher(index_reader)

    # Analyzer
    analyzer = StandardAnalyzer()

    # Create query to get reviews for the specified business_id
    query = QueryParser("business_id", analyzer).parse(business_id)
    top_docs = index_searcher.search(query, 1000)  # Assume at most 1000 reviews returned

    # Dictionary to store data in the format {date: [review_texts]}
    reviews_by_date = defaultdict(list)

    for score_doc in top_docs.scoreDocs:
        doc = index_searcher.doc(score_doc.doc)
        review_text = doc.get("text")
        review_date = doc.get("date")

        # Debugging statements
        print(f"Review Text: {review_text}")
        print(f"Review Date: {review_date}")

        if review_text and review_date:
            try:
                date_obj = datetime.strptime(review_date, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                date_obj = datetime.strptime(review_date.split()[0], "%Y-%m-%d")

            # Append the review to the date
            reviews_by_date[date_obj].append(review_text)
        else:
            print("Skipping review due to missing text or date.")

    index_reader.close()

    return reviews_by_date

def plot_sentiment_trend(business_id, date_sentiment, method):
    """
    Plot sentiment fluctuation graph with a red dashed line for the average score.
    Also generates a smoothed version of the sentiment trend.
    :param business_id: The ID of the business
    :param date_sentiment: Dictionary of sentiment scores grouped by date {date: average sentiment score}
    :param method: Name of the sentiment analysis method used
    """
    dates = sorted(date_sentiment.keys())
    sentiment_scores = [date_sentiment[date] for date in dates]
    
    # Calculate the mean sentiment score
    mean_score = np.mean(sentiment_scores)

    # Plot sentiment scores over time
    plt.figure(figsize=(12, 6))
    plt.plot(dates, sentiment_scores, marker='o', color='b', linestyle='-', label="Sentiment Score")
    plt.axhline(y=mean_score, color='r', linestyle='--', label=f"Mean Score ({mean_score:.2f})")
    plt.title(f"{business_id} Sentiment Over Time ({method})")
    plt.xlabel("Date")
    plt.ylabel("Average Sentiment Score")
    plt.legend()
    plt.grid()

    # Save the original plot
    output_folder = "./application/output"
    os.makedirs(output_folder, exist_ok=True)
    plt.savefig(f"{output_folder}/{business_id}_sentiment_trend_{method}.png")
    plt.close()

    # Smooth the sentiment scores using Gaussian filter
    smoothed_scores = gaussian_filter1d(sentiment_scores, sigma=2)

    # Plot the smoothed sentiment trend
    plt.figure(figsize=(12, 6))
    plt.plot(dates, smoothed_scores, color='g', linestyle='-', label="Smoothed Sentiment Score")
    plt.axhline(y=mean_score, color='r', linestyle='--', label=f"Mean Score ({mean_score:.2f})")
    plt.title(f"{business_id} Smoothed Sentiment Over Time ({method})")
    plt.xlabel("Date")
    plt.ylabel("Smoothed Average Sentiment Score")
    plt.legend()
    plt.grid()

    # Save the smoothed plot
    plt.savefig(f"{output_folder}/{business_id}_sentiment_trend_smoothed_{method}.png")
    plt.close()