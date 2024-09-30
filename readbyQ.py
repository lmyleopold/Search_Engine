import json

#   paths need to be modified
business_path = "D:\yelp_dataset\yelp_academic_dataset_business.json"
review_path = "D:\yelp_dataset\yelp_academic_dataset_review.json"

"""create a smaller sampled dataset"""
businesses = []
reviews = []
business_set = set()
sub_business = []
sub_review = []

with open(business_path, 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():
            json_obj = json.loads(line)
            businesses.append(json_obj)

with open(review_path, 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():
            json_obj = json.loads(line)
            reviews.append(json_obj)

for obj in businesses:
    state = obj.get('state')
    if state == 'PA':
        new_json_obj = {}
        new_json_obj['business_id'] = obj.get('business_id')
        new_json_obj['name'] = obj.get('name')
        new_json_obj['city'] = obj.get('city')
        new_json_obj['latitude'] = obj.get('latitude')
        new_json_obj['longitude'] = obj.get('longitude')
        new_json_obj['stars'] = obj.get('stars')
        sub_business.append(new_json_obj)
        business_set.add(obj.get('business_id'))

for obj in reviews:
    if obj.get('business_id') in business_set:
        new_json_obj = {}
        new_json_obj['review_id'] = 'review_id'
        new_json_obj['business_id'] = obj.get('business_id')
        new_json_obj['user_id'] = obj.get('user_id')
        new_json_obj['stars'] = obj.get('stars')
        new_json_obj['text'] = obj.get('text')
        new_json_obj['useful'] = obj.get('useful')
        new_json_obj['funny'] = obj.get('funny')
        new_json_obj['cool'] = obj.get('cool')
        sub_review.append(new_json_obj)


with open('sub_business.json', 'w', encoding='utf-8') as file:
    json.dump(sub_business, file, ensure_ascii=False, indent=4)
with open('sub_review.json', 'w', encoding='utf-8') as file:
    json.dump(sub_review, file, ensure_ascii=False, indent=4)


"""choose state """
# state_business_dic = {}
# state_review_dic = {}
# business_review_dic = {}
# business_state_dic = {}

# for obj in businesses:
#     business_id = obj.get('business_id')
#     state = obj.get('state')
#     review_count = obj.get('review_count')
#     state_business_dic[state] = state_business_dic.get(state, 0) + 1
#     business_state_dic[business_id] = state
#
# for obj in reviews:
#     business_id = obj.get('business_id')
#     state = business_state_dic[business_id]
#     state_review_dic[state] = state_review_dic.get(state, 0) + 1
#
# for key in sorted(state_business_dic):
#     # print(f"{key:<{4}} : {state_business_dic[key]}")
#     print(f"{key:<{3}}: {state_business_dic[key]:<{8}}  {state_review_dic[key]}")


# print(state_business_dic)
#
# print(state_review_dic)