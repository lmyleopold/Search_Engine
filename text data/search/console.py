import lucene
import os
import time
from java.io import StringReader # type: ignore
from java.nio.file import Paths # type: ignore
from org.apache.lucene.store import FSDirectory # type: ignore
from org.apache.lucene.analysis.standard import StandardAnalyzer # type: ignore
from org.apache.lucene.index import DirectoryReader, Term # type: ignore
from org.apache.lucene.search import IndexSearcher, PhraseQuery, BooleanQuery, TermQuery, BooleanClause # type: ignore
from org.apache.lucene.search.highlight import Highlighter, QueryScorer, SimpleFragmenter, SimpleHTMLFormatter  # type: ignore
from org.apache.lucene.queryparser.classic import QueryParser # type: ignore

# 引入查询函数
from index import create_index
# from query import geospatial_query
from query import normal_query, phrase_query, boolean_query, geospatial_query

# console
def search_console(index_path):
    print("Welcome to Search Console!")
    print("Type 'exit' to quit the console.")
    
    # 初始化 Lucene 虚拟机
    lucene.initVM()

    while True:
        # 获取用户的查询类型
        query_type = input("\nEnter query type ('normal', 'phrase', 'boolean', 'geospatial'): ").strip().lower()
        if query_type == 'exit':
            break

        # 获取查询字符串
        if query_type != 'geospatial':
            query_str = input("Enter your search query: ").strip()
            if query_str == 'exit':
                break

        # 获取结果数量 N
        N = input("Enter the number of results to display (default is 10): ").strip()
        if N == 'exit':
            break
        N = int(N) if N.isdigit() else 10
        search_key = "text"

        # 执行不同类型的查询
        if query_type == 'normal':
            search_key = input("Enter the search key (default is 'text'): ").strip()
            normal_query(index_path, query_str, N, search_key)
        elif query_type == 'phrase':
            search_key = input("Enter the search key (default is 'text'): ").strip()
            phrase_query(index_path, query_str, N, search_key)
        elif query_type == 'boolean':
            search_key = input("Enter the search key (default is 'text'): ").strip()
            boolean_query(index_path, query_str, N, search_key)
        elif query_type == 'geospatial':
            # 获取地理空间查询的坐标
            top_left_lat = float(input("Enter top-left latitude: ").strip())
            top_left_long = float(input("Enter top-left longitude: ").strip())
            bottom_right_lat = float(input("Enter bottom-right latitude: ").strip())
            bottom_right_long = float(input("Enter bottom-right longitude: ").strip())
            geospatial_query(index_path, (top_left_lat, top_left_long), (bottom_right_lat, bottom_right_long), N)
        else:
            print("Unknown query type. Please enter 'normal', 'phrase', 'boolean', or 'geospatial'.")

    print("Exiting console. Goodbye!")

# # normal_query
# def normal_query(index_path, query_str, N=10, search_key="text"):
#     print("---------- begin normal query ----------", '\n')

#     # 记录开始时间
#     start_time = time.time()

#     index_directory = FSDirectory.open(Paths.get(index_path))
#     index_reader = DirectoryReader.open(index_directory)
#     index_searcher = IndexSearcher(index_reader)
    
#     analyzer = StandardAnalyzer()
    
#     # 使用 QueryParser 解析查询
#     query = QueryParser(search_key, analyzer).parse(query_str)
    
#     # 执行查询
#     top_docs = index_searcher.search(query, N)

#     # 使用 Highlighter 来生成摘要片段
#     formatter = SimpleHTMLFormatter("<b>", "</b>")  # 定义高亮格式
#     scorer = QueryScorer(query)
#     highlighter = Highlighter(formatter, scorer)
#     highlighter.setTextFragmenter(SimpleFragmenter(50))  # 片段的长度为50个字符

#     # 记录结束时间
#     end_time = time.time()
    
#     # 计算查询时间
#     time_taken = end_time - start_time
#     print(f"Query processed in {time_taken:.2f} seconds")
    
#     # 输出查询结果
#     print(f"------found {top_docs.totalHits.value} documents, the top {N} as follows:-----")
#     for rank, score_doc in enumerate(top_docs.scoreDocs):
#         doc_rank = rank + 1
#         doc_id = score_doc.doc
#         doc_score = score_doc.score
#         doc = index_searcher.doc(score_doc.doc)

#         # 获取要高亮的字段文本
#         text_to_highlight = doc.get(search_key)
#         if text_to_highlight:
#             token_stream = analyzer.tokenStream(search_key, StringReader(text_to_highlight))
#             fragment = highlighter.getBestFragment(token_stream, text_to_highlight)
#             snippet = fragment if fragment else text_to_highlight[:100]
#         else:
#             snippet = "No snippet available"

#         # 打印结果
#         print(f"rank: {doc_rank}, score: {doc_score}, docID: {doc_id}, snippet: {snippet}", '\n')

#     index_reader.close()


# # phrase_query
# def phrase_query(index_path, query_str, N=10, search_key="text"):
#     print("---------- begin phrase query ----------", '\n')

#     # 记录开始时间
#     start_time = time.time()

