# **3.2 Dataset Analysis**

## **3.2.1 Data Sampling**

> 1. sample businesses and reviews from one of these areas.
> 2. construct a dataset exclusively for the chosen area, containing only the businesses located within it and their associated reviews
>

 

## **3.2.2 Tokenization and Stemming**

> #### A
>
> 1. Randomly select a business *b*1 from the sampled dataset and extract all reviews associated with *b*1 to form a small dataset *B*1.
> 2. Display the word frequency distributions in *B*1 before and after applying stemming.
> 3. plot the word frequency distributions on a log scale (experiment with different visualizations to best present your data and insights).
>
> #### B
>
> 1. Repeat the process for another randomly selected business, *b*2, 
> 2. ***compare the findings between the two businesses using the generated plots.***
>
> #### C
>
> 1. ***list the top 10 most frequent words (excluding stopwords) before and after stemming for both businesses.***
> 2. ***Provide a discussion of your findings based on these results.***
>

### *Analysis of Tokenization and Stemming Impact on Business Review Data*

Tokenization is a critical step in natural language processing that breaks down text into smaller units, such as words or phrases, for computational analysis. In this project, customer review data from two businesses, **B1** and **B2**, was tokenized and subsequently stemmed using the `PorterStemmer` from the NLTK library. Stemming reduces words to their base forms by removing suffixes, creating more uniform representations.

### Token Length Distribution

<img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241006180436293.png" alt="image-20241006180436293" style="zoom:25%;" /><img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241006180449421.png" alt="image-20241006180449421" style="zoom:25%;" />

<img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241006180557929.png" alt="image-20241006180557929" style="zoom:25%;" /><img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241006180610131.png" alt="image-20241006180610131" style="zoom:25%;" />

Figures 1 and 2 represent the token length distributions for **B1** and **B2** respectively, before and after stemming. In both cases, the token distributions exhibit similar trends:

1. **High Frequency of Short Tokens**: Tokens with lengths between 2 and 5 characters are the most frequent. This is expected in natural language processing, as common English words such as "the", "and", "is", and "in" tend to be shorter in length. 

2. **Exponential Decline for Longer Tokens**: As token length increases beyond 10 characters, the frequency of occurrence declines rapidly. This pattern is consistent across both businesses, indicating that longer words are less common, likely domain-specific terms or compound words.

3. **Effect of Stemming**: After stemming, both **B1** and **B2** show similar trends in reduced token length variability, particularly for tokens around 5 to 7 characters. The stemming process helps consolidate different forms of the same root word, such as "services" and "service", into a single base form, resulting in more frequent shorter tokens.

**Comparison Between B1 and B2**:  
Although both businesses follow similar patterns in token length distribution, **B2** appears to have a slightly higher frequency of shorter tokens after stemming, suggesting that reviews for **B2** may involve more concise language or a higher presence of root forms. **B1**, on the other hand, retains a slightly broader distribution of longer tokens, indicating potentially more varied vocabulary in the reviews.

### Word Cloud and Top 10 Word Frequency Analysis

<img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241006180506607.png" alt="image-20241006180506607" style="zoom:25%;" />

<img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241006180639436.png" alt="image-20241006180639436" style="zoom:25%;" />

Figures 3 and 4 showcase the word clouds for **B1** and **B2**, illustrating the most frequent terms before and after stemming. Both businesses share common keywords like "food", "good", "great", and "service", reflecting an overall focus on dining experience and food quality. However, distinct themes emerge for each business:

- **B1** features "oysters" prominently, suggesting a heavy emphasis on seafood, particularly oysters.  
- **B2**, on the other hand, highlights "breakfast" and "eggs", indicating a focus on breakfast items.

After stemming, the word clouds show a simplification in word forms, reducing "ordered" to "order" and "services" to "servic". This leads to more uniform word forms but may lose some nuance in tense or plurality.

<img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241006180525595.png" alt="image-20241006180525595" style="zoom:25%;" />

<img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241006180652817.png" alt="image-20241006180652817" style="zoom:25%;" />

