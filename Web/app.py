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
def structure():
    if request.method=='POST':
        print("button click")
        return redirect('/result')
    return render_template('main.html')
#html연결하기
''' 지도가 main일때
def structure():
    if request.method=='POST':
        print("button click")
        return redirect('/result')
    return render_template('index.html')
'''



# 카페 분석 결과 화면 보여주기
@app.route('/result', methods=['GET', 'POST'])
def show_result():
    cafe_info = show_wordcloud('동작','오후홍콩')
    average_score = show_predict('동작','오후홍콩')
    if request.method == 'POST':
        print("button click")
        return redirect('/result')
    return render_template('result.html', cafe_info=cafe_info, score=average_score)
'''
@app.route('/result2')
def show_result2():
    cafe_info = show_wordcloud('강남','알베르')
    average_score = show_predict('강남','알베르')
    return render_template('result.html', cafe_info=cafe_info, score=average_score)

@app.route('/result3')
def show_result3():
    cafe_info = show_wordcloud('동작','카페퍼블리코')
    average_score = show_predict('동작','카페퍼블리코')
    return render_template('result.html', cafe_info=cafe_info, score=average_score)
'''

if __name__ == '__main__':
    app.run('0.0.0.0', port=8888, debug=True)
