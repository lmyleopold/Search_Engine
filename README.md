# Sentiment and Search Analysis Project

This project performs sentiment analysis and search operations on business reviews. It provides various scripts for tokenization, index creation, querying, and sentiment analysis using both TextBlob and BERT models. Additionally, it includes visualization tools for plotting sentiment trends and review distribution.

## Project Structure

```
text data/
├── data/
│   └── LA_business.jsonl                    # Data file containing business information
├── token/
│   ├── pos.py                               # Script for POS tagging and visualization
│   ├── tokenization.py                      # Script for tokenizing and stemming
│   ├── utils.py                             # Utility functions for data sampling
│   └── visualization.py                     # Functions for plotting various analyses
├── search/
│   ├── index.py                             # Script to create Lucene index for the dataset
│   ├── query.py                             # Script to perform different types of queries
│   ├── console.py                           # Console application for interactive querying
│   └── reprentative.py                      # Script to extract representative sentences for a user
├── summary/
│   ├── review_distribution.py               # Script to plot the distribution of user reviews
│   └── user_review_summary.py               # Script to generate summary for a user’s reviews
└── application/
    ├── console.py                           # Main console for executing sentiment analysis
    ├── recommend.py                         # Script to recommend businesses based on user review history
    ├── sentiment_bert.py                    # Sentiment analysis with BERT
    ├── sentiment_textblob.py                # Sentiment analysis with TextBlob
    └── utils.py                             # Helper functions for loading reviews and plotting sentiment trends

```

## Setup Instructions

1. **Environment Setup**:
   - Ensure you have [Python 3.x](https://www.python.org/downloads/) and [Apache Lucene](https://lucene.apache.org/) installed.
   - Install required Python packages by running:
     ```bash
     pip install nltk transformers textblob matplotlib scipy wordcloud
     ```

2. **Lucene Initialization**:
   - Many scripts require the Lucene virtual machine (VM) to be initialized. This can be done with:
     ```python
     lucene.initVM()
     ```

## Module Descriptions

### 1. Tokenization and POS Tagging (`token/`)

- **pos.py**: Tokenizes text, performs part-of-speech (POS) tagging, and plots the distribution of sentence lengths and POS tags in the reviews.
- **tokenization.py**: Tokenizes, stems, and counts word frequencies in reviews. Also plots the distribution of word lengths and generates a word cloud.
- **utils.py**: Provides functions for sampling data from JSON files.
- **visualization.py**: Contains helper functions for plotting distributions, top word frequencies, and generating word clouds.

### 2. Index Creation and Querying (`search/`)

- **index.py**: Creates a Lucene index for the business and review data. This allows fast searching based on various fields like `business_id`, `text`, `user_id`, etc.
  - `create_index(index_path)`: Creates an index at the specified path with options for case folding, stemming, and stopword removal.
  - `insight_index(index_path)`: Displays basic information about the index.
- **query.py**: Provides different query types:
  - `normal_query()`, `phrase_query()`, `boolean_query()`, and `geospatial_query()` perform keyword, phrase, Boolean, and geospatial queries, respectively.
- **console.py**: An interactive console for querying the dataset using different query types.
- **reprentative.py**: Extracts the most common sentences or representative sentences for a user using TF-IDF and cosine similarity.

### 3. Summary and Distribution (`summary/`)

- **review_distribution.py**: Calculates and plots the distribution of reviews contributed by each user. The plot is saved to a file and provides insights into review frequency.
  - `extract_user_review_data()`: Retrieves review data for each user.
  - `plot_review_distribution()`: Plots the distribution with a logarithmic scale.
- **user_review_summary.py**: Generates a summary of a user’s review contributions, including:
  - The number of reviews contributed by the user.
  - The bounding box of businesses reviewed by the user.
  - The top 10 most frequent words and phrases used by the user.

### 4. Sentiment Analysis and Recommendation (`application/`)

- **console.py**: Main console for executing sentiment analysis. Allows users to select a business ID and choose between `TextBlob` or `BERT` for sentiment analysis.
- **recommend.py**: Provides a recommendation score for a business based on the user’s past reviews. The score is based on sentiment analysis of frequently mentioned keywords.
- **sentiment_textblob.py**: Uses TextBlob for sentiment analysis on review text and calculates an average sentiment score for each date.
- **sentiment_bert.py**: Uses BERT for sentiment analysis, with a continuous sentiment score calculated for each review.
- **utils.py**: Contains functions to load reviews and plot sentiment trends over time. Plots include:
  - A plot of sentiment fluctuation over time.
  - A smoothed version using Gaussian filtering for trend visualization.

## How to Use

### Running the Search Console
Run the search console to interactively search the indexed data:
```bash
python search/console.py
```

### Running Sentiment Analysis
Run the `application/console.py` script to analyze sentiment on a business's reviews:
```bash
python application/console.py
```

### Running Review Summary
Generate a summary of a user’s reviews:
```bash
python summary/user_review_summary.py
```

## Visualization

Various plots are generated as part of the analysis, including:

- **Token Length Distribution**: Shows the distribution of token lengths before and after stemming.
- **Top Words and Phrases**: Bar plots of the top frequent words and phrases.
- **POS Tag Distribution**: Shows the frequency of different POS tags in reviews.
- **Sentiment Trend**: Line plot showing sentiment fluctuation over time for a business, with a red dashed line indicating the mean score and an optional smoothed trend.

## Additional Notes

- **Data Requirements**: The project expects the data files in JSON format, specifically `LA_business.jsonl` and `LA_review.jsonl` located in `data/`.
- **Error Handling**: Ensure that your environment paths are correct, and the data files exist in the specified format to avoid errors.

## Future Enhancements

Consider adding:

- **Extended Sentiment Analysis**: Using additional NLP models for more nuanced sentiment analysis.
- **Advanced Querying**: Implementing more advanced search features, such as fuzzy search.
- **Enhanced Recommendation**: Refining the recommendation algorithm based on more user and business attributes.
