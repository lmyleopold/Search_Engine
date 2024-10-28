1. 选出某个user的评论中最representative的句子，代码在github text data/summary/representative.py

    a. 首先利用search.engine获取到改user的全部评论

    b. 对每一条评论做 sentence_segement, 得到一个个sentence

    c. 对每一个sentence 做embedding, embedding的方式有很多，我们用了最简单的方式，tf-idf

    注：假设根据改user所有的review建立了一个vocabulary，这个vocabulary里面有 N 个词，那么对于一个句子的tf-idf embedding 得到的矩阵的维度是 1行 N列，例如 [0.001, 0, 0, 0.23, 0.68], 0就是vocabulary中的这个词在这个sentence里没出现， 其他的数是这个词的tf-idf值

    d. 在得到embedding之后，选出在这个用户评论中使用最频繁的sentence, 这里使用cosine_similarity：

        利用cosine similarity，计算这个句子[0.001, 0, 0, 0.23, 0.68]与其他所有句子的cosine similarity值，然后平均, 再除以句子长度做一个惩罚， 解决了句子较长的问题。
    
    e. 在这个user自己的review中出现很频繁的句子也可能在其他user中出现频繁，因此要选出在其他用户中不那么频繁的句子

        具体流程是：
            （1）. 随机选出100个用户，根据 d 步，选出每个人使用最频繁的句子
            （2）. 利用cosine similarity，选出这个user 在这些句子中cosine similarity较小的句子
    
    示例：
    这是第一个用户
    embedding_type = bow, user_id = QQtoHnP0cP7nzNnUob_1CQ
    the 10 most common sentences:
    ['Miriam had a salad and the drum.', 'The coffee is great and the service was excellent.', 'The staff is friendly and the prices fair.', 'The cake was dry and really dense.', 'The exception is the BBQ counter.', 'About balance and highlighting the ingredients.', 'The greens and slaw were perfection.', 'The dead battery was the worst.', 'The service and value are great.', 'This was the highlight of the evening.']
    the 3 most representative sentences:
    11
    ['The staff is friendly and the prices fair.', 'They were good and the price was fair.', 'This was the highlight of the evening.']
    ------------------------------------
    embedding_type = tf-idf, user_id = QQtoHnP0cP7nzNnUob_1CQ
    the 10 most common sentences:
    ['The service was just ok at best.', 'We had a great time and the food was delicious.', 'I just had some decaf and it was good.', 'This is really terrific chicken.', 'They were good and the price was fair.', 'The quality is the best in New Orleans.', 'I ordered the little salad and it was delicious.', 'This was the highlight of the evening.', 'The service and value are great.', 'The coffee is great and the service was excellent.']
    the 3 most representative sentences:
    11
    ["Well, it's the best I have had here.", 'You have to pay for better food.', 'and the best we had on our trip.']
    ------------------------------------
    embedding_type = ngram, user_id = QQtoHnP0cP7nzNnUob_1CQ
    the 10 most common sentences:
    ["Doesn't matter, it was terrible.", 'Best croissants in New Orleans.', 'It was a theme for the day unfortunately.', 'It was beautiful and very thoughtful.', "Some of the best you'll find in New Orleans.", 'It was huge and nicely dressed.', 'It was a beautifully presented dish.', 'I ordered the little salad and it was delicious.', 'Bread pudding was last and it was ok.', 'Nothing special but it was fine.']
    the 3 most representative sentences:
    11
    ['This was the highlight of the evening.', 'We finished with the bread pudding and it was excellent.', 'We had dinner here tonight, and it was very good.']
    ------------------------------------
    embedding_type = bert, user_id = QQtoHnP0cP7nzNnUob_1CQ
    the 10 most common sentences:
    ['I chose Roast Duckling Madison.', 'The mashed potatoes were instant.', 'Similarly I enjoyed the vegetables.', 'We both chose Italian dressing.', 'The catfish dish was excellent.', 'The bread service is embarrassing.', 'Perfectly dressed and balanced.', 'Quintessential New Orleans cuisine.', 'Something different about them.', 'Inspired and beautifully prepared.']
    the 3 most representative sentences:
    11
    ['This is really terrific chicken.', 'This was a good representation.', 'We both chose Italian dressing.']
    ------------------------------------

    这是第二个用户
    embedding_type = bow, user_id = 3JQ8RjMGiT8m5hsBq99Zfw
    the 10 most common sentences:
    ['The cheeseburger here was sublime.', 'The lychee and the pear were fantastic.', 'It was the bargain of a lifetime!', 'The mimosa and the tea were excellent.', 'The atmosphere was very unenjoyable.', 'The service was very attentive.', 'The waitress was warm and friendly.', 'The food and service was excellent.', 'The order-at-the-counter process was perfect.', 'The pizza-by-the-slice is excellent.']
    the 3 most representative sentences:
    11
    ['The waitress was warm and friendly.', 'The worst part was the sticker shock.', 'Was a great complement to the calamari.']
    ------------------------------------
    embedding_type = tf-idf, user_id = 3JQ8RjMGiT8m5hsBq99Zfw
    the 10 most common sentences:
    ['The macaroni and cheese was pretty good too.', 'The service was very attentive.', 'It was very affordable and tasty.', 'It was hot but was pretty bland.', 'But, it had very little flavor.', 'The bread and cheese were enough for me.', 'The order-at-the-counter process was perfect.', 'It was pretty good but so rich.', 'The pizza-by-the-slice is excellent.', 'The food and service was excellent.']
    the 3 most representative sentences:
    11
    ['The spicy potato salad was really good!', 'The waiter was very nice as well.', 'The waitress was warm and friendly.']
    ------------------------------------
    embedding_type = ngram, user_id = 3JQ8RjMGiT8m5hsBq99Zfw
    the 10 most common sentences:
    ['It was tasty but a little gummy.', 'It was simply okay, not delicious.', 'But it was only $6.50, so it was okay.', 'It was hot but was pretty bland.', 'It was the bargain of a lifetime!', 'It was not bread pudding, and it was pretty dry.', 'It was delicious and rivaled Chick-Fil-A.', 'It was pretty good but so rich.', 'It was served with fluffy rice.', 'It was very affordable and tasty.']
    the 3 most representative sentences:
    11
    ['It was tasty but a little gummy.', 'It was tender and cooked perfectly medium rare.', 'It was the bargain of a lifetime!']
    ------------------------------------
    embedding_type = bert, user_id = 3JQ8RjMGiT8m5hsBq99Zfw
    the 10 most common sentences:
    ['The cheeseburger here was sublime.', 'The rolls were reasonably priced.', 'My tastebuds were honestly dazzled.', 'The finger sandwiches were lacking.', 'Obviously not their signature dish.', 'A very consistent establishment!', 'That was completely ridiculous.', 'Brussel sprouts were delicious.', 'Lavender lemonade was refreshing.', 'The pizza-by-the-slice is excellent.']
    the 3 most representative sentences:
    11
    ['The waiters are utter dum-dums.', 'This place merits regular visits.', 'Very light, undetectable dressing.']
    ------------------------------------

    

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