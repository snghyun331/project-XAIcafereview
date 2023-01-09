import pandas as pd
'''
from pymongo import MongoClient

#<파일 불러오기>
path = f'all_review(from Mapo2Songpa).csv'
data = pd.read_csv(path)
data.reset_index(inplace=True) #index생성
data_dict = data.to_dict('records')

client = MongoClient('localhost', 27017)
db =client.vegan
collection = db['vegan']
collection.insert_many(data_dict)
'''
#<파일 불러오기>
path = f'all_review(from Mapo2Songpa).csv'
df = pd.read_csv(path)
#groups = df.groupby('카페명')
#result = dict(list(groups))
#result['프릳츠 도화점']['별점']
#print(result['프릳츠 도화점'])
store = '프릳츠 도화점'
storeiwant = df[df['카페명'].isin([store])]
print(storeiwant)
print(storeiwant['별점'])