Figures 5 and 6 further support these insights by presenting the top 10 most frequent words before and after stemming. In **B1**, the focus on seafood remains strong with "oysters" being one of the top terms, along with general words like "food", "good", and "service". **B2**, in contrast, places more emphasis on terms like "breakfast", "wait", and "eggs", indicating customer attention on breakfast items and potentially service timing.

**Key Differences Between B1 and B2**:

- **B1**'s reviews are more seafood-centric, particularly around oysters, reflecting a unique menu focus.
- **B2**'s reviews reveal a stronger association with breakfast-related terms and the service experience, such as wait times, which could indicate different peak hours or customer expectations.

Overall, the word clouds and frequency distributions provide a clear distinction in customer priorities and menu focus between the two businesses, while also highlighting common themes of food quality and service.

### Conclusion

The analysis of token length distribution, word clouds, and word frequency highlights both commonalities and differences in the customer review data for **B1** and **B2**. While both businesses share core review topics related to food quality and service, **B1** is more seafood-focused, and **B2** seems to cater more to breakfast-oriented customers. The stemming process has effectively normalized word forms across both datasets, providing a more consistent basis for further text analysis. However, careful attention must be paid to the loss of some semantic detail, such as tense or pluralization, due to stemming.

### sentence segmentation

Sentence segmentation is a process used to identify the boundaries of individual sentences. Typically, sentences are divided by certain punctuation marks, such as periods and question marks. Before performing Part-of-Speech (POS) tagging, it is essential to conduct sentence segment first. In this assignment, we use the NLTK library for sentence segmentation. The results of these two businesses are illustrated in Fig. 2.

Analysis : Firstly, we can discover that most sentence lengths are lower than 150, with a length of 40 being the most frequent. This distribution corresponds to people's daily speech patterns, suggesting there is no significant difference between these two business reviews. Such consistency indicates that the reviews are straightforward and assesible, reflecting common conversational styles.

![img](https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/wps1.jpg) 

Figure 2a: Sentence Length Distribution in B1 business reviews

![img](https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/wps2.jpg) 

Figure 2b: Sentence Length Distribution in B1 business reviews

### POS tagging

The purpose of POS tagging is to assign a part of speech to each word in a sentence. This task, often conducted after sentence segmentation, is fundamental because it helps understand the structure of a sentence and provides insights into the relationships between words. We analyze the distribution of POS tags in the businesses' reviews by NLTK library, and the results are shown as Fig. 3.

Analysis: From figure3, we can see that the frequency of NN and JJ are significantly high which indicates that most sentences in reviews are descriptive languages and focus primarily on subjects. Furthermore, the overall distribution of POS tags in these two business reviews is similar and the diversity of tags is abundant, reflecting dynamic linguistic patterns and comparable styles. 

![img](https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/wps3.jpg)

Figure 3a: POS Tag Distribution in B1 business reviews

![img](https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/wps4.jpg) 

Figure 3b: POS Tag Distribution in B2 business reviews



## **3.2.3 Writing Style**

> 1. Randomly sample the following: (i) two posts from StackOverflow, (ii) two posts from Reddit, (iii) two news articles from Straits Times, and (iv) two patents in any domain.
> 2. ***Discuss the differences on their writing styles***
>

https://stackoverflow.com/questions/5963269/how-to-make-a-great-r-reproducible-example

https://stackoverflow.com/questions/513832/how-do-i-compare-strings-in-java

Both Stack Overflow pages demonstrate good writing practices, following standard rules for capitalization, grammar, and punctuation. Each sentence starts with a capital letter, and proper nouns are correctly capitalized. Relevant code snippets are frequently included to demonstrate concepts, enhancing understanding through practical examples. Important concepts are often highlighted using bold or italic text, drawing attention to key points. Additionally, code examples usually contain explanatory comments that clarify what each part does, making it easier for readers to follow along. One of two posts is organized with descriptive section headings, which helps guide readers through the content. What’s more, the writing maintains a neutral and objective tone, avoiding personal opinions in favor of factual guidance.

 https://www.reddit.com/r/Futurology/comments/qffjqm/new_research_from_oxford_university_suggests_that/

