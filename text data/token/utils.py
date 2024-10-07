import json

def state_data_sample(s = None):
    city_business = {}
    state_business = {}
    id_to_business = {}
    business_to_id = {}
    review = 0

    with open('./data/yelp_academic_dataset_business.json', 'r') as f:
        for line in f:
            content = json.loads(line)
            if content['city'] not in city_business:
                city_business[content['city']] = [content['business_id']]
                review += content['review_count']
            else:
                city_business[content['city']].append(content['business_id'])
                review += content['review_count']

            if content['state'] not in state_business:
                state_business[content['state']] = [content['business_id']]
            else:
                state_business[content['state']].append(content['business_id'])

            id_to_business[content['business_id']] = content['name']
            business_to_id[content['name']] = content['business_id']

    print("city_business contains", len(city_business), "city")
    print("state_business contains", len(state_business), "state")
    print("city_business contains", len(id_to_business), "business")
    print(review, "in city_business")

    business_review = {}
    review_to_business = {}
    review = 0

    with open('./data/yelp_academic_dataset_review.json', 'r') as f:
        for line in f:
            content = json.loads(line)

            if content['business_id'] not in id_to_business:
                print("there review not in business")
            else:
                review += 1

            if content['business_id'] not in business_review:
                business_review[content['business_id']] = [content['review_id']]
            else:
                business_review[content['business_id']].append(content['review_id'])
            review_to_business[content['review_id']] = content['business_id']

    print("business_review contains %s business" %(len(business_review)))
    print(review," ", len(review_to_business), "in review.json")

    city_business_review = {}
    for city in city_business:
        sum = len(city_business[city])
        for business in city_business[city]:
            sum += len(business_review[business])
        city_business_review[city] = sum

    state_business_review = {}
    for state in state_business:
        sum = len(state_business[state])
        for business in state_business[state]:
            sum += len(business_review[business])
            #total += len(business_review[business])
        state_business_review[state] = sum

    sort_city_business = sorted(city_business.items(), key = lambda item: len(item[1]), reverse = True)
    sort_state_business = sorted(state_business.items(), key = lambda item: len(item[1]), reverse = True)
    sort_city_business_review = sorted(city_business_review.items(), key = lambda item: item[1], reverse = True)
    sort_state_business_review = sorted(state_business_review.items(), key = lambda item: item[1], reverse = True)

    print(sort_city_business[0][0], "contains most business", len(sort_city_business[0][1]))
    print(sort_city_business_review[0][0], "contains most business and review", sort_city_business_review[0][1])
    print("state  business  review  total")

    sum = 0
    sum1 = 0
    for i in range(len(sort_state_business_review)):
        print(sort_state_business_review[i][0], len(state_business[sort_state_business_review[i][0]]), 
            sort_state_business_review[i][1]- len(state_business[sort_state_business_review[i][0]]), sort_state_business_review[i][1])
        sum += sort_state_business_review[i][1]- len(state_business[sort_state_business_review[i][0]])
        sum1 += sort_state_business_review[i][1]
    print(sum)
    print(sum1 - len(id_to_business))

    sample_state = sort_state_business_review[2][0]
    if s != None:
        sample_state = s
    print('store data of state', sample_state)
    res = 0
    with open('./data/' + sample_state + '_business.jsonl', 'w') as w:
        with open('./data/yelp_academic_dataset_business.json', 'r') as f:
            for line in f:
                content = json.loads(line)
                if content['state'] == sample_state:
                    json.dump(content, w)
                    w.write('\n')
                    res += 1
    print(res, "business in state", sample_state)

    res = 0
    with open('./data/' + sample_state + '_review.jsonl', 'w') as w:
        with open('./data/yelp_academic_dataset_review.json', 'r') as f:
            for line in f:
                content = json.loads(line)
                if content['business_id'] in state_business[sample_state]:
                    json.dump(content, w)
                    w.write('\n')
                    res += 1
    print(res, "review in state", sample_state)
    print("finish state data sample")

# get reviews of one business
def business_review_data_sample(num):
    business_id = []
    business_review = {}
    with open('./data/LA_business.jsonl', 'r') as f:
        for line in f:
            business_id.append(json.loads(line)['business_id'])
            business_review[json.loads(line)['business_id']] = []

    with open('./data/LA_review.jsonl', 'r') as f:
        for line in f:
            content = json.loads(line)
            if content['business_id'] not in business_review:
                print("business_review doesn't contain business id")
            business_review[content['business_id']].append(content['review_id'])
    
    sort_state_business = sorted(business_review.items(), key = lambda item: len(item[1]), reverse = True)
    sample_business_id = sort_state_business[3][0]
    if num != None:
        sample_business_id = sort_state_business[num][0]
    print(sample_business_id, len(business_review[sample_business_id]))

    with open('./data/B1_review.txt', 'w') as w:
        with open('./data/LA_review.jsonl', 'r') as f:
            for line in f:
                content = json.loads(line)
                if content['business_id'] == sample_business_id:
                    w.write(content['text'] + '\n')

if __name__ == '__main__':
    #business_review_data_sample(None)
    state_data_sample(None)

# state  business  review  total
# PA 34039 1598960 1632999
# FL 26330 1161545 1187875
# LA 9924 761673 771597
# TN 12056 614388 626444
# MO 10913 502385 513298
# IN 11247 489752 500999
# AZ 9912 431708 441620
# NV 7715 430678 438393
# CA 5203 348856 354059
# NJ 8536 260897 269433
# ID 4467 157572 162039
# AB 5573 109436 115009
# DE 2265 70302 72567
# IL 2145 51832 53977
# MA 2 44 46
# SD 1 42 43
# TX 4 35 39
# HI 2 34 36
# CO 3 31 34
# NC 1 29 30
# WA 2 19 21
# UT 1 19 20
# MI 1 11 12
# VI 1 11 12
# VT 1 10 11
# MT 1 6 7
# XMS 1 5 6

# business review
# _ab50qdWOk0DdB6XOrBitw 7673
# ac1AeYqs8Z4_e2X5M3if2A 7516
# oBNrLz4EDhiscSlbOl8uAw 5264
# iSRTaT9WngzB8JJ2YKJUig 5254
# VQcCL9PiNL_wkGf-uF3fjg 5146
# _C7QiQQc47AOEv4PE3Kong 4969
# GBTPC53ZrG1ZBY3DT8Mbcw 4661
# 6a4gLLFSgr-Q6CZXDLzBGQ 4480
# VaO-VW3e1kARkU9bP1E7Fw 4034
# qb28j-FNX1_6xm7u372TZA 3971