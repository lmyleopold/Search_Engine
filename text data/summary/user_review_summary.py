import json
from collections import defaultdict, Counter
from nltk.corpus import stopwords
from nltk import word_tokenize, ngrams
import matplotlib.pyplot as plt
import lucene
from org.apache.lucene.store import FSDirectory
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import Term
from org.apache.lucene.search import TermQuery
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.analysis.standard import StandardAnalyzer
from java.nio.file import Paths


def init_lucene():
    lucene.initVM()

# 提取用户评论数量
def get_user_review_count(index_path, user_id):
    print(f"Fetching review count for user: {user_id}")
    
    index_directory = FSDirectory.open(Paths.get(index_path))
    index_reader = DirectoryReader.open(index_directory)
    index_searcher = IndexSearcher(index_reader)

    # 查询用户评论
    # query = TermQuery(Term("user_id", user_id))
    analyzer = StandardAnalyzer()
    query = QueryParser("user_id", analyzer).parse(user_id)
    top_docs = index_searcher.search(query, 1000)  # 假设用户最多有1000条评论

    review_count = top_docs.totalHits.value
    index_reader.close()

    return review_count

# 获取用户评论的商家bounding box
def get_user_bounding_box(index_path, user_id):
    print(f"Fetching bounding box for user: {user_id}")

    index_directory = FSDirectory.open(Paths.get(index_path))
    index_reader = DirectoryReader.open(index_directory)
    index_searcher = IndexSearcher(index_reader)

    # 查询用户评论过的商家
    # query = TermQuery(Term("user_id", user_id))
    analyzer = StandardAnalyzer()
    query = QueryParser("user_id", analyzer).parse(user_id)
    top_docs = index_searcher.search(query, 1000)

    latitudes = []
    longitudes = []

    # 遍历每个文档，获取与评论相关的商家ID
    for score_doc in top_docs.scoreDocs:
        doc = index_searcher.doc(score_doc.doc)
        business_id = doc.get("business_id")

        # 使用 business_id 查询商家数据
        # business_query = TermQuery(Term("business_id", business_id))
        analyzer = StandardAnalyzer()
        business_query = QueryParser("business_id", analyzer).parse(business_id)
        business_docs = index_searcher.search(business_query, 1)

        if business_docs.totalHits.value > 0:
            business_doc = index_searcher.doc(business_docs.scoreDocs[0].doc)
            latitude = business_doc.get("latitude_display")
            longitude = business_doc.get("longitude_display")

            if latitude and longitude:
                latitudes.append(float(latitude))
                longitudes.append(float(longitude))

    index_reader.close()

    # 计算 bounding box
    if latitudes and longitudes:
        top_left = (max(latitudes), min(longitudes))  # 左上角 (最大纬度, 最小经度)
        bottom_right = (min(latitudes), max(longitudes))  # 右下角 (最小纬度, 最大经度)
        return top_left, bottom_right
    else:
        return None, None

# 获取用户评论中的高频词和短语
def get_top_frequent_words(index_path, user_id, top_n=10):
    print(f"Fetching top frequent words for user: {user_id}")

    index_directory = FSDirectory.open(Paths.get(index_path))
    index_reader = DirectoryReader.open(index_directory)
    index_searcher = IndexSearcher(index_reader)

    # 查询用户评论
    # query = TermQuery(Term("user_id", user_id))
    analyzer = StandardAnalyzer()
    query = QueryParser("user_id", analyzer).parse(user_id)
    top_docs = index_searcher.search(query, 1000)

    # 收集所有评论文本
    review_texts = []
    for score_doc in top_docs.scoreDocs:
        doc = index_searcher.doc(score_doc.doc)
        review_text = doc.get("text")
        if review_text:
            review_texts.append(review_text)

    index_reader.close()

    # 统计高频词（排除停用词）
    stop_words = set(stopwords.words("english"))
    word_counter = Counter()

    for review in review_texts:
        words = word_tokenize(review.lower())
        filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
        word_counter.update(filtered_words)

    # 统计高频短语 (bigrams)
    bigram_counter = Counter()
    for review in review_texts:
        words = word_tokenize(review.lower())
        filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
        bigrams = ngrams(filtered_words, 2)
        bigram_counter.update(bigrams)

    # 返回高频词和高频短语
    top_words = word_counter.most_common(top_n)
    top_bigrams = bigram_counter.most_common(top_n)

    return top_words, top_bigrams

# 输出用户评论总结
def user_review_summary(index_path, user_id):
    # 获取用户贡献的评论数量
    review_count = get_user_review_count(index_path, user_id)
    print(f"User {user_id} has contributed {review_count} reviews.")

    # 获取用户评论的商家活动区域 (bounding box)
    top_left, bottom_right = get_user_bounding_box(index_path, user_id)
    if top_left and bottom_right:
        print(f"User {user_id}'s activity area is defined by the bounding box:")
        print(f"Top-left corner (latitude, longitude): {top_left}")
        print(f"Bottom-right corner (latitude, longitude): {bottom_right}")
    else:
        print(f"Could not determine the bounding box for user {user_id}.")

    # 获取用户评论中的高频词和短语
    top_words, top_bigrams = get_top_frequent_words(index_path, user_id)
    print(f"Top-10 most frequent words: {top_words}")
    print(f"Top-10 most frequent phrases: {top_bigrams}")

if __name__ == "__main__":
    init_lucene()

    index_path = "./data/index"  # 假设索引已经构建

    user_id = "bcjbaE6dDog4jkNY91ncLQ"  # 示例用户ID

    user_review_summary(index_path, user_id)