https://www.reddit.com/r/science/comments/7e1jo1/raising_the_taxes_of_graduate_students_by_as_much/

Both posts employ a conversational and informal tone. Most sentences begin with a capitalized word, and proper nouns are correctly capitalized, adhering to standard grammar conventions. However, some sentences start with lowercase letters, adding to the casual feel. The formatting varies, with some users utilizing bullet points or line breaks to enhance readability. Key points are often emphasized using bold or italic text. Throughout, the language remains casual and accessible. Additionally, users often engage in debate-style responses, directly addressing or arguing with each other's points. Many comments are short and to the point, typically consisting of just a sentence or two. There's also a frequent use of humor and sarcasm, with attempts at wit, jokes, and playful remarks.

https://www.straitstimes.com/world/middle-east/food-aid-to-gaza-falls-as-israel-sets-new-aid-rule-sources

https://www.straitstimes.com/world/middle-east/gaza-and-a-ceasefire-slip-out-of-focus-as-lebanon-conflict-rages

Straits Times news articles use everyday vocabulary and simpler sentence structures for the sake of readability and accessibility. They also follow the basic writing format conventions, such as capitalizing the first word in a sentence. The news is written in an objective and neutral tone from a third person perspective, focusing on reporting facts rather than subjective value judgements. However, one of the article includes quotes from government officials and local civilians to convey their opinions. 

https://patentimages.storage.googleapis.com/48/13/18/d69ced9231b763/US11379296.pdf

https://patentimages.storage.googleapis.com/8e/5a/f5/55fb42a72eade4/US10938515.pdf

These two patents strictly adhere to a formulaic format. Overall, the patents demonstrate a clear structure, coherent logical flow, and proper use of  grammar. This regime includes several figures to concisely introduce each module. Then the patents elaborate on the corresponding details in a precise and formal manner, using specific and technical terminology and the passive tense to illustrate certain mechanisms or procedures. Additionally, unique reference numbers are assigned every five lines to clarify designations and minimize ambiguity.

# **3.3 Development of a Search Engine**

## 3.3.1 Write a search engine to index and search reviews

> #### A
>
> 1. Keyword search of business
>
>    *e.g.,* searching for restaurants by words in their names.
>
> 2. Keyword search of reviews
>
>    *e.g.,* searching for reviews that contain certain keywords or phrases.
>
> 3. Geospatial search
>
>    *e.g.,* searching for businesses located within a geospatial area defined by a bounding box.
>
> #### B
>
> 1. ***Detail your definition of “document” in your indexing,*** 
> 2. your choice of parsing/linguistic processing on the words/terms in the chosen fields
>
> #### C
>
> 1. collect the time needed to index every 10% of the documents
> 2. Discuss your findings on the indexing time.
>
> #### D
>
> 1. ***return top N (the number of N is configurable) results for each search via the console along with rank, scores, docID, and snippets whenever possible.***
> 2. Discuss whether the results returned by the search engine are as expected with sample queries.
> 3. record the time taken to process a query.
>





index.py运行结果

