import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import numpy as np

#Bar Plot of length distribution with Log Scale
def bar_plot_length_distribution(List, freq, stack = True):
    label = ["Token Length before Stemming", "Token Length after Stemming"]
    color=['#1f77b4', '#ff7f0e']
    plt.figure(figsize=(12, 6))
    if stack == False:
        width = 0.35
        plt.bar([L - width / 2 for L in List[0]], freq[0], alpha=0.7, label=label[0], color = color[0], width = width)
        plt.bar([L + width / 2 for L in List[1]], freq[1], alpha=0.7, label=label[1], color = color[1], width = width)
    else:
        plt.bar(List[0], freq[0], alpha=0.7, label=label[0], color = color[0], width = 0.7)
        plt.bar(List[1], freq[1], alpha=0.7, label=label[1], color = color[1], width = 0.7)
    plt.xlim(0, None)
    plt.yscale('log') 
    plt.ylim(0, None)
    plt.legend()
    plt.title("Token Length Distribution")
    plt.xlabel("Token Length")
    plt.ylabel("Frequency (Log Scale)")
    plt.show()

#bar plot of top words
def bar_plot_top_word(dict, top = 6):
    dict0 = sorted(dict[0].items(), key = lambda item: item[1], reverse = True)
    dict1 = sorted(dict[1].items(), key = lambda item: item[1], reverse = True)
    x0, y0, x1, y1 = [],[],[],[]
    for i in range(top):
        x0.append(dict0[i][0])
        y0.append(dict0[i][1])
        x1.append(dict1[i][0])
        y1.append(dict1[i][1])

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(x0, y0, alpha=0.7)
    plt.xticks(rotation=45)
    plt.title("Top 10 Most Frequent Words Before Stemming")
    plt.xlabel("Word")
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    plt.bar(x1, y1, alpha=0.7)
    plt.title("Top 10 Most Frequent Words After Stemming")
    plt.xticks(rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.show()

#word cloud
def word_cloud(dict):
    wordcloud_before = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict[0])
    wordcloud_after = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict[1])

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(wordcloud_before, interpolation='bilinear')
    plt.title("Before Stemming")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(wordcloud_after, interpolation='bilinear')
    plt.title("After Stemming")
    plt.axis('off')
    plt.show()

#POS
def pos_plot(dict):
    dict = sorted(dict.items(), key = lambda item: item[1], reverse = True)
    x0, y0 = [],[]
    for i in range(len(dict)):
        x0.append(dict[i][0])
        y0.append(dict[i][1])
    
    plt.figure(figsize=(12, 6))
    plt.bar(x0, y0, alpha=0.7, width = 0.7)
    plt.xticks(rotation=90)
    plt.title("Pos Tag Distribution")
    plt.xlabel("POS Tag", fontsize=10)
    plt.ylabel("Frequency")
    plt.yscale('log') 
    plt.ylim(0, None)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.show()

#sentence_length
def sentence_plot(dict):
    dict = sorted(dict.items(), key = lambda item: item[0], reverse = True)
    x0, y0 = [],[]
    for i in range(len(dict)):
        if dict[i][0] < 500:
            x0.append(dict[i][0])
            y0.append(dict[i][1])
    
    plt.figure(figsize=(12, 6))
    plt.hist(x0, weights=y0, bins=len(x0), alpha=0.7)
    plt.xlim(0, None)
    plt.yscale('log') 
    plt.ylim(0, None)
    plt.title("Sentence Length Distribution")
    plt.xlabel("Sentence Length")
    plt.ylabel("Frequency (Log Scale)")
    plt.show()

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 34, 35, 43, 45, 49]
    b = [79758, 69818, 114212, 86272, 53979, 33850, 34067, 14067, 12056, 7331, 3370, 1193, 762, 291, 224, 50, 19, 15, 14, 7, 4, 3, 5, 2, 4, 1, 1, 1, 1, 1, 1, 2, 1, 1]
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 34, 43, 45, 47]
    d = [79758, 84900, 108876, 102677, 60633, 39982, 19073, 8392, 4625, 1668, 340, 196, 93, 61, 38, 12, 8, 14, 7, 6, 2, 6, 2, 1, 3, 4, 2, 2, 1, 1]

    bar_plot_length_distribution([a, c], [b, d], stack=False)

    a = {'leroy': 31, 'regret': 31, 'worse': 31, 'round': 31, 'issue': 31, 'scampi': 30, 'ribeye': 30, 'flavorless': 30, 'patrons': 30, 'moment': 30, 'air': 30, 'tough': 30, 'seeing': 30, 'purchase': 30, 'advice': 30, 'changed': 30, 'option': 30, 'lack': 30, 'opted': 30, 'certainly': 30, 'bathroom': 30, 'stopping': 30, 'julep': 30, 'multiple': 30, 'mention': 30, 'na': 30, 'bigger': 30, 'prior': 30, 'coffee': 30, 'ten': 30, 'available': 30, 'etc': 29, 'tea': 29, 'ingredients': 29, 'shrimps': 29, 'brownie': 29, 'goes': 29, 'cleaned': 29, 'guests': 29, 'sense': 29, 'cheap': 29, 'beat': 29, 'parade': 29, 'spend': 29, 'underwhelming': 29, 'similar': 29, 'brunch': 29, 'coleslaw': 29, 'means': 29, 'complaint': 29, 'thursday': 29, 'bunch': 28, 'followed': 28, 'soak': 28, 'date': 28, 'cut': 28, 'move': 28, 'regular': 28, 'receive': 28, 'number': 28, 'beers': 28, 'toasted': 28, 'send': 28, 'welcome': 28, 'ton': 28, 'conversation': 28, 'disgusting': 28, 'unless': 28, 'plain': 28, 'decide': 28, 'marys': 28, 'positive': 28, 'treated': 28, 'reservation': 28, 'tons': 28}
    bar_plot_top_word([a, a])