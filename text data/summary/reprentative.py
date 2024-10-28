import lucene, json
import numpy as np
import random
import torch
from nltk.tokenize import word_tokenize, sent_tokenize
from java.nio.file import Paths # type: ignore
from org.apache.lucene.store import FSDirectory # type: ignore
from org.apache.lucene.index import DirectoryReader, Term # type: ignore
from org.apache.lucene.search import IndexSearcher, TermQuery # type: ignore
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertTokenizer, BertModel

def get_review_sentence_score(review_sentence, embedding_type = 'tf-idf'):
    if embedding_type == 'bow':
        embedding = CountVectorizer().fit_transform(review_sentence).toarray()
    elif embedding_type == 'tf-idf':
        embedding = TfidfVectorizer().fit_transform(review_sentence).toarray()
    elif embedding_type == 'ngram':
        embedding = CountVectorizer(ngram_range=(2, 2)).fit_transform(review_sentence).toarray()
    elif embedding_type == 'bert':
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        embedding = []
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        model = BertModel.from_pretrained('bert-base-uncased').to(device)
        inputs = tokenizer(review_sentence, return_tensors='pt', padding=True, truncation=True, max_length=256).to(device)
        with torch.no_grad():
            outputs = model(**inputs)
        cls_embedding = outputs.last_hidden_state[:, 0, :]
        embedding.append(cls_embedding.numpy())
        embedding = np.vstack(embedding)

    cosine_matrix = cosine_similarity(embedding)
    sentence_length = [len(word_tokenize(sentence)) for sentence in review_sentence]
    review_sentence_score = cosine_matrix.mean(axis=1) / sentence_length

    return review_sentence_score

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

# most common in one person, maybe also common in other person,
def get_most_common_sentence(index_path, user_id, N, embedding_type = 'tf-idf'): 
    # review = []
    # with open('./data/LA_review.jsonl') as f:
    #     for l in f:
    #         content = json.loads(l)
    #         if content['user_id'] == user_id:
    #             review.append(content['text'])

    # use search engine
    review = search_instance('user_id', user_id, 'text')

    review_sentence = [s for r in review for s in sent_tokenize(r) if len(s) > 30]

    if len(review_sentence) == 0:
        print(f'user_id: {user_id}, review_sentence: {len(review_sentence)}')
        return None, None

    review_sentence_score = get_review_sentence_score(review_sentence, embedding_type)
    top_review_sentence_index = np.argsort(review_sentence_score)[-min(N, len(review_sentence)):]

    return [review_sentence[i] for i in top_review_sentence_index], review_sentence

def get_most_representative_sentence(index_path, user_id, N, embedding_type = 'tf-idf', sample = False):
    #directly use dataset
    # all_user_id = set()
    # with open('./data/LA_review.jsonl') as f:
    #     for l in f:
    #         id = json.loads(l)['user_id']
    #         all_user_id.add(id)
    
    # use search engine
    all_user_id = set(search_instance('json_type', 'review', 'user_id'))

    print(len(all_user_id))

    if sample:
        all_user_id = random.sample(list(all_user_id), 10)
        if user_id not in all_user_id:
            all_user_id.append(user_id)
    print(len(all_user_id))
    
    all_user_sentence = []
    all_user_sentence_index = {}
    for id in all_user_id:
        s, _ = get_most_common_sentence(index_path, id, N * 10, embedding_type)
        if s != None:
            all_user_sentence_index[id] = []
            all_user_sentence_index[id].append(len(all_user_sentence))
            all_user_sentence.extend(s)
            all_user_sentence_index[id].append(len(all_user_sentence))
    
    review_sentence_score = get_review_sentence_score(all_user_sentence, embedding_type)

    user_sentence_score = np.unique(review_sentence_score[all_user_sentence_index[user_id][0] : all_user_sentence_index[user_id][1]])
    user_sentence = np.unique(all_user_sentence[all_user_sentence_index[user_id][0] : all_user_sentence_index[user_id][1]])
    top_review_sentence_index = np.argsort(user_sentence_score)[-min(N, len(user_sentence)) :]
    
    return [user_sentence[i] for i in top_review_sentence_index], user_sentence


if __name__ == "__main__":
    lucene.initVM()

    index_path = "./data/index"

    user = [('QQtoHnP0cP7nzNnUob_1CQ', 169), ('3JQ8RjMGiT8m5hsBq99Zfw', 167)]
    type = ['bow', 'tf-idf', 'ngram', 'bert']
                
    for item in user:
        for t in type:
            print(f'embedding_type = {t}, user_id = {item[0]}')
            print(f'the 10 most common sentences:')
            a, b = get_most_common_sentence(index_path, item[0], 10, embedding_type=t)
            print(a)
            print(f'the 3 most representative sentences:')
            a, b = get_most_representative_sentence(index_path, item[0], 3, embedding_type=t, sample=True)
            print(a)
            print('------------------------------------')

# [('NWUQCWiY0w97l2mcWq9GAQ', 179), ('J3ldbseGNbmXwCQcy5J0xg', 179), ('h0Jn9rkacf3tGw5BeZMHWA', 178), ('D2EQgPgib4kSHKROuPBLAw', 177), ('AR4iAZuZdShphRC_oS2Slg', 176), ('kulP4rgLtL6FGAOtOgh9pw', 174), ('akih7qRzoyBpv_YMTQjL0A', 174), ('005GchcM1HWBH3SFKrIxBA', 173), ('kgKl_TSwiCJ3iX-g2VP0MQ', 173), ('6JejVLZl5M-IB3UkNTkXtQ', 172), ('vlx1Vn0txmphKLtpK3L52w', 171), ('a0DnfD31lNdiBTY2-YBBFA', 171), ('kIVlnCkkAscCfScYs4y2nQ', 171), ('y9cyIC5VbyQ58WDLGbeDag', 170), ('QQtoHnP0cP7nzNnUob_1CQ', 169), ('U6CknC8K0NTsXn_yLPV6tQ', 168), ('3JQ8RjMGiT8m5hsBq99Zfw', 167), ('kTpLsEWkkX7fRxZPToMsew', 167), ('9XHoOGeGMv9unv-tT2dcxg', 165), ('gZTe6SgFxPDq5hq2fX6iSw', 163)]