```
INFO: Using MemorySegmentIndexInput with Java 19; to disable start with -Dorg.apache.lucene.store.MMapDirectory.enableMemorySegments=false
---------- begin creating index ----------
Indexed 77159 documents in 7.64 seconds
Indexed 154318 documents in 14.82 seconds
Indexed 231477 documents in 22.16 seconds
Indexed 308636 documents in 29.43 seconds
Indexed 385795 documents in 36.66 seconds
Indexed 462954 documents in 44.02 seconds
Indexed 540113 documents in 51.24 seconds
Indexed 617272 documents in 66.13 seconds
Indexed 694431 documents in 73.23 seconds
Indexed 771590 documents in 80.32 seconds
--------- finish creating index ---------
---------the function of index_directory-----------
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_jobject', 'boxfn_', 'cast_', 'class', 'class_', 'close', 'copyFrom', 'createOutput', 'createTempOutput', 'deleteFile', 'deletePendingFiles', 'directory', 'equals', 'fileLength', 'getClass', 'getDirectory', 'getPendingDeletions', 'hashCode', 'instance_', 'listAll', 'listAll_', 'notify', 'notifyAll', 'obtainLock', 'open', 'openChecksumInput', 'openInput', 'pendingDeletions', 'rename', 'sync', 'syncMetaData', 'toString', 'wait', 'wrapfn_'] 

---------the function of index_reader-----------
['CacheHelper', 'CacheKey', 'ClosedListener', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_jobject', 'boxfn_', 'cast_', 'class', 'class_', 'close', 'context', 'current', 'decRef', 'directory', 'docFreq', 'document', 'equals', 'getClass', 'getContext', 'getDocCount', 'getIndexCommit', 'getReaderCacheHelper', 'getRefCount', 'getSumDocFreq', 'getSumTotalTermFreq', 'getTermVector', 'getTermVectors', 'getVersion', 'hasDeletions', 'hashCode', 'incRef', 'indexCommit', 'indexExists', 'instance_', 'isCurrent', 'leaves', 'listCommits', 'maxDoc', 'notify', 'notifyAll', 'numDeletedDocs', 'numDocs', 'of_', 'open', 'openIfChanged', 'parameters_', 'readerCacheHelper', 'refCount', 'registerParentReader', 'storedFields', 'termVectors', 'toString', 'totalTermFreq', 'tryIncRef', 'version', 'wait', 'wrapfn_'] 

---------the number of document -----------
771597 

------the forward 10 businesses' name:------
document ID: 0, business name: Herb Import Co
document ID: 1, business name: Nifty Car Rental
document ID: 2, business name: River 127
document ID: 3, business name: Lafitte's Landing Seafood House
document ID: 4, business name: New Orleans Spirit Tours
document ID: 5, business name: Copper Vine
document ID: 6, business name: Riverview Room
document ID: 7, business name: Mahony's Po-Boys & Seafood
document ID: 8, business name: Monogram Express
document ID: 9, business name: Sears Auto Center
```

query.py运行结果

