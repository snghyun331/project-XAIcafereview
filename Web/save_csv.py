# Lime모델 적용 및 as_list.csv로 저장하는 파일

import pandas as pd
import lime
from lime import lime_text
from lime.lime_text import LimeTextExplainer
from predict import predict
from load.cafereviewDB import load_infos
import warnings
warnings.filterwarnings('ignore')


class save_aslist:
    def __init__(self, region, cafe_name):
        self.region = region
        self.cafe_name = cafe_name
    
    # cafereviewDB로부터 정보를 받아오는 함수    
    def get_cafe_info(self):
        List = load_infos(self.region, self.cafe_name)
        return List

    # review_text 데이터만 가져오는 함수 (region X, cafe name X, average_star X)
    def extract_only_review(self):
        only_review = []
        for i in self.get_cafe_info():
            review = i['review_text']
            only_review.append(review)
        return only_review
    
    
    # Lime모델 함수
    def run_lime(self):
        region_lists = []
        cafe_lists = []
        average_star_lists = []
        word_lists = []
        value_lists = []
        
        for i in range(len(self.extract_only_review())):     #  끊김 현상 있을 경우, range 나눠서 진행 ( range(1,5).... )
            d = {0: 'negative', 1: 'positive'}
            classes = list(d.values())         # ['negative','positive']
            explainer = LimeTextExplainer(class_names=classes)
            exp = explainer.explain_instance(text_instance = self.extract_only_review()[i], 
                                    classifier_fn = predict, num_features=20,
                                    distance_metric='cosine', labels=[0,1])
            as_list = exp.as_list()
            
            for j in as_list:
                region_lists.append(self.get_cafe_info()[0]['region'])
                cafe_lists.append(self.get_cafe_info()[0]['cafe_name'])
                average_star_lists.append(self.get_cafe_info()[0]['average_star'])
                word_lists.append(j[0])
                value_lists.append(j[1])
              
        return region_lists, cafe_lists, average_star_lists, word_lists, value_lists
        
    # Lime의 as_list()로 추출한 단어 및 value 데이터를 as_list.csv에 저장하는 함수 
    def save(self):
        region_lists, cafe_lists, average_star_lists, word_lists, value_lists = self.run_lime()
        list_tuples = list(zip(region_lists, cafe_lists, average_star_lists,  word_lists, value_lists))
        df = pd.DataFrame(list_tuples, columns = ['region','cafe_name','average_star','word','value'])
        df.to_csv('as_list.csv',encoding='utf8')
        


# # 확인용
# save_aslist('동작','카페퍼블리코 본점').save()
