'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-07-16 11:29:58
@LastEditors: HCQ
@LastEditTime: 2020-07-16 11:37:16
'''


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'