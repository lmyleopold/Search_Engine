1. 关键词搜索评论：boolean search N = 3

```
Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): boolean
Enter your search query: good breakfast
Enter the number of results to display (default is 10): 3
Enter the search key (default is 'text'): text
---------- begin boolean query ---------- 

Query processed in 0.14 seconds
------found 12549 documents, the top 3 as follows:-----
json_type: review, rank: 1, score: 3.4009456634521484,              docID: 96205, text: A nice diner feel breakfast restaurant in the French Quarter.  Nothing fancy, but good breakfast menu and good service.  Small restaurant with tables only, no booths.  Good for a quick, filling and good breakfast. 

json_type: review, rank: 2, score: 3.3496389389038086,              docID: 247637, text: We had breakfast here, and it was very good.  The menu has local twists on traditional breakfast entrees.  Thus you will find seafood in some of the breakfast dishes, and a lot of the breakfast entrees have a sauce on them (Hollandaise for example).  So the dishes are not plain Waffle House types of breakfast dishes, but rather the Chef's own interpretation of various classic breakfast entrees.  All very good, with excellent service that is friendly, but not over bearing.  If you want something different for breakfast or lunch, this is a good choice. 

json_type: review, rank: 3, score: 3.3422329425811768,              docID: 705692, text: Good breakfast spot in the French Quarter. Good good, good service. More traditional breakfast option with less emphasis on Cajun cuisine.
```

```
Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): boolean 
Enter your search query: car     
Enter the number of results to display (default is 10): 3
Enter the search key (default is 'text'): text
---------- begin boolean query ---------- 

Query processed in 0.02 seconds
------found 1622 documents, the top 3 as follows:-----
json_type: review, rank: 1, score: 3.488175392150879,              docID: 156688, text: Worst car wash ever whole car wash broke astf don't even wash your car just simply wets it the worst car wash !!!!! 

json_type: review, rank: 2, score: 3.4746837615966797,              docID: 157702, text: I rented a car from Enterprise rent-a-Car, location Kenner, La. 70062. I had the car for one day, I used it for a short time the day I rented the car. The car spent the rest of the day and night in my garage until I drove it back to Enterprise the next day . The car didn't have any damage on it when I returned it to them. Now they are claiming I returned the car with damage on it, my big mistake was not doing a walk about with the attendant when he checked the car for damages after returning the car . Since the car hadn't any damage I felt safe to let the attendant check the car by himself, he came to the door after checking the car and said I could go. I assumed ever thing was all right, now I got emails from the insurance company telling me about the damages to the car. Six months down the line I could get bills for possible repairs for the car 

json_type: review, rank: 3, score: 3.441908359527588,              docID: 706709, text: This car wash was awesome. I paid $10 and my car came out nice.  It is a do it yourself car wash so you will have to scrub our car with a brush and soapy water before you go into the car wash and then vacuum your car at the end. It a great place I will definitely be going back. 

```



2. 关键词搜索商户：phase search N = 5

```
Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): phrase
Enter your search query: good breakfast
Enter the number of results to display (default is 10): 5
Enter the search key (default is 'text'): name
---------- begin phrase query ---------- 

Query processed in 0.01 seconds
------found 0 documents, the top 5 as follows:-----

```

```
Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): phrase
Enter your search query: 5
Enter the number of results to display (default is 10): 
Enter the search key (default is 'text'): 
---------- begin phrase query ---------- 

Query processed in 0.02 seconds
------found 0 documents, the top 10 as follows:-----

Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): phrase
Enter your search query: car wash
Enter the number of results to display (default is 10): 5
Enter the search key (default is 'text'): name
---------- begin phrase query ---------- 

Query processed in 0.03 seconds
------found 28 documents, the top 5 as follows:-----
json_type: business, rank: 1, score: 4.6856513023376465,              docID: 241, name: Sahara Car Wash 

json_type: business, rank: 2, score: 4.6856513023376465,              docID: 762, name: Halima Car Wash 

json_type: business, rank: 3, score: 4.6856513023376465,              docID: 1276, name: Safari Car Wash 

json_type: business, rank: 4, score: 4.6856513023376465,              docID: 1808, name: WOW Car Wash 

json_type: business, rank: 5, score: 4.6856513023376465,              docID: 1969, name: SUDZ Car Wash
```



3. 关键词搜索评论：normal search N = 3 格式"word1 word2\"

