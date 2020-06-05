from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])    #리뷰입력
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    bookreview = {
        'title': title_receive,
        'author': author_receive,
        'review': review_receive
    }
    db.bookreviews.insert_one(bookreview)
    return jsonify({'result':'success', 'msg': '리뷰 작성 성공!'})


@app.route('/reviews', methods=['GET']) #입력된 DB 보여주기
def read_reviews():
    bookreviews = list(db.bookreviews.find({},{'_id':0})) #_id:0 의미는 false로 지정하는 것
    return jsonify({'result':'success', 'bookreviews': bookreviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)