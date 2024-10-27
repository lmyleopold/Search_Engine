我提取了review_count > 1500条的所有`business_id`并进行语义分析

```
['W4ZEKkva9HpAdZG88juwyQ', '8uF-bhJFgT4Tn6DTb27viA', 'GBTPC53ZrG1ZBY3DT8Mbcw', 'g04aAvgol7IW8buqSbT4xA', 'vN6v8m4DO45Z4pp8yxxF_w', 'S2Ho8yLxhKAa26pBAm6rxA', 'Zi-F-YvyVOK0k5QD7lrLOg', 'DcBLYSvOuWcNReolRVr12A', 'mhrW9O0O5hXGXGnEYBVoag', 'hfbZ97Te3T4jeWN6GgsGrQ', 'VQcCL9PiNL_wkGf-uF3fjg', '_C7QiQQc47AOEv4PE3Kong', 'u7uFQCoHFtBKCtbWUm6yZw', 'FEXhWNCMkv22qG04E83Qjg', 'TcNZXteosegb1RO4O5hREw', 'ku8cAVBLaF_4rI-yK6gNnQ', 'qb28j-FNX1_6xm7u372TZA', 'V9VLhHdSFpFi4yXFqVcVEA', 'EagkHaaC-kUozD3MPzbRIw', 'RLlOK2fL6xU1sfIPiP2QBw', 'ChlcxTEoWBQJXJ2Xb2vm5g', 'gTC8IQ_i8zXytWSly3Ttvg', '6Ty-KKWq6hLZYW8DWEHYvg', 't9LiapsQABwMQeiF1Czl6w', 'VaO-VW3e1kARkU9bP1E7Fw', 'XnQ84ylyAZwh-XfHGGNBbQ', 'qclZoDz3sjT7v5xOSj5P2Q', 'VVH6k9-ycttH3TV_lk5WfQ', 'iwmW2mgcn2YdirXUHCsgXQ', 'PGd06nrseC2YAIqP6S9gUA', 'Vz2RN55rTJBGn43K1v84nA', 'n_fUROdhfmLwd_mpBi55ew', '7Iv-6B0EH-yVo5o_VnykWw', 'Eb1XmmLWyt_way5NNZ7-Pw', '75FY8ZQx5nOWP0VFmNvWfw', '6a4gLLFSgr-Q6CZXDLzBGQ', 'iSRTaT9WngzB8JJ2YKJUig', 'BjeHLwKOlHyV6DJgmZxAjA', '-Tskf8WK17rb3ZfeFuRSWA', 'ac1AeYqs8Z4_e2X5M3if2A', '_ab50qdWOk0DdB6XOrBitw', '8UPv1p9GW-BiZtQqUt8nOA', 'e5fCI12X_GLCST668S4ROA', 'ww3YJXu5c18aGZXWmm00qg', 'U4X-tzwvTzW8uWxs2KIPtg', 'Y2Pfil51rNvTd_lFHwzb_g', 'WXgV2lOUgas7DzTLeDau-w', 'c-iKAO2GBzSKjm7y1Oljcw', '-VlBFlHwX-Pt6Xyzs9roGw', 'yz0KWVamNhqiZGz7XTClzg', '9xdXS7jtWjCVzL4_oPGv9A', 'oBNrLz4EDhiscSlbOl8uAw']
```

找到以下两个结果比较具有代表性：

<img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241027183338137.png" alt="image-20241027183338137" style="zoom: 50%;" /><img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241027183347025.png" alt="image-20241027183347025" style="zoom: 50%;" />

> application/output/ac1AeYqs8Z4_e2X5M3if2A_sentiment_trend_TextBlob.png：评价变好，但又个别极差评

<img src="C:\Users\lmyle\AppData\Roaming\Typora\typora-user-images\image-20241027183500707.png" alt="image-20241027183500707" style="zoom:50%;" /><img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241027183559513.png" alt="image-20241027183559513" style="zoom:50%;" />

> application/output/e5fCI12X_GLCST668S4ROA_sentiment_trend_TextBlob.png：差评变多，口碑下滑

我使用了语义分析两种方法，分别是基于textblob（NLTK）和BERT的，其中BERT速度慢且极端值较多，所以还是建议使用textblob，但是smooth后所展现出的趋势其实是**一致的**：

<img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241027183855785.png" alt="image-20241027183855785" style="zoom:50%;" /><img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241027183838704.png" alt="image-20241027183838704" style="zoom:50%;" />

<img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241027184259232.png" alt="image-20241027184253379" style="zoom:50%;" />
<img src="https://lmyleopold-typora-image.oss-cn-shanghai.aliyuncs.com/img/image-20241027184313825.png" alt="image-20241027184313825" style="zoom:50%;" />

整个application的操作方式如下：

```powershell
python ./application/console.py 
```

```
Enter the business ID: ac1AeYqs8Z4_e2X5M3if2A
Choose method (textblob/bert): textblob
```

```
Review Text: My family and I visited this place for dinner on a Monday evening. We had 6:30pm reservations. We were very surprise to see a line out the door when we arrived. I ordered the shrimp creole which was lukewarm and just "okay". My husband and son ordered the shrimp platter which looked, smelled and tasted amazing. The hush puppies with the shrimp platter were so so good with a spicy kick!!!! My daughter ordered shrimp Alfredo which she says she enjoyed. The icing on the cake was the bread pudding dessert. OMG, please do your sweet taste buds a favor and order this fantastic treat! What a way to end our BIG EASY meal in NOLA.
Review Date: 2018-04-04 03:42:17
Review Text: Decent étouffée and Poboy but kinda run of the mill for New Orleans.
Review Date: 2015-10-08 04:57:18
Review Text: Got the taste of New Orleans and there was nothing on there worth ordering again. Friend got a seafood platter and he didn't care for it. Pretty pricey, surprised there are so many good reviews but have good for them.
Review Date: 2018-04-04 04:28:02
Review Text: Came here for a late dinner on our first night in New Orleans. We had just arrived and needed somewhere to get dinner. This place, located just across from our hotel was the perfect introduction to NOLA. We got the gator tail bites (highly recommend) and a rack of ribs. Food was good, service was good- a solid experience!
Review Date: 2015-06-21 04:44:58
Review Text: George and I each had the seafood gumbo and it was truly amazing.  We could have just stayed with bowls of that. We then had shrimp and oyster po boys that were amazing.  We will be back before end of this trip!
Review Date: 2015-10-17 15:29:25
...
```

Output：两张趋势图