```
INFO: Using MemorySegmentIndexInput with Java 19; to disable start with -Dorg.apache.lucene.store.MMapDirectory.enableMemorySegments=false
---------- begin normal query ---------- 

Query processed in 0.11 seconds
------found 1042 documents, the top 10 as follows:-----
json_type: review, rank: 1, score: 3.4009456634521484,              docID: 96205, text: A nice diner feel breakfast restaurant in the French Quarter.  Nothing fancy, but good breakfast menu and good service.  Small restaurant with tables only, no booths.  Good for a quick, filling and good breakfast. 

json_type: review, rank: 2, score: 3.3496389389038086,              docID: 247637, text: We had breakfast here, and it was very good.  The menu has local twists on traditional breakfast entrees.  Thus you will find seafood in some of the breakfast dishes, and a lot of the breakfast entrees have a sauce on them (Hollandaise for example).  So the dishes are not plain Waffle House types of breakfast dishes, but rather the Chef's own interpretation of various classic breakfast entrees.  All very good, with excellent service that is friendly, but not over bearing.  If you want something different for breakfast or lunch, this is a good choice. 

json_type: review, rank: 3, score: 3.3422329425811768,              docID: 705692, text: Good breakfast spot in the French Quarter. Good good, good service. More traditional breakfast option with less emphasis on Cajun cuisine. 

json_type: review, rank: 4, score: 3.304903984069824,              docID: 417023, text: Solid for breakfast.  Good doughnuts and cinnamon rolls and also good breakfast sandwiches made to order. 

json_type: review, rank: 5, score: 3.298600196838379,              docID: 449831, text: Best breakfast I've ever had... I had the boudin hash breakfast special. My daughter had the boudin breakfast sandwich, also very good.. don't expect anything fancy...just good home cooked food, reasonably priced 

json_type: review, rank: 6, score: 3.2895843982696533,              docID: 622664, text: Pretty good breakfast. Very busy on a Friday morning! I had a burrito and my friend had a breakfast bowl. She loved loved loved her breakfast bowl. The flavor was delicious and the serving size good. My burrito was decent I'd suggest mAybe getting something a little bigger as it wasnt that filling.  But all in all a good breakfast spot. 

json_type: review, rank: 7, score: 3.2866106033325195,              docID: 421058, text: This place is a must for breakfast!!!  Breakfast was awesome!  Some good Cajun food too for breakfast.  Big portions. 

json_type: review, rank: 8, score: 3.280959129333496,              docID: 26419, text: Want some good breakfast, then come here.  All of the breakfast items are really good.  Can't go wrong. 

json_type: review, rank: 9, score: 3.2630159854888916,              docID: 101572, text: Nice breakfast spot, good coffee and nice choice of breakfast sandwiches.  Clean, "techno" atmosphere populated by hipsters.  Has the patina of a franchise.  Good possible breakfast spot with convenient parking.  My new alternative during peak demand times. 

json_type: review, rank: 10, score: 3.254242420196533,              docID: 150897, text: Great food. Good service.  Enjoyed breakfast with my dad!!!!! I had the traditional Eggs Benedict sub ham for chicken with breakfast potatoes. Dad had omelet with breakfast potatoes. Both were equally delicious. Music pretty good playlist...old school. 

---------- begin phrase query ---------- 

Query processed in 0.02 seconds
------found 854 documents, the top 10 as follows:-----
json_type: review, rank: 1, score: 3.2456858158111572,              docID: 82829, text: Good breakfast spot and close to MSY airport. 
Friendly people and fun atmosphere with good breakfast food.
Recommend the Beignet sticks! 

json_type: review, rank: 2, score: 3.101207733154297,              docID: 96205, text: A nice diner feel breakfast restaurant in the French Quarter.  Nothing fancy, but good breakfast menu and good service.  Small restaurant with tables only, no booths.  Good for a quick, filling and good breakfast. 

json_type: review, rank: 3, score: 3.0696749687194824,              docID: 174661, text: Best iced coffee in New Orleans. I would give it 5 stars but they don't have good breakfast options with the coffee. There are a couple places within a block where you can get good breakfast though. 

json_type: review, rank: 4, score: 2.9433975219726562,              docID: 708488, text: Had a really good breakfast with reasonable prices. 

json_type: review, rank: 5, score: 2.9243898391723633,              docID: 493960, text: Good breakfast; good flavorful food!  Nice vibe.  Friendly service 

json_type: review, rank: 6, score: 2.905625820159912,              docID: 477913, text: Pretty good breakfast despite average service and very small space. 

json_type: review, rank: 7, score: 2.8871009349823,              docID: 430955, text: Thanks Great restaurant, friendly staff good breakfast!, delicious pancakes and sausage!!! 

json_type: review, rank: 8, score: 2.8871009349823,              docID: 497470, text: Good breakfast my first time there - I'll try it again soon. 

json_type: review, rank: 9, score: 2.8839564323425293,              docID: 124723, text: Great food! Only removed one star bc my water cup was a little dirty and the waiter seemed a little snappy. But I loved the food! I finally got a good breakfast without eggs in it! The Brie and grilled ham were the highlights! Good breakfast, but small so go early or expect a little wait. 

json_type: review, rank: 10, score: 2.8688111305236816,              docID: 208116, text: Cozy cafe in the Treme. Good breakfast sandwiches in a relaxed atmosphere. 

---------- begin boolean query ---------- 

Query processed in 0.02 seconds
------found 15353 documents, the top 10 as follows:-----
json_type: review, rank: 1, score: 3.4009456634521484,              docID: 96205, text: A nice diner feel breakfast restaurant in the French Quarter.  Nothing fancy, but good breakfast menu and good service.  Small restaurant with tables only, no booths.  Good for a quick, filling and good breakfast. 

json_type: review, rank: 2, score: 3.3496389389038086,              docID: 247637, text: We had breakfast here, and it was very good.  The menu has local twists on traditional breakfast entrees.  Thus you will find seafood in some of the breakfast dishes, and a lot of the breakfast entrees have a sauce on them (Hollandaise for example).  So the dishes are not plain Waffle House types of breakfast dishes, but rather the Chef's own interpretation of various classic breakfast entrees.  All very good, with excellent service that is friendly, but not over bearing.  If you want something different for breakfast or lunch, this is a good choice. 

json_type: review, rank: 3, score: 3.3422329425811768,              docID: 705692, text: Good breakfast spot in the French Quarter. Good good, good service. More traditional breakfast option with less emphasis on Cajun cuisine. 

json_type: review, rank: 4, score: 3.304903984069824,              docID: 417023, text: Solid for breakfast.  Good doughnuts and cinnamon rolls and also good breakfast sandwiches made to order. 

json_type: review, rank: 5, score: 3.298600196838379,              docID: 449831, text: Best breakfast I've ever had... I had the boudin hash breakfast special. My daughter had the boudin breakfast sandwich, also very good.. don't expect anything fancy...just good home cooked food, reasonably priced 

json_type: review, rank: 6, score: 3.2895843982696533,              docID: 622664, text: Pretty good breakfast. Very busy on a Friday morning! I had a burrito and my friend had a breakfast bowl. She loved loved loved her breakfast bowl. The flavor was delicious and the serving size good. My burrito was decent I'd suggest mAybe getting something a little bigger as it wasnt that filling.  But all in all a good breakfast spot. 

json_type: review, rank: 7, score: 3.2866106033325195,              docID: 421058, text: This place is a must for breakfast!!!  Breakfast was awesome!  Some good Cajun food too for breakfast.  Big portions. 

json_type: review, rank: 8, score: 3.280959129333496,              docID: 26419, text: Want some good breakfast, then come here.  All of the breakfast items are really good.  Can't go wrong. 

json_type: review, rank: 9, score: 3.2630159854888916,              docID: 101572, text: Nice breakfast spot, good coffee and nice choice of breakfast sandwiches.  Clean, "techno" atmosphere populated by hipsters.  Has the patina of a franchise.  Good possible breakfast spot with convenient parking.  My new alternative during peak demand times. 

json_type: review, rank: 10, score: 3.254242420196533,              docID: 150897, text: Great food. Good service.  Enjoyed breakfast with my dad!!!!! I had the traditional Eggs Benedict sub ham for chicken with breakfast potatoes. Dad had omelet with breakfast potatoes. Both were equally delicious. Music pretty good playlist...old school. 

---------- begin geospatial query ---------- 

Query processed in 0.01 seconds
------found 728 businesses, the top 10 as follows:-----
json_type: business, rank: 1, score: 2.0, docID: 3, name: Lafitte's Landing Seafood House, latitude: 29.8754822266, longitude: -90.04938 

json_type: business, rank: 2, score: 2.0, docID: 12, name: Domino's Pizza, latitude: 29.8753202, longitude: -90.045817 

json_type: business, rank: 3, score: 2.0, docID: 21, name: The Music Box Village, latitude: 29.9635911, longitude: -90.0292571 

json_type: business, rank: 4, score: 2.0, docID: 45, name: Frady's One Stop Food Store, latitude: 29.963974, longitude: -90.0426042 

json_type: business, rank: 5, score: 2.0, docID: 52, name: Factotum Barber + Supply, latitude: 29.9649841114, longitude: -90.0422938596 

json_type: business, rank: 6, score: 2.0, docID: 92, name: New Orleans Hamburger & Seafood Co., latitude: 29.8768457, longitude: -90.0482728 

json_type: business, rank: 7, score: 2.0, docID: 107, name: Zydeco's, latitude: 29.8777671, longitude: -90.0173044 

json_type: business, rank: 8, score: 2.0, docID: 121, name: Suis Generis, latitude: 29.9649909096, longitude: -90.0426163126 

json_type: business, rank: 9, score: 2.0, docID: 154, name: Terry Parkway Animal Hospital, latitude: 29.902336, longitude: -90.0307482 

json_type: business, rank: 10, score: 2.0, docID: 162, name: Petite Clouet Cafe, latitude: 29.963326, longitude: -90.0454062
```

