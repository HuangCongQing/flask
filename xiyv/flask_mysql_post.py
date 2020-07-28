import json
import pymysql
import requests
from flask import Flask, request, jsonify
from pymysql.cursors import DictCursor
import socket
import os
import threading
import time


app = Flask(__name__)
app.debug = True


# db = pymysql.connect(host='127.0.0.1', user='root', password='1234', port=3306, db='ciwa', charset='utf8mb4')

#只接受POST访问
@app.route("/check/date/", methods=["POST"])

def check_date():
    if not request.data:       #检查是否有数据从web传来
        return('fail')
    get_date = request.data.decode('utf-8')     #获取从web来的数据
    get_date_json = json.loads(get_date)        #把获取到的数据转成Json格式
    return jsonify(get_date_json)               #返回Json格式的数据

if __name__=='__main__':
     app.run(host='127.0.0.1', port=4321)


#
# data = {
#     'id': 1,
#     'name': 'lily',
#     'age': 11,
#     'birthplace': 'san',
#     'grade': 123
# }
#url = 'http://127.0.0.1:4321/check/date/'
#
#
# r = requests.post(url, data=json.dumps(data))
# print(r.json())
#
#


# def check():
#     #默认返回内容
#     return_dict = {'code': 1, 'result': False, 'msg': '请求成功'}
#     #判断入参是否为空
#     if request.args is None:
#         return_dict['return_code'] = '504'
#         return_dict['return_info'] = '请求参数为空'
#         return json.dumps(return_dict, ensure_ascii=False)
#     #获取传入的参数
#     get_data = request.args.to_dict()
#     month = get_data.get('month')
#     day = get_data.get('day')
#     date = str(month) + '/' + str(day)
#     #对参数进行操作
#     return_dict['result'] = sql_result(date)
#     return json.dumps(return_dict, ensure_ascii=False)
#
# #定义功能函数
# def sql_result(date):
#     conn = pymysql.connect(host='127.0.0.1', database='ciwa', user='root', password='1234')
#     cursor = conn.cursor(DictCursor)
#     cursor.execute("select * from employees ")
#     result = cursor.fetchall()
#     conn.close()
#     return result
#     print(result)
#
# if __name__=='__main__':
#     app.run(host='127.0.0.1', port=5000)
#


