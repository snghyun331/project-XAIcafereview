import re
import json
import numpy as np
from konlpy.tag import Okt
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model
import warnings
warnings.filterwarnings('ignore')


# 하나의 리뷰에 대한 감성분석 함수
def sentiment_predict(new_sentence):
    okt = Okt()
    tokenizer = Tokenizer(6946)
    
    with open("lstm_model/wordIndex.json","r") as json_file:
        word_index = json.load(json_file)
        tokenizer.word_index = word_index
    
    model = load_model('lstm_model/model.h5')
    
    stopwords = ['은','의','가','이','다','들','는','과','도','를','에','와','한','하다','님','.','듯','요',',']
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
    new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
    new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
    encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
    pad_new = pad_sequences(encoded, maxlen = 70) # 패딩
    score = float(model.predict(pad_new)) # 예측
    return score



# Lime 모델 생성 시 classifier_fn 인자에 들어갈 함수를 만들어주는 함수
def predict(new_sentence_lst):
    okt = Okt()
    tokenizer = Tokenizer(6946)
    
    with open("lstm_model/wordIndex.json","r") as json_file:
        word_index = json.load(json_file)
        tokenizer.word_index = word_index
    
    model = load_model('lstm_model/model.h5')

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
    



    