```
Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): normal
Enter your search query: "good breakfast"
Enter the number of results to display (default is 10): 3
Enter the search key (default is 'text'): text
---------- begin normal query ---------- 

Query processed in 0.13 seconds
------found 854 documents, the top 3 as follows:-----
json_type: review, rank: 1, score: 3.2456858158111572,              docID: 82829, text: Good breakfast spot and close to MSY airport. 
Friendly people and fun atmosphere with good breakfast food.
Recommend the Beignet sticks! 

json_type: review, rank: 2, score: 3.101207733154297,              docID: 96205, text: A nice diner feel breakfast restaurant in the French Quarter.  Nothing fancy, but good breakfast menu and good service.  Small restaurant with tables only, no booths.  Good for a quick, filling and good breakfast. 

json_type: review, rank: 3, score: 3.0696749687194824,              docID: 174661, text: Best iced coffee in New Orleans. I would give it 5 stars but they don't have good breakfast options with the coffee. There are a couple places within a block where you can get good breakfast though.


Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): phrase
Enter your search query: good breakfast
Enter the number of results to display (default is 10): 3
Enter the search key (default is 'text'): text
---------- begin phrase query ---------- 

Query processed in 0.04 seconds
------found 854 documents, the top 3 as follows:-----
json_type: review, rank: 1, score: 3.2456858158111572,              docID: 82829, text: Good breakfast spot and close to MSY airport. 
Friendly people and fun atmosphere with good breakfast food.
Recommend the Beignet sticks! 

json_type: review, rank: 2, score: 3.101207733154297,              docID: 96205, text: A nice diner feel breakfast restaurant in the French Quarter.  Nothing fancy, but good breakfast menu and good service.  Small restaurant with tables only, no booths.  Good for a quick, filling and good breakfast. 

json_type: review, rank: 3, score: 3.0696749687194824,              docID: 174661, text: Best iced coffee in New Orleans. I would give it 5 stars but they don't have good breakfast options with the coffee. There are a couple places within a block where you can get good breakfast though.
```

```
Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): normal
Enter your search query: "car wash"
Enter the number of results to display (default is 10): 3
Enter the search key (default is 'text'): text
---------- begin normal query ---------- 

Query processed in 0.02 seconds
------found 536 documents, the top 3 as follows:-----
json_type: review, rank: 1, score: 8.056665420532227,              docID: 156688, text: Worst car wash ever whole car wash broke astf don't even wash your car just simply wets it the worst car wash !!!!! 

json_type: review, rank: 2, score: 7.78621768951416,              docID: 134135, text: Okay , so it was first time visiting this car wash. I was totally confused at first, but I met the lady Dawn, whom I assume works for this car wash company . She says she normally not there all the time. It looks like she was just visiting and working on something for the car wash. I asked her how much is the car wash? She gave me the info I needed. The issue came in that the change machine was down and I only had a 20. So, Dawn was nice enough to break my 20 herself , so I can get my car wash. She also helped me get through the car wash successfully. Dawn was GREAT!! Thanks for making my car wash experience the BOMB! We need more people like Dawn in customer service. 

json_type: review, rank: 3, score: 7.390958786010742,              docID: 249028, text: This place rocks!!!!!!!!! Unbelievable how well the car wash works and it's kind of fun riding on through without actually driving. Way to go Pelican car wash!!!!!!!!! 


Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): phrase
Enter your search query: car wash
Enter the number of results to display (default is 10): 3
Enter the search key (default is 'text'): text
---------- begin phrase query ---------- 

Query processed in 0.01 seconds
------found 536 documents, the top 3 as follows:-----
json_type: review, rank: 1, score: 8.056665420532227,              docID: 156688, text: Worst car wash ever whole car wash broke astf don't even wash your car just simply wets it the worst car wash !!!!! 

json_type: review, rank: 2, score: 7.78621768951416,              docID: 134135, text: Okay , so it was first time visiting this car wash. I was totally confused at first, but I met the lady Dawn, whom I assume works for this car wash company . She says she normally not there all the time. It looks like she was just visiting and working on something for the car wash. I asked her how much is the car wash? She gave me the info I needed. The issue came in that the change machine was down and I only had a 20. So, Dawn was nice enough to break my 20 herself , so I can get my car wash. She also helped me get through the car wash successfully. Dawn was GREAT!! Thanks for making my car wash experience the BOMB! We need more people like Dawn in customer service. 

json_type: review, rank: 3, score: 7.390958786010742,              docID: 249028, text: This place rocks!!!!!!!!! Unbelievable how well the car wash works and it's kind of fun riding on through without actually driving. Way to go Pelican car wash!!!!!!!!!
```

