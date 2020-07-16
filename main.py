'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-07-15 23:39:33
@LastEditors: HCQ
@LastEditTime: 2020-07-16 12:03:51
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    # return render_template('hello.html') # 导入html
    return tip1() # 导入html


@app.route('/tip1')
def tip1():
    return '-----tip1页面内容---------'

if __name__ == '__main__':
    app.debug = True
    app.run(port=9000)
