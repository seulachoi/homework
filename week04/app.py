from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework_week04

##HTML 화면 기본
@app.route('/')
def home():
    return render_template('index.html')

##주문하기 API
@app.route('/order', methods=['POST'])
def save_order():
    #request.form으로 클라이언트가 준 정보를 가져오기
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    #위 정보를 데이터 dictionary형태로
    data = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    #dic형태 데이터를 db에 저장
    db.dbhomework_week04.insert_one(data)

    return jsonify({'result':'success', 'msg':'포스트성공'})

##주문 목록보기 API
@app.route('/order', methods=['GET'])
def show_order():
    orders = list(db.dbhomework_week04.find({},{'_id':False}))
    #db에서 리스트 형태로 가져온 데이터를, 클라이언트가 get 요청하면 'orders'라는 키 값으로 넘겨주기
    return jsonify({'result':'success', 'orders':orders})

if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)