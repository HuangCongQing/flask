'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-07-16 11:29:58
@LastEditors: HCQ
@LastEditTime: 2020-07-16 12:19:39
'''


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! 20200716'

if __name__ == '__main__':
    app.debug = True
    app.run(port=9000)
