# as_list.csv 데이터를 불러와서 전처리 하는 파일

import re
import pandas as pd
from konlpy.tag import Okt
from collections import Counter
import warnings
warnings.filterwarnings('ignore')
import os

#강제 경로설정
os.environ['JAVA_HOME']=r'C:\Program Files\Java\jdk-19\bin\server'


class as_list:
    def __init__(self,region,name):
        self.df = pd.read_csv('as_list.csv',encoding = 'utf8', index_col = 0)
        self.region = region
        self.name = name
    
    # 해당 카페의 전체 별점 가져오는 함수
    def get_star(self):
        df = self.df
        df = df[(df['region'] == self.region)&(df['cafe_name'] == self.name)]
        average_star = df['average_star'].values[0]
        return average_star   
    
    
    # 긍정 단어들만 뽑아서 리스트로 만들어주는 함수
    def get_pos(self):
        df = self.df
        df = df[(df['region'] == self.region)&(df['cafe_name'] == self.name)]
        pos_df = df[df['value'] > 0]
        pos_word_list = pos_df['word'].values.tolist()
        okt = Okt()
        stopwords = ['번','때','하다','분','요','우','있다','되다','곳','보다','나오다','어쩌구','아주','시','수','되다','여기다']
        re_word_list = []
        for pos_word in pos_word_list:
            word = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣]',"", pos_word)
            morph = okt.pos(word, stem = True, norm = True)
            for re_word, tag in morph:
                if tag in ['Noun','VerbPrefix','Adjective','Exclamation','Verb'] and re_word not in stopwords:
                    re_word_list.append(re_word)
        re_word_list = [w if w != '밀크' else '밀크티' for w in re_word_list ]
        re_word_list = [w if w != '티' else '' for w in re_word_list]
        re_word_list = ' '.join(re_word_list).split()
        return re_word_list
    
    
    # 부정 단어들만 뽑아서 리스트로 만들어주는 함수
    def get_neg(self):
        df = self.df
        df = df[(df['region'] == self.region)&(df['cafe_name'] == self.name)]
        neg_df = df[df['value'] < 0]
        neg_word_list = neg_df['word'].values.tolist()
        okt = Okt()
        stopwords = ['번','때','하다','분','요','우','있다','되다','곳','보다','나오다','어쩌구','아주','시','수','되다','여기다']
        re_word_list = []
        for neg_word in neg_word_list:
            word = re.sub('[^ㄱ-ㅎㅏ-ㅣ가-힣]',"", neg_word)
            morph = okt.pos(word, stem = True, norm = True)
            for re_word, tag in morph:
                if tag in ['Noun','VerbPrefix','Adjective','Exclamation','Verb'] and re_word not in stopwords:
                    re_word_list.append(re_word)
        re_word_list = [w if w != '밀크' else '밀크티' for w in re_word_list ]
        re_word_list = [w if w != '티' else '' for w in re_word_list]
        re_word_list = ' '.join(re_word_list).split()
        return re_word_list
    
    
    # 긍정 단어 빈도 수 계산해주는 함수
    def pos_word_counter(self):
        words_list = self.get_pos()
        count = Counter(words_list)
        return count
    
    
    # 부정 단어 빈도 수 계산해주는 함수    
    def neg_word_counter(self):
        words_list = self.get_neg()
        count = Counter(words_list)
        return count
    
    
    
    
