import matplotlib.pyplot as plt
from collections import defaultdict
import lucene
from org.apache.lucene.store import FSDirectory
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.search import IndexSearcher
from java.nio.file import Paths

# 初始化Lucene
def init_lucene():
    lucene.initVM()

# 提取用户评论数据
def extract_user_review_data(index_path):
    print("Extracting user review data...")
    
    # 打开索引
    index_directory = FSDirectory.open(Paths.get(index_path))
    index_reader = DirectoryReader.open(index_directory)
    index_searcher = IndexSearcher(index_reader)

    # 统计每个用户贡献的评论数量
    user_review_count = defaultdict(int)

    # 遍历索引中的每个文档
    for i in range(index_reader.maxDoc()):
        doc = index_reader.document(i)
        user_id = doc.get("user_id")
        if user_id:
            user_review_count[user_id] += 1

    index_reader.close()

    return user_review_count

# 统计评论数量分布
def calculate_review_distribution(user_review_count):
    review_distribution = defaultdict(int)

    # 统计不同评论数量对应的用户数
    for count in user_review_count.values():
        review_distribution[count] += 1

    return review_distribution

# 绘制评论数量分布图
def plot_review_distribution(review_distribution):
    x = list(review_distribution.keys())  # 评论数量
    y = list(review_distribution.values())  # 用户数

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='darkblue')
    plt.xlabel('Number of Reviews Contributed by a User')
    plt.ylabel('Number of Users')
    plt.title('Distribution of Reviews Contributed by Users')
    plt.yscale('log')  # 使用对数刻度处理不均匀分布
    plt.grid(True)
    plt.show()
    plt.savefig('./data/summary/review_distribution.png')

    with open('./data/summary/review_distribution.txt', 'w') as f:
        for count, user_count in review_distribution.items():
            f.write(f'{count}: {user_count}\n')

# def save_review_distribution_plot(review_distribution):
#     x = list(review_distribution.keys())
#     y = list(review_distribution.values())

#     plt.figure(figsize=(10, 6))
#     plt.bar(x, y, color='skyblue')
#     plt.xlabel('Number of Reviews Contributed by a User')
#     plt.ylabel('Number of Users')
#     plt.title('Distribution of Reviews Contributed by Users')
#     plt.yscale('log')
#     plt.grid(True)
    


if __name__ == "__main__":
    init_lucene()
    
    index_path = "./data/index"
    
    user_review_count = extract_user_review_data(index_path)
    
    review_distribution = calculate_review_distribution(user_review_count)
    
    plot_review_distribution(review_distribution)
