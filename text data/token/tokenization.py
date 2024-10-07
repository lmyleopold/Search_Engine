import nltk
import os
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from utils import business_review_data_sample
from nltk.stem import PorterStemmer
from collections import Counter
from visualization import *

#default isalpha and exclude stopword
def tokenize(isalpha = True, stopword = True):
	#if not os.path.exists('./data/B1_review.txt'):
	print("generate B1_review.txt")
	business_review_data_sample(2)
	print("finish generating B1_review.txt")

	stop_words = set(stopwords.words('english'))
	token_before = [] #words before stem, contain the same words
	with open('./data/B1_review.txt', 'r', encoding='utf-8') as f:
		for line in f:
			token_before.extend([token.lower() for token in word_tokenize(line) if (not isalpha or token.isalpha()) and (not stopword or token.lower() not in stop_words)])

	print("end tokenizing, contains", len(token_before), "tokens")
	ps = PorterStemmer()
	token_after = [ps.stem(token) for token in token_before] #words after token
	print("end stemming, contains", len(token_after), "tokens")

	token_before_dict = Counter(token_before) #dict
	token_after_dict = Counter(token_after)

	token_before_list = list(token_before_dict.keys()) #contain distinct words before stem
	token_before_freq = [token_before_dict[token] for token in token_before_list]
	token_after_list = list(token_after_dict.keys())
	token_after_freq = [token_after_dict[token] for token in token_after_list]

	print("before stemming, contain", len(token_before_list), "word types")
	print("after stemming, contain", len(token_after_list), "word types")

	token_length_before_dict = Counter(len(token) for token in token_before)
	token_length_after_dict = Counter(len(token) for token in token_after)

	token_length_before_list = sorted(token_length_before_dict.keys())
	token_length_before_freq = [token_length_before_dict[length] for length in token_length_before_list]
	token_length_after_list = sorted(token_length_after_dict.keys())
	token_length_after_freq = [token_length_after_dict[length] for length in token_length_after_list]

	print(token_length_before_list)
	print(token_length_before_freq)
	print(token_length_after_list)
	print(token_length_after_freq)
	return (token_before, token_after, token_before_dict, token_after_dict, 
		 token_length_before_list, token_length_before_freq, token_length_after_list,token_length_after_freq)

if __name__ == '__main__':
	token_before, token_after, token_before_dict, token_after_dict, token_length_before_list, token_length_before_freq, token_length_after_list,token_length_after_freq = tokenize(True, True)
	bar_plot_length_distribution([token_length_before_list, token_length_after_list], 
			[token_length_before_freq, token_length_after_freq], True)
	bar_plot_length_distribution([token_length_before_list, token_length_after_list], 
			[token_length_before_freq, token_length_after_freq], False)
	word_cloud([token_before_dict, token_after_dict])
	bar_plot_top_word([token_before_dict, token_after_dict], top=10)