#     # 打开索引目录
#     index_directory = FSDirectory.open(Paths.get(index_path))
#     index_reader = DirectoryReader.open(index_directory)
#     index_searcher = IndexSearcher(index_reader)

#     # 定义分析器
#     analyzer = StandardAnalyzer()

#     # 创建 PhraseQuery
#     phrase_query = PhraseQuery.Builder()
#     for word in query_str.split():
#         phrase_query.add(Term(search_key, word))
#     phrase_query = phrase_query.build()

#     # 执行查询
#     top_docs = index_searcher.search(phrase_query, N)

#     # 设置高亮工具
#     formatter = SimpleHTMLFormatter("<b>", "</b>")  # 定义高亮格式
#     scorer = QueryScorer(phrase_query)
#     highlighter = Highlighter(formatter, scorer)
#     highlighter.setTextFragmenter(SimpleFragmenter(50))  # 片段的长度为50个字符

#     # 记录结束时间
#     end_time = time.time()
#     print(f"Query processed in {end_time - start_time:.2f} seconds")

#     print(f"------found {top_docs.totalHits.value} documents, the top {N} as follows:-----")

#     for rank, score_doc in enumerate(top_docs.scoreDocs):
#         doc_rank = rank + 1
#         doc_id = score_doc.doc
#         doc_score = score_doc.score
#         doc = index_searcher.doc(score_doc.doc)

#         # 获取需要高亮的字段文本
#         text_to_highlight = doc.get(search_key)
#         if text_to_highlight:
#             # 创建 TokenStream 用于高亮处理
#             token_stream = analyzer.tokenStream(search_key, StringReader(text_to_highlight))
#             # 获取最佳的高亮片段
#             fragment = highlighter.getBestFragment(token_stream, text_to_highlight)
#             snippet = fragment if fragment else text_to_highlight[:100]  # 如果没有高亮片段，则取前100字符
#         else:
#             snippet = "No snippet available"

#         # 打印结果
#         print(f"json_type: {doc.get('json_type')}, rank: {doc_rank}, score: {doc_score}, "
#               f"docID: {doc_id}, snippet: {snippet}", '\n')

#     # 关闭索引读取器
#     index_reader.close()


# # boolean_query
# def boolean_query(index_path, query_str, N=10, search_key="text"):
    # print("---------- begin boolean query ----------", '\n')

    # start_time = time.time()

    # # 打开索引目录和读取器
    # index_directory = FSDirectory.open(Paths.get(index_path))
    # index_reader = DirectoryReader.open(index_directory)
    # index_searcher = IndexSearcher(index_reader)

    # # 定义分析器
    # analyzer = StandardAnalyzer()

    # # 构建 BooleanQuery
    # boolean_query_builder = BooleanQuery.Builder()
    # for term in query_str.split():
    #     boolean_query_builder.add(TermQuery(Term(search_key, term)), BooleanClause.Occur.MUST)  # AND 
    # # 你可以根据需求在上面调整布尔查询的逻辑 (MUST, SHOULD, MUST_NOT)
    # boolean_query = boolean_query_builder.build()

    # # 执行查询
    # top_docs = index_searcher.search(boolean_query, N)

    # # 设置高亮器
    # formatter = SimpleHTMLFormatter("<b>", "</b>")  # 定义高亮的HTML格式
    # scorer = QueryScorer(boolean_query)
    # highlighter = Highlighter(formatter, scorer)
    # highlighter.setTextFragmenter(SimpleFragmenter(50))  # 片段长度设置为50个字符

    # # 记录查询时间
    # end_time = time.time()
    # print(f"Query processed in {end_time - start_time:.2f} seconds")

    # # 输出查询结果
    # print(f"------found {top_docs.totalHits.value} documents, the top {N} as follows:-----")
    # for rank, score_doc in enumerate(top_docs.scoreDocs):
    #     doc_rank = rank + 1
    #     doc_id = score_doc.doc
    #     doc_score = score_doc.score
    #     doc = index_searcher.doc(score_doc.doc)

    #     # 获取需要高亮的字段文本
    #     text_to_highlight = doc.get(search_key)
    #     if text_to_highlight:
    #         # 创建 TokenStream 用于高亮处理
    #         token_stream = analyzer.tokenStream(search_key, StringReader(text_to_highlight))
    #         # 获取最佳高亮片段
    #         fragment = highlighter.getBestFragment(token_stream, text_to_highlight)
    #         snippet = fragment if fragment else text_to_highlight[:100]  # 如果没有高亮，显示前100个字符
    #     else:
    #         snippet = "No snippet available"

    #     # 打印结果
    #     print(f"json_type: {doc.get('json_type')}, rank: {doc_rank}, score: {doc_score}, "
    #           f"docID: {doc_id}, snippet: {snippet}", '\n')

    # # 关闭索引读取器
    # index_reader.close()

    

if __name__ == "__main__":
    index_path = "./data/index"
    
    if not os.path.exists(index_path):
        create_index(index_path, casefold=True, stemming=True, stopword=True)

    # 启动 console
    search_console(index_path)
