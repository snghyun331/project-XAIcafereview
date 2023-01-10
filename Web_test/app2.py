from flask import Flask, render_template, jsonify, request, redirect
from py_src.show_wordcloud import show_wordcloud
from py_src.show_predict import show_predict
import save_csv
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 한글 깨짐 방지

#지도검색페이지
@app.route('/', methods=['GET', 'POST'])
#html연결하기
def structure():
    if request.method=='POST':
        print("button click")
        return redirect('/result')
    return render_template('index.html')

# 카페 분석 결과 화면 보여주기
@app.route('/result')
def show_result1():
    cafe_info = show_wordcloud('동작','오후홍콩')
    average_score = show_predict('동작','오후홍콩')
    return render_template('result.html', cafe_info=cafe_info, score=average_score)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8888, debug=True)
