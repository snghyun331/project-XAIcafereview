import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from predict import sentiment_predict
from load.cafereviewDB import load_infos
import warnings
warnings.filterwarnings('ignore')


# 해당 카페에 대한 전체적인 반응을 알려주는 함수 (이 카페는 전체적으로 78% 확률로 긍정적인 반응)
def show_predict(region, cafe_name):
    List = load_infos(region, cafe_name)
    only_reviews = []
    for i in List:
        review = i['review_text']
        only_reviews.append(review)
    
    total = 0   
    count = 0   
    for only_review in only_reviews:
        count += 1
        score = sentiment_predict(only_review)
        total += score
        
    average_score = round((total / count), 3)
    
    return average_score