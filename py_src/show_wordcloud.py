# show_wordcloud를 별도 함수로 분리(app.py)
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from load import as_list
import time
import word_cloud


def show_wordcloud(region,name):
    star = as_list.as_list(region,name).get_star()
    word_cloud.word_cloud(region,name).make_cloud_image_pos("wordcloud1")
    word_cloud.word_cloud(region,name).make_cloud_image_neg("wordcloud1")
    time.sleep(0.5)
    return {'cafe_name': name, 'average_star': star}



