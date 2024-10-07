import lucene
import os
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
from index import create_index

# this function use ""QueryParser""
# this function includes keyword, phrase and boolean search
# because QueryParser can search according to the type of query_str ???? the result may not be correct, more experiment
# query_str = "test", keyword query
# query_str = "test test", phrase query
# query_str = "test AND test" boolean query
def normal_query(index_path, query_str, N = 10, search_key = "text", casefold = True, stemming = True, stopword = True):
    print("---------- begin normal query ----------", '\n')
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
    
    print(f"------found {top_docs.totalHits.value} documents, the top {N} as follows:-----")
    for rank, score_doc in enumerate(top_docs.scoreDocs):
        doc_rank = rank + 1
        doc_id = score_doc.doc
        doc_score = score_doc.score
        doc = index_searcher.doc(score_doc.doc)
        print(f"json_type: {doc.get('json_type')}, rank: {doc_rank}, score: {doc_score},\
              docID: {doc_id}, {search_key}: {doc.get(search_key)}", '\n')

    index_reader.close()

#use PhraseQuery for phrase query. if the str only have one word, it is also be keyword query
def phrase_query(index_path, query_str, N = 10, search_key = "text"):
    print("---------- begin phrase query ----------", '\n')
    index_directory = FSDirectory.open(Paths.get(index_path))
    index_reader = DirectoryReader.open(index_directory)
    index_searcher = IndexSearcher(index_reader)

    phrase_query = PhraseQuery.Builder()
    for str in query_str.split():
        phrase_query.add(Term(search_key, str))
    phrase_query = phrase_query.build()

    top_docs = index_searcher.search(phrase_query, N)
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
    print(f"------found {top_docs.totalHits.value} documents, the top {N} as follows:-----")
    for rank, score_doc in enumerate(top_docs.scoreDocs):
        doc_rank = rank + 1
        doc_id = score_doc.doc
        doc_score = score_doc.score
        doc = index_searcher.doc(score_doc.doc)
        print(f"json_type: {doc.get('json_type')}, rank: {doc_rank}, score: {doc_score},\
              docID: {doc_id}, {search_key}: {doc.get(search_key)}", '\n')

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