4. 关键词搜索商户：normal search N = 5 格式"word1 AND word2 AND word3"

```
Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): normal                            
Enter your search query: good AND breakfast AND egg
Enter the number of results to display (default is 10): 5
Enter the search key (default is 'text'): name
---------- begin normal query ---------- 

Query processed in 0.01 seconds
------found 0 documents, the top 5 as follows:-----

```

```
Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): normal
Enter your search query: car AND wash AND dry
Enter the number of results to display (default is 10): 5
Enter the search key (default is 'text'): name
---------- begin normal query ---------- 

Query processed in 0.01 seconds
------found 0 documents, the top 5 as follows:-----

```



4*. 关键词搜索商户：normal search N = 5

```
Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): normal
Enter your search query: good breakfast
Enter the number of results to display (default is 10): 5
Enter the search key (default is 'text'): name
---------- begin normal query ---------- 

Query processed in 0.02 seconds
------found 42 documents, the top 5 as follows:-----
json_type: business, rank: 1, score: 3.2655248641967773,              docID: 1115, name: Good Hands 

json_type: business, rank: 2, score: 3.2655248641967773,              docID: 2391, name: Good Bird 

json_type: business, rank: 3, score: 3.2655248641967773,              docID: 4518, name: Good Bird 

json_type: business, rank: 4, score: 3.2655248641967773,              docID: 8622, name: Good Eggs 

json_type: business, rank: 5, score: 3.1677613258361816,              docID: 4467, name: Bayou Breakfast
```

```
Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): normal
Enter your search query: car wash
Enter the number of results to display (default is 10): 5
Enter the search key (default is 'text'): name
---------- begin normal query ---------- 

Query processed in 0.01 seconds
------found 91 documents, the top 5 as follows:-----
json_type: business, rank: 1, score: 4.685651779174805,              docID: 241, name: Sahara Car Wash 

json_type: business, rank: 2, score: 4.685651779174805,              docID: 762, name: Halima Car Wash 

json_type: business, rank: 3, score: 4.685651779174805,              docID: 1276, name: Safari Car Wash 

json_type: business, rank: 4, score: 4.685651779174805,              docID: 1808, name: WOW Car Wash 

json_type: business, rank: 5, score: 4.685651779174805,              docID: 1969, name: SUDZ Car Wash
```



5.关键词搜索商户：normal search N = 5 格式"word1 word2 word3"

```
Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): normal
Enter your search query: good breakfast egg
Enter the number of results to display (default is 10): 5
Enter the search key (default is 'text'): name
---------- begin normal query ---------- 

Query processed in 0.01 seconds
------found 45 documents, the top 5 as follows:-----
json_type: business, rank: 1, score: 3.592729091644287,              docID: 7596, name: Egg Roll House 

json_type: business, rank: 2, score: 3.2655248641967773,              docID: 1115, name: Good Hands 

json_type: business, rank: 3, score: 3.2655248641967773,              docID: 2391, name: Good Bird 

json_type: business, rank: 4, score: 3.2655248641967773,              docID: 4518, name: Good Bird 

json_type: business, rank: 5, score: 3.2655248641967773,              docID: 8622, name: Good Eggs
```

```
Enter query type ('normal', 'phrase', 'boolean', 'geospatial'): normal
Enter your search query: car wash dry
Enter the number of results to display (default is 10): 5
Enter the search key (default is 'text'): name
---------- begin normal query ---------- 

Query processed in 0.02 seconds
------found 101 documents, the top 5 as follows:-----
json_type: business, rank: 1, score: 4.9020676612854,              docID: 689, name: Quick Wash and Dry 

json_type: business, rank: 2, score: 4.685651779174805,              docID: 241, name: Sahara Car Wash 

json_type: business, rank: 3, score: 4.685651779174805,              docID: 762, name: Halima Car Wash 

json_type: business, rank: 4, score: 4.685651779174805,              docID: 1276, name: Safari Car Wash 

json_type: business, rank: 5, score: 4.685651779174805,              docID: 1808, name: WOW Car Wash
```
