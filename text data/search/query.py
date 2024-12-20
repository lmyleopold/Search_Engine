import lucene
import os, time
from java.io import File, StringReader # type: ignore
from java.nio.file import Path, Paths # type: ignore
from org.apache.lucene.store import ByteBuffersDirectory, MMapDirectory, NIOFSDirectory, FSDirectory # type: ignore
from org.apache.lucene.analysis.core import SimpleAnalyzer, WhitespaceAnalyzer, StopAnalyzer # type: ignore
from org.apache.lucene.analysis.en import EnglishAnalyzer # type: ignore
from org.apache.lucene.analysis.tokenattributes import PayloadAttribute # type: ignore
from org.apache.lucene.analysis.standard import StandardAnalyzer # type: ignore
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer, LimitTokenCountAnalyzer # type: ignore
from org.apache.lucene.util import Version, BytesRef, BytesRefIterator # type: ignore
from org.apache.lucene.document import Document, Field, StoredField, LongPoint, DoublePoint, StringField, TextField # type: ignore
from org.apache.lucene.index import IndexOptions, IndexWriter, IndexWriterConfig, DirectoryReader, FieldInfos, MultiFields, MultiTerms, Term # type: ignore
from org.apache.lucene.queryparser.classic import MultiFieldQueryParser, QueryParser # type: ignore
from org.apache.lucene.search import BooleanClause, BooleanQuery, IndexSearcher, TermQuery, PhraseQuery # type: ignore
from org.apache.lucene.search.highlight import Highlighter, QueryScorer, SimpleFragmenter, SimpleHTMLFormatter  # type: ignore
from index import create_index

# this function use ""QueryParser""
# this function includes keyword, phrase and boolean search
# because QueryParser can search according to the type of query_str ???? the result may not be correct, more experiment
# query_str = "test", keyword query
# query_str = "test test", phrase query
# query_str = "test AND test" boolean query
def normal_query(index_path, query_str, N = 10, search_key = "text", casefold = True, stemming = True, stopword = True):
    print("---------- begin normal query ----------", '\n')

    start_time = time.time()

    index_directory = FSDirectory.open(Paths.get(index_path))
    index_reader = DirectoryReader.open(index_directory)
    index_searcher = IndexSearcher(index_reader)
    
    # analyzer for query
    analyzer = StandardAnalyzer()
    if casefold == False:
        analyzer = WhitespaceAnalyzer()
    else:
        if stopword == False:
            analyzer = SimpleAnalyzer()
        else:
            if stemming == False:
                analyzer = StopAnalyzer()

    # "test" is the content in the json to search, can be changed to other key in json, like business_id
    query = QueryParser(search_key, analyzer).parse(query_str)
    
    top_docs = index_searcher.search(query, N)

    # 使用 Highlighter 来生成摘要片段
    formatter = SimpleHTMLFormatter("<b>", "</b>")  # 定义高亮格式
    scorer = QueryScorer(query)
    highlighter = Highlighter(formatter, scorer)
    highlighter.setTextFragmenter(SimpleFragmenter(50))  # 片段的长度为50个字符

    end_time = time.time()

    print(f"Query processed in {end_time - start_time:.2f} seconds")
    
    print(f"------found {top_docs.totalHits.value} documents, the top {N} as follows:-----")
    for rank, score_doc in enumerate(top_docs.scoreDocs):
        doc_rank = rank + 1
        doc_id = score_doc.doc
        doc_score = score_doc.score
        doc = index_searcher.doc(score_doc.doc)
        
        # 获取要高亮的字段文本
        text_to_highlight = doc.get(search_key)
        if text_to_highlight:
            token_stream = analyzer.tokenStream(search_key, StringReader(text_to_highlight))
            fragment = highlighter.getBestFragment(token_stream, text_to_highlight)
            snippet = fragment if fragment else text_to_highlight[:100]
        else:
            snippet = "No snippet available"

        print(f"json_type: {doc.get('json_type')}, rank: {doc_rank}, score: {doc_score},\
              docID: {doc_id}, {search_key}: {doc.get(search_key)}", '\n')

    index_reader.close()

#use PhraseQuery for phrase query. if the str only have one word, it is also be keyword query
def phrase_query(index_path, query_str, N = 10, search_key = "text"):
    print("---------- begin phrase query ----------", '\n')

    start_time = time.time()

    index_directory = FSDirectory.open(Paths.get(index_path))
    index_reader = DirectoryReader.open(index_directory)
    index_searcher = IndexSearcher(index_reader)

    phrase_query = PhraseQuery.Builder()
    for str in query_str.split():
        phrase_query.add(Term(search_key, str))
    phrase_query = phrase_query.build()

    top_docs = index_searcher.search(phrase_query, N)

    end_time = time.time()
    print(f"Query processed in {end_time - start_time:.2f} seconds")

    print(f"------found {top_docs.totalHits.value} documents, the top {N} as follows:-----")
    for rank, score_doc in enumerate(top_docs.scoreDocs):
        doc_rank = rank + 1
        doc_id = score_doc.doc
        doc_score = score_doc.score
        doc = index_searcher.doc(score_doc.doc)
        print(f"json_type: {doc.get('json_type')}, rank: {doc_rank}, score: {doc_score},\
              docID: {doc_id}, {search_key}: {doc.get(search_key)}", '\n')

    index_reader.close()

