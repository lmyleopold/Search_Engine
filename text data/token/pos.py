import nltk
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from utils import business_review_data_sample
from collections import Counter
from visualization import *

sentences = []
pos = {}

if not os.path.exists('./data/B1_review.txt'):
		print("generate B1_review.txt")
		business_review_data_sample(2)
		
with open('./data/B1_review.txt', 'r') as f:
	for line in f:
		sents = sent_tokenize(line)
		for sent in sents:
			sentences.append(len(sent))
			words = word_tokenize(sent)
			pos_tags = nltk.pos_tag(words)
			for item in pos_tags:
				if item[1] not in pos:
					pos[item[1]] = 1
				else:
					pos[item[1]] += 1

sentences_dict = Counter(sentences)
print(sentences_dict)
print(pos)
sentence_plot(sentences_dict)
pos_plot(pos)