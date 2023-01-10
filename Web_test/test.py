# as_list.csv 저장 Test용

import pymysql
import re
import json
import pandas as pd
import numpy as np
from konlpy.tag import Okt
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model
import lime
from lime import lime_text
from lime.lime_text import LimeTextExplainer
import warnings
warnings.filterwarnings('ignore')

connect = pymysql.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "sng24678@",
            database='cafe_reviewDB'
        )
cursor = connect.cursor()

query = """
Select region, cafe_name, average_star, review_text from reviews where cafe_name = "카페퍼블리코 본점"
"""
cursor.execute(query)

raws = cursor.fetchall()
# raws = cursor.fetchmany(size = 10)

List = []

for raw in raws:
    dict = {}
    dict['region'] = raw[0]
    dict['cafe_name'] = raw[1]
    dict['average_star'] = raw[2]
    dict['review_text'] = raw[3]
    List.append(dict)

connect.close()

only_review = []
for i in List:
    review = i['review_text']
    only_review.append(review)


okt = Okt()
tokenizer = Tokenizer(6946)

with open("lstm_model/wordIndex.json","r") as json_file:
    word_index = json.load(json_file)
    tokenizer.word_index = word_index

model = load_model('lstm_model/model.h5')


def predict(new_sentence_lst):
    return_values_lst = []
    for new_sen in new_sentence_lst:
        stopwords = ['은','의','가','이','다','들','는','과','도','를','에','와','한','하다','님','.','듯','요',',']
        new_sen = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣]',"", new_sen)
        new_sen = okt.morphs(new_sen, stem=True) # 토큰화
        new_sen = [word for word in new_sen if not word in stopwords] # 불용어 제거
        encoded = tokenizer.texts_to_sequences([new_sen]) # 정수 인코딩
        pad_new = pad_sequences(encoded, maxlen = 70) # 패딩
        positive_percentage = model.predict(pad_new)[0][0]
        negative_percentage = 1 - positive_percentage
        return_values_lst.append([negative_percentage,positive_percentage])     
    return np.array(return_values_lst)

region_lists = []
cafe_lists = []
average_star_lists = []
word_lists = []
value_lists = []


try:
    for i in range(58,63):   # total: 130    for i in range(len(only_review)):
        d = {0: 'negative', 1: 'positive'}
        classes = list(d.values())         # ['negative','positive']
        explainer = LimeTextExplainer(class_names=classes)
        exp = explainer.explain_instance(text_instance=only_review[i], classifier_fn=predict, num_features=20,
                                        distance_metric='cosine', labels=[0, 1])
        as_list = exp.as_list()
        
        for j in as_list:
            region_lists.append('동작')
            cafe_lists.append('카페퍼블리코 본점')
            average_star_lists.append(4.3)
            word_lists.append(j[0])
            value_lists.append(j[1])
except:
    pass
    
list_tuples = list(zip(region_lists, cafe_lists, average_star_lists,  word_lists, value_lists))
df = pd.DataFrame(list_tuples, columns = ['region','cafe_name','average_star','word','value'])
df.to_csv('temp3.csv',encoding='utf8')





    
