from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from load import as_list


class word_cloud:
    def __init__(self,region,name):
        self.region = region
        self.name = name
    
    
    # 워드클라우드 글씨 핑크색 - 긍정
    def word_pink_func(self,
            word, font_size, position, orientation, random_state = None, **kwargs):
        return ("hsl(291,68%%, %d%%)" % np.random.randint(30,85))
        # hsl: https://www.w3schools.com/colors/colors_hsl.asp  참고
    
    
    # 워드클라우드 글씨 회색 - 부정    
    def word_grey_func(self,
        word, font_size, position, orientation, random_state = None, **kwargs):
        return ("hsl(0,0%%, %d%%)" % np.random.randint(10,80))
    
    
    # 긍정 단어 워드클라우드 만들기   
    def make_cloud_image_pos(self,file_name):
        icon = Image.open("static/assets/mask_img/heart.png")
        mask = Image.new("RGB", icon.size, (255,255,255))
        mask.paste(icon, icon)
        mask = np.array(mask)
        
        no = {"너무", "정말", "이제", "지금","이게","좀"}
        font_path = 'static/font/BMDOHYEON_ttf.ttf'
        pos_word = dict(as_list.as_list(self.region,self.name).pos_word_counter())
        
        wc = WordCloud(
            font_path=font_path, 
            background_color='white',
            width = 800, 
            height = 450, 
            stopwords = no,
            mask = mask
        )
        wc_pos = wc.generate_from_frequencies(pos_word)

        fig = plt.figure(figsize=(20,20))
        plt.imshow(wc_pos.recolor(color_func = self.word_pink_func), interpolation='nearest')
        plt.axis('off')
        fig.savefig("static/assets/img/{0}_pos.png".format(file_name))
        
        
    # 부정 단어 워드클라우드 만들기
    def make_cloud_image_neg(self,file_name):
        icon = Image.open("static/assets/mask_img/bad.png")
        mask = Image.new("RGB", icon.size, (255,255,255))
        mask.paste(icon, icon)
        mask = np.array(mask)
        
        no = {"너무", "정말", "이제", "지금","이게","좀"}
        font_path = 'static/font/BMDOHYEON_ttf.ttf'
        neg_word = dict(as_list.as_list(self.region,self.name).neg_word_counter())
        
        wc = WordCloud(
            font_path=font_path, 
            background_color='white',
            width = 800, 
            height = 450, 
            stopwords = no,
            mask = mask
        )
        wc_neg = wc.generate_from_frequencies(neg_word)

        fig = plt.figure(figsize=(20,20))
        plt.imshow(wc_neg.recolor(color_func = self.word_grey_func), interpolation='nearest')
        plt.axis('off')
        fig.savefig("static/assets/img/{0}_neg.png".format(file_name))
        