console.py运行结果

```
Welcome to Search Console!
Type 'exit' to quit the console.
Oct 13, 2024 8:43:43 AM org.apache.lucene.store.MemorySegmentIndexInputProvider <init>
INFO: Using MemorySegmentIndexInput with Java 19; to disable start with -Dorg.apache.lucene.store.MMapDirectory.enableMemorySegments=false

Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): normal
Enter your search query: good breakfast
Enter the number of results to display (default is 10): 
---------- begin normal query ---------- 

Query processed in 0.14 seconds
------found 1042 documents, the top 10 as follows:-----
rank: 1, score: 3.4009456634521484, docID: 96205, snippet:  French Quarter.  Nothing fancy, but <b>good</b> <b>breakfast</b> 

rank: 2, score: 3.3496389389038086, docID: 247637, snippet: We had <b>breakfast</b> here, and it was very <b>good</b>.  The 

rank: 3, score: 3.3422329425811768, docID: 705692, snippet: <b>Good</b> <b>breakfast</b> spot in the French Quarter. <b>Good</b> 

rank: 4, score: 3.304903984069824, docID: 417023, snippet: Solid for <b>breakfast</b>.  <b>Good</b> doughnuts and cinnamon 

rank: 5, score: 3.298600196838379, docID: 449831, snippet:  <b>breakfast</b> sandwich, also very <b>good</b>.. don't expect 

rank: 6, score: 3.2895843982696533, docID: 622664, snippet: Pretty <b>good</b> <b>breakfast</b>. Very busy on a Friday 

rank: 7, score: 3.2866106033325195, docID: 421058, snippet: This place is a must for <b>breakfast</b>!!!  <b>Breakfast</b> 

rank: 8, score: 3.280959129333496, docID: 26419, snippet: Want some <b>good</b> <b>breakfast</b>, then come here.  All of 

rank: 9, score: 3.2630159854888916, docID: 101572, snippet: Nice <b>breakfast</b> spot, <b>good</b> coffee and nice choice 

rank: 10, score: 3.254242420196533, docID: 150897, snippet: Great food. <b>Good</b> service.  Enjoyed <b>breakfast</b> with 


Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): phrase
Enter your search query: good breakfast
Enter the number of results to display (default is 10): 2
---------- begin phrase query ---------- 

Query processed in 0.05 seconds
------found 854 documents, the top 2 as follows:-----
json_type: review, rank: 1, score: 3.2456858158111572,              docID: 82829, text: Good breakfast spot and close to MSY airport. 
Friendly people and fun atmosphere with good breakfast food.
Recommend the Beignet sticks! 

json_type: review, rank: 2, score: 3.101207733154297,              docID: 96205, text: A nice diner feel breakfast restaurant in the French Quarter.  Nothing fancy, but good breakfast menu and good service.  Small restaurant with tables only, no booths.  Good for a quick, filling and good breakfast. 


Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): boolean
Enter your search query: good breakfast
Enter the number of results to display (default is 10): 3
---------- begin boolean query ---------- 

Query processed in 0.02 seconds
------found 12549 documents, the top 3 as follows:-----
json_type: review, rank: 1, score: 3.4009456634521484,              docID: 96205, text: A nice diner feel breakfast restaurant in the French Quarter.  Nothing fancy, but good breakfast menu and good service.  Small restaurant with tables only, no booths.  Good for a quick, filling and good breakfast. 

json_type: review, rank: 2, score: 3.3496389389038086,              docID: 247637, text: We had breakfast here, and it was very good.  The menu has local twists on traditional breakfast entrees.  Thus you will find seafood in some of the breakfast dishes, and a lot of the breakfast entrees have a sauce on them (Hollandaise for example).  So the dishes are not plain Waffle House types of breakfast dishes, but rather the Chef's own interpretation of various classic breakfast entrees.  All very good, with excellent service that is friendly, but not over bearing.  If you want something different for breakfast or lunch, this is a good choice. 

json_type: review, rank: 3, score: 3.3422329425811768,              docID: 705692, text: Good breakfast spot in the French Quarter. Good good, good service. More traditional breakfast option with less emphasis on Cajun cuisine. 


Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): geospatial
Enter the number of results to display (default is 10): 5
Enter top-left latitude: 30
Enter top-left longitude: -90.05
Enter bottom-right latitude: 29
Enter bottom-right longitude: -90
---------- begin geospatial query ---------- 

Query processed in 0.12 seconds
------found 728 businesses, the top 5 as follows:-----
json_type: business, rank: 1, score: 2.0, docID: 3, name: Lafitte's Landing Seafood House, latitude: 29.8754822266, longitude: -90.04938 

json_type: business, rank: 2, score: 2.0, docID: 12, name: Domino's Pizza, latitude: 29.8753202, longitude: -90.045817 

json_type: business, rank: 3, score: 2.0, docID: 21, name: The Music Box Village, latitude: 29.9635911, longitude: -90.0292571 

json_type: business, rank: 4, score: 2.0, docID: 45, name: Frady's One Stop Food Store, latitude: 29.963974, longitude: -90.0426042 

json_type: business, rank: 5, score: 2.0, docID: 52, name: Factotum Barber + Supply, latitude: 29.9649841114, longitude: -90.0422938596 


Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): exit
Exiting console. Goodbye!
```

