1. 选出某个user的评论中最representative的句子，代码在github text data/summary/representative.py

    a. 首先利用search.engine获取到改user的全部评论

    b. 对每一条评论做 sentence_segement, 得到一个个sentence

    c. 对每一个sentence 做embedding, embedding的方式有很多，我们用了最简单的方式，tf-idf

    注：假设根据改user所有的review建立了一个vocabulary，这个vocabulary里面有 N 个词，那么对于一个句子的tf-idf embedding 得到的矩阵的维度是 1行 N列，例如 [0.001, 0, 0, 0.23, 0.68], 0就是vocabulary中的这个词在这个sentence里没出现， 其他的数是这个词的tf-idf值

    d. 在得到embedding之后，选出在这个用户评论中使用最频繁的sentence， 这里考虑了两种方式：

        第一种是 ： 将这个矩阵 [0.001, 0, 0, 0.23, 0.68] 加起来，矩阵的和除以非零元素的个数，这是防止越长的句子这个和越大。 然后选出tf-idf矩阵和最大的几个sentence。这种方式选出来的句子很短

        第二种是 ： 不是简单sum矩阵，利用cosine similarity，计算这个句子[0.001, 0, 0, 0.23, 0.68]与其他所有句子的cosine similarity值，然后平均, 再除以句子长度做一个惩罚， 解决了句子较长的问题。
    
    e. 在这个user自己的review中出现很频繁的句子也可能在其他user中出现频繁，因此要选出在其他用户中不那么频繁的句子

        具体流程是：
            （1）. 随机选出100个用户，根据 d 步，选出每个人使用最频繁的句子
            （2）. 利用tf-idf 或这个 cosine similarity，选出这个user 在这些句子中 tf-idf较小的句子
    
    一些想法：
        通过tf-idf 和 cosine similarity两种方式得到的句子是不同的，tf-idf倾向于选出那些含有特别的词的句子，强调信息量和关键词的重要性，cosine similarity比较的是句子内容是否相似，
        
        近一步的方式可能是两者进行结合， 例如 score = tf-idf + lambda * cosine_similarity
    
    示例：
    使用tf-idf : user_id = '3JQ8RjMGiT8m5hsBq99Zfw'
        前十个使用最频繁的句子：
        ["I'm skeptical about that claim.", 'All in all, a pleasant experience!', 'Brussel sprouts were delicious.', 'Atmosphere is extremely chaotic.', 'Decent place, very inexpensive.', "Seaworthy's service is lacking.", "Reginelli's disappoints me sometimes.", 'Very light, undetectable dressing.', 'Fresh fillings, generous portions.', 'A very consistent establishment!']
        前三个最后代表性的：
        ['A very consistent establishment!', 'All in all, a pleasant experience!', 'Atmosphere is extremely chaotic.']

    使用tf-idf : user_id = 'QQtoHnP0cP7nzNnUob_1CQ'
        前十个使用最频繁的句子：
        ['Similarly I enjoyed the vegetables.', 'Perfectly dressed and balanced.', "It's a standard, simple cocktail.", 'Quintessential New Orleans cuisine.', "I wouldn't come as a destination.", 'I prefer a more holistic approach.', 'Something different about them.', "I certainly didn't leave hungry.", 'I chose Roast Duckling Madison.', 'Basil, sprouts, lime, jalepenos.']
        前三个最后代表性的：
        ['A little pork and a little vinegar.', 'Basil, sprouts, lime, jalepenos.', 'Definitely coming back for more.']
    
    使用 cosine similarity : user_id = '3JQ8RjMGiT8m5hsBq99Zfw'
        前十个使用最频繁的句子：
        ['I just had some decaf and it was good.', 'I also ordered the fish of the day.', 'I love the menu, the place, music.', 'The service and value are great.', 'I ordered the little salad and it was delicious.', 'The quality is the best in New Orleans.', '5 stars for the bakery and coffee and 3 for the restaurant.', 'This was the highlight of the evening.', 'The coffee is great and the service was excellent.', "Well, it's the best I have had here."]
        前三个最后代表性的：
        ['5 stars for the bakery and coffee and 3 for the restaurant.', 'A couple of us tried it and it was very good.', 'Bread pudding was last and it was ok.']
    
    使用 cosine similarity : user_id = 'QQtoHnP0cP7nzNnUob_1CQ'
        前十个使用最频繁的句子：
        ['It was delicious and had a custard-y flavor.', 'The bread and cheese were enough for me.', 'It was pretty good but so rich.', 'When I got the bill, it was $8 or $9!', "It's not, it's a full, hot, plate.", 'It was not bread pudding, and it was pretty dry.', 'It was hot but was pretty bland.', 'But, it had very little flavor.', 'The food and service was excellent.', 'But it was only $6.50, so it was okay.']
        前三个最后代表性的：
        ["And it was the same price as Luke's!", 'But it was only $6.50, so it was okay.', 'But, it had very little flavor.']
    

    

2. application 部分 实现了一个相对简单的推荐系统, 代码在github text data/summary/recommend.py

    a. 在businees.json中有个属性是 categories，也就是这个商家做什么

    b. 统计用户评论，统计用户评论中 出现的 不同的categories的频次，这里加了一个情感分析的方式，也就是出现在积极情感得句子中的categories才被计算。这样就得到了用户对哪些种类评价最多

    c. 给定一个business 和 一个 user，计算这个business 的 categories 和 用户评论中的得到的关键词之间的联系程度，以此判断是否向该用户进行推荐

    示例：
    用户 user_id = 'bcjbaE6dDog4jkNY91ncLQ'
    得到的该用户的常用的 category: 
    [('salad', 9.1767), ('food', 8.8501), ('vegan', 4.1803), ('soup', 2.921999), ('tacos', 1.973799), ('fish', 1.8329), ('sandwiches', 1.3204), ('music', 1.3149), ('used', 1.0406), ('veggies', 0.951), ('vegetarian', 0.8732), ('chips', 0.8687), ('vietnamese', 0.8074), ('restaurants', 0.6597), ('empanadas', 0.6597), ('mexican', 0.5106), ('brunch', 0.4939), ('seafood', 0.4404), ('banks', 0.4215), ('breakfast', 0.34), ('diners', 0.3161)]

    business_id = "ifofBiQeb6DI0-u0KEQybg"
    得到该商家的tag : ['salad', 'restaurants', 'breakfast, 'brunch', 'food']

    输出为：
    "According to user bcjbaE6dDog4jkNY91ncLQ review keywords and business ifofBiQeb6DI0-u0KEQybg tags, the probability that user will go to business is 0.666331"