import lucene, json
import numpy as np
import random
from nltk.tokenize import sent_tokenize
from java.io import File, StringReader # type: ignore
from java.nio.file import Path, Paths # type: ignore
from org.apache.lucene.store import ByteBuffersDirectory, MMapDirectory, NIOFSDirectory, FSDirectory # type: ignore
from org.apache.lucene.index import IndexOptions, IndexWriter, IndexWriterConfig, DirectoryReader, FieldInfos, MultiFields, MultiTerms, Term # type: ignore
from org.apache.lucene.search import BooleanClause, BooleanQuery, IndexSearcher, TermQuery, PhraseQuery # type: ignore
from org.apache.lucene.queryparser.classic import MultiFieldQueryParser, QueryParser # type: ignore
from org.apache.lucene.analysis.standard import StandardAnalyzer # type: ignore
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_review_sentence_score(review_tfidf, cosine = False):
    if cosine:
        cosine_matrix = cosine_similarity(review_tfidf)
        review_sentence_score = cosine_matrix.mean(axis=1) / np.count_nonzero(review_tfidf, axis=1)
    else:
        review_sentence_score = review_tfidf.sum(axis=1)
        review_sentence_count = np.count_nonzero(review_tfidf, axis=1)
        review_sentence_score = review_sentence_score / review_sentence_count
    return review_sentence_score

# most common in one person, maybe also common in other person,
def get_most_common_sentence(index_path, user_id, N, cosine = False):
    index_directory = FSDirectory.open(Paths.get(index_path))
    index_reader = DirectoryReader.open(index_directory)
    index_searcher = IndexSearcher(index_reader)
    
    query = TermQuery(Term('user_id', user_id))
    top_docs = index_searcher.search(query, N * 100000)
    
    review_sentence = []
    for _, score_doc in enumerate(top_docs.scoreDocs):
        doc_id = score_doc.doc
        doc = index_searcher.doc(doc_id)
        review_sentence.extend(s for s in sent_tokenize(doc.get('text')) if len(s) > 20)
    index_reader.close()

    if len(review_sentence) == 0:
        print(f'user_id: {user_id}, total_review: {top_docs.totalHits.value}, review_sentence: {len(review_sentence)}')
        return None, None

    review_tfidf = TfidfVectorizer().fit_transform(review_sentence).toarray()
    review_sentence_score = get_review_sentence_score(review_tfidf, cosine)
    top_review_sentence_index = np.argsort(review_sentence_score)[-min(N, len(review_sentence)):]

    return [review_sentence[i] for i in top_review_sentence_index], review_sentence

def get_most_representative_sentence(index_path, user_id, N, cosine = False, sample = False):
    all_user_id = set()
    with open('./data/LA_review.jsonl') as f:
        for l in f:
            id = json.loads(l)['user_id']
            all_user_id.add(id)
    if sample:
        all_user_id = random.sample(all_user_id, 100)
        if user_id not in all_user_id:
            all_user_id.append(user_id)
    print(len(all_user_id))
    
    all_user_sentence = []
    all_user_sentence_index = {}
    for id in all_user_id:
        s, _ = get_most_common_sentence(index_path, id, N * 5, cosine)
        if s != None:
            all_user_sentence_index[id] = []
            all_user_sentence_index[id].append(len(all_user_sentence))
            all_user_sentence.extend(s)
            all_user_sentence_index[id].append(len(all_user_sentence))
    
    review_tfidf = TfidfVectorizer().fit_transform(all_user_sentence).toarray()
    review_sentence_score = get_review_sentence_score(review_tfidf, cosine)

    user_sentence_score = np.unique(review_sentence_score[all_user_sentence_index[user_id][0] : all_user_sentence_index[user_id][1]])
    user_sentence = np.unique(all_user_sentence[all_user_sentence_index[user_id][0] : all_user_sentence_index[user_id][1]])
    print(len(user_sentence) == len(user_sentence_score))
    top_review_sentence_index = np.argsort(user_sentence_score)[:min(N, len(user_sentence))]
    
    return [user_sentence[i] for i in top_review_sentence_index], user_sentence


if __name__ == "__main__":
    lucene.initVM()

    index_path = "./data/index"

    # a, b = get_most_common_sentence(index_path, '1HM81n6n4iPIFU5d2Lokhw', 5)

    a, b = get_most_common_sentence(index_path, '1HM81n6n4iPIFU5d2Lokhw', 15, cosine = True)

    print(a)

    a, b = get_most_representative_sentence(index_path, '1HM81n6n4iPIFU5d2Lokhw', 15, cosine = True, sample=True)

    print(a)