update

```
Enter your search query: car
Enter the number of results to display (default is 10): 5
Enter the search key (default is 'text'): name
---------- begin normal query ---------- 

Query processed in 0.09 seconds
------found 82 documents, the top 5 as follows:-----
json_type: business, rank: 1, score: 2.5097739696502686,              docID: 4218, name: Car Doc 

json_type: business, rank: 2, score: 2.1646687984466553,              docID: 1, name: Nifty Car Rental 

json_type: business, rank: 3, score: 2.1646687984466553,              docID: 241, name: Sahara Car Wash 

json_type: business, rank: 4, score: 2.1646687984466553,              docID: 631, name: Enterprise Car Sales 

json_type: business, rank: 5, score: 2.1646687984466553,              docID: 762, name: Halima Car Wash
```



# **3.4 Review Summary**

## 3.4.1 show a distribution of reviews contributed by the users

> 1. plot a figure with x-axis showing the number of reviews contributed by a user, and y-axis showing the number of users having a particular number of reviews

review_distribution.py 运行结果

![review_distribution](https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/review_distribution.png)

## 3.4.2 present a user’s review summary, given a user id, his/her review summary contains

> 1. ***The number of reviews he/she has contributed.***
> 2. ***The bounding box of the businesses that he/she has reviewed.*** This bounding box may suggests the activity area of this user.
> 3. ***The top-10 most frequent words used in his/her review, excluding stopwords.*** It would be a plus to show the top-10 most frequent phrases used in his/her reviews.
> 4. ***Three most representative sentences selected from his/her reviews. In your report, you should describe what does it mean by “representative” and how the sentences are selected.***
>