# use BooleanQuery, can only boolean query
def boolean_query(index_path, query_str, N = 10, search_key = "text"):
    print("---------- begin boolean query ----------", '\n')

    start_time = time.time()

    index_directory = FSDirectory.open(Paths.get(index_path))
    index_reader = DirectoryReader.open(index_directory)
    index_searcher = IndexSearcher(index_reader)

    boolean_query = BooleanQuery.Builder()
    for str in query_str.split():
        boolean_query.add(TermQuery(Term(search_key, str)), BooleanClause.Occur.MUST)  # AND 
    # AND BooleanClause.Occur.MUST
    # OR BooleanClause.Occur.SHOULD
    # NOT BooleanClause.Occur.MUST_NOT
    boolean_query = boolean_query.build()

    top_docs = index_searcher.search(boolean_query, N)

    end_time = time.time()
    print(f"Query processed in {end_time - start_time:.2f} seconds")

    print(f"------found {top_docs.totalHits.value} documents, the top {N} as follows:-----")
    for rank, score_doc in enumerate(top_docs.scoreDocs):
        doc_rank = rank + 1
        doc_id = score_doc.doc
        doc_score = score_doc.score
        doc = index_searcher.doc(score_doc.doc)
        print(f"json_type: {doc.get('json_type')}, rank: {doc_rank}, score: {doc_score},\
              docID: {doc_id}, {search_key}: {doc.get(search_key)}", '\n')

    index_reader.close()


# this function is used to search the businesses in the bounding box
def geospatial_query(index_path, top_left, bottom_right, N=10):
    """
    执行地理空间查询，查找在 bounding box 内的 businesses
    :param index_path: 索引路径
    :param top_left: 左上角坐标 (latitude, longitude)
    :param bottom_right: 右下角坐标 (latitude, longitude)
    :param N: 返回的文档数量
    """
    print("---------- begin geospatial query ----------", '\n')

    start_time = time.time()
    
    # 打开索引目录和索引读取器
    index_directory = FSDirectory.open(Paths.get(index_path))
    index_reader = DirectoryReader.open(index_directory)
    index_searcher = IndexSearcher(index_reader)

    # 定义范围查询，使用左上角和右下角坐标定义经纬度范围
    latitude_query = DoublePoint.newRangeQuery(
        "latitude", bottom_right[0], top_left[0])  # 纬度范围 (最小纬度, 最大纬度)
    longitude_query = DoublePoint.newRangeQuery(
        "longitude", top_left[1], bottom_right[1])  # 经度范围 (最小经度, 最大经度)

    # 构建布尔查询，将 latitude 和 longitude 范围查询结合
    boolean_query = BooleanQuery.Builder()
    boolean_query.add(latitude_query, BooleanClause.Occur.MUST)  # 必须满足纬度范围
    boolean_query.add(longitude_query, BooleanClause.Occur.MUST)  # 必须满足经度范围
    boolean_query = boolean_query.build()

    # 执行搜索
    top_docs = index_searcher.search(boolean_query, N)

    end_time = time.time()
    print(f"Query processed in {end_time - start_time:.2f} seconds")
    
    # 输出查询结果
    print(f"------found {top_docs.totalHits.value} businesses, the top {N} as follows:-----")
    for rank, score_doc in enumerate(top_docs.scoreDocs):
        doc_rank = rank + 1
        doc_id = score_doc.doc
        doc_score = score_doc.score
        doc = index_searcher.doc(score_doc.doc)
        print(f"json_type: {doc.get('json_type')}, rank: {doc_rank}, score: {doc_score}, "
              f"docID: {doc_id}, name: {doc.get('name')}, "
              f"latitude: {doc.get('latitude_display')}, longitude: {doc.get('longitude_display')}", '\n')

    index_reader.close()


if __name__ == "__main__":
    index_path = "./data/index"
    lucene.initVM()

    if not os.path.exists(index_path):
        create_index(index_path, casefold = True, stemming = True, stopword = True)

    query_str = 'good breakfast'
    normal_query(index_path, query_str)

    # split the phrase into each single word
    phrase_query(index_path, query_str)

    #in boolean query, after splitint, select the word not in {and, or, not}
    #I have not achieved this
    boolean_query(index_path, query_str)
    
    top_left = (30.0, -90.05)
    bottom_right = (29.0, -90.0)
    geospatial_query(index_path, top_left, bottom_right)