from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html') #html 부르기

# @app.route('/mypage')
# def mypage():
#    return 'This is My Page!'

# API 역할을 하는 부분
@app.route('/test', methods=['POST']) #POST 방식
def test_post():
   title_receive = request.form['title_give'] #POST는 .form
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/test', methods=['GET']) #GET 방식
def test_get():
   title_receive = request.args.get('title_give') #GET은 .args.get
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)