user_review_summary.py 运行结果

```
Fetching review count for user: bcjbaE6dDog4jkNY91ncLQ
User bcjbaE6dDog4jkNY91ncLQ has contributed 121 reviews.
Fetching bounding box for user: bcjbaE6dDog4jkNY91ncLQ
User bcjbaE6dDog4jkNY91ncLQ's activity area is defined by the bounding box:
Top-left corner (latitude, longitude): (30.0500397, -90.2662712)
Bottom-right corner (latitude, longitude): (29.920519, -89.9530888)
Fetching top frequent words for user: bcjbaE6dDog4jkNY91ncLQ
Top-10 most frequent words: [('food', 45), ('salad', 40), ('back', 38), ('get', 36), ('good', 35), ('service', 31), ('like', 27), ('cheese', 25), ('one', 25), ('time', 24)]
Top-10 most frequent phrases: [(('go', 'back'), 9), (('customer', 'service'), 8), (('bread', 'pudding'), 6), (('love', 'place'), 6), (('back', 'sure'), 5), (('service', 'slow'), 5), (('every', 'time'), 5), (('next', 'time'), 4), (('salad', 'good'), 4), (('first', 'time'), 4)]
```

*Three most representative sentences*

TBD

# **3.5 Application**

> ***to detect the sentences containing comparison in reviews***