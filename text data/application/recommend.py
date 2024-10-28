import lucene, json
from collections import Counter
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
from java.nio.file import Path, Paths # type: ignore
from org.apache.lucene.store import FSDirectory # type: ignore
from org.apache.lucene.index import DirectoryReader, Term # type: ignore
from org.apache.lucene.search import IndexSearcher, TermQuery # type: ignore

def search_instance(search_key, search_value, search_target):
    result = []

    index_directory = FSDirectory.open(Paths.get('./data/index'))
    index_reader = DirectoryReader.open(index_directory)
    index_searcher = IndexSearcher(index_reader)
    
    query = TermQuery(Term(search_key, search_value))
    top_docs = index_searcher.search(query, 1000000)
    
    for _, score_doc in enumerate(top_docs.scoreDocs):
        doc_id = score_doc.doc
        doc = index_searcher.doc(doc_id)
        if doc.get(search_target) != None:
            result.append(doc.get(search_target))
        
    index_reader.close()

    return result

def parse_category(category, at = True):
    list = category.split(',')
    if at:
        list = [word for item in list for word in item.split('&')]
    list = [item.lower().strip() for item in list]
    return list

def get_business_categories():
    categories = set()

    business_categories = search_instance('json_type', 'business', 'categories')
    
    for category in business_categories:
        list = parse_category(category)
        categories.update(list)

    return sorted(categories)

def get_user_keyword(user_id):
    business_categories = get_business_categories()
    user_review = search_instance('user_id', user_id, 'text')
    user_review_sentence = []
    for review in user_review:
        user_review_sentence.extend(s for s in sent_tokenize(review) if len(s) > 20)

    keywrods = Counter()
    analyser = SentimentIntensityAnalyzer()

    for sentence in user_review_sentence:
        sentiment_score = analyser.polarity_scores(sentence)['compound']
        if sentiment_score > 0.1:
            words = word_tokenize(sentence.lower())
            filtered_words = [word for word in words if word in business_categories]
            # if use sentiment score
            # if not, use /sentiment_score = 1/
            dict = {word: sentiment_score for word in filtered_words}
            keywrods.update(dict)
    
    return keywrods

def get_user_business_score(user_id, business_id):
    business_category = search_instance('business_id', business_id, 'categories')
    if len(business_category) > 0:
        business_category_list = parse_category(business_category[0])
    else:
        print(f"The business with business_id {business_id} doesn't post relevant category tag")
        return 0

    user_keyword  = get_user_keyword(user_id)
    user_keyword_value = sum(user_keyword.values())
    user_keyword = dict(user_keyword)

    score = 0
    for item in business_category_list:
        if item in user_keyword:
            score += user_keyword[item]
    
    score += 0.112345 * user_keyword_value
    score /= user_keyword_value

    print(f'According to user {user_id} review keywords and business {business_id} tags, \
          the score, which means if user will like this business, is {score:.6f}')
    
    return score


if __name__ == "__main__":
    lucene.initVM()
    user_id = 'bcjbaE6dDog4jkNY91ncLQ'
    business_id = "x5-7JNoYyh8VgCp5pCsiUw"
    print(get_user_business_score(user_id, business_id))