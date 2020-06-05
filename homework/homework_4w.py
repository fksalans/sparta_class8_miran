from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db=client.dbsparta

@app.route('/')
def home():
    return render_template('homework_4w.html')

@app.route('/shopping', methods=['GET'])
def listing():
    result = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success'})

@app.route('/shopping', methods=['POST'])
def purchase():
    person_receive = request.form['person_give']
    volume_receive = request.form['volume_give']
    address_receive = request.form['address_give']
    mobile_receive = request.form['mobile_give']

    order = {
        'person': person_receive,
        'volume': volume_receive,
        'address': address_receive,
        'mobile': mobile_receive
    }

    db.orders.insert_one(order)
    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
