# console.py

from sentiment_textblob import analyze_reviews_with_textblob
from sentiment_bert import analyze_reviews_with_bert
from utils import load_reviews, plot_sentiment_trend, init_lucene

def main():
    # Initialize Lucene virtual machine
    init_lucene()

    index_path = "./data/index"  # Assuming index path
    business_id = input("Enter the business ID: ").strip()
    method = input("Choose method (textblob/bert): ").strip().lower()

    # Load review data
    reviews = load_reviews(index_path, business_id)
    if not reviews:
        print(f"No reviews found for business ID: {business_id}")
        return

    # Choose analysis method
    if method == "textblob":
        date_sentiment = analyze_reviews_with_textblob(reviews)
        plot_sentiment_trend(business_id, date_sentiment, method="TextBlob")
    elif method == "bert":
        date_sentiment = analyze_reviews_with_bert(reviews)
        plot_sentiment_trend(business_id, date_sentiment, method="BERT")
    else:
        print("Invalid method selected. Choose 'textblob' or 'bert'.")

if __name__ == "__main__":
    main()
