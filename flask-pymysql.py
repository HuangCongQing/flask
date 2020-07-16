'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-07-16 18:01:02
@LastEditors: HCQ
@LastEditTime: 2020-07-16 19:34:19
'''

from flask import Flask, render_template
import pymysql
from flask.json import jsonify

app = Flask(__name__)
# 建立连接，参数分别是数据库的主机地址，用户名，密码，数据库名称，端口号
db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    db='flaskdb',
    charset='utf8' # 建数据库时要选utf8不然会报错。
)
# 使用 cursor() 方法创建一个游标对象 cursor
cur = db.cursor()

@app.route('/')
def getlist():
    #  获取所有记录列表
    sql = "select * from info" # 数据库中的一个表 info
    cur.execute(sql)
    content = cur.fetchall()
    list1 = [l for l in content]
    return jsonify(list=list1)
    # return jsonify({
    #     'id': list1[0],
    #     'name': list1[1],
    #     'age': list1[2]
    #     })
    for item in content:
        id = item[0]
        name = item[1]
        age = item[2]
        # 打印结果
        print ("id=%s,name=%s,age=%s" % \
             (id, name, age))
@app.route('/gethead')
def gethead():
	# 获取表头
    sql = "SHOW FIELDS FROM info"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]
    print(labels) # list格式
    return jsonify(items=labels)

articles = [
    {
        'id': 1,
        'title': 'the way to python',
        'content': 'tuple, list, dict'
    },
    {
        'id': 2,
        'title': 'the way to REST',
        'content': 'GET, POST, PUT'
    }
]

@app.route('/getarticle')
def test():
    # 获取所有文章列表 
    return jsonify({'articles': articles})

if __name__ == '__main__':
    app.run()
