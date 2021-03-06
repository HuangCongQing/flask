from sqlalchemy.testing.config import db

'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-07-16 13:49:29
@LastEditors: HCQ
@LastEditTime: 2020-07-16 17:49:38
'''

# coding:utf-8

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

'''配置数据库'''
app = Flask(__name__)
app.config['SECRET_KEY'] ='hard to guess'
# 这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名jianshu,连接方式参考 \
# http://docs.sqlalchemy.org/en/latest/dialects/mysql.html
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost:3306/flaskdb'
#设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
#实例化
db = SQLAlchemy(app)

'''定义模型，建立关系'''
class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    user = db.relationship('User', backref='role')

    #repr()方法显示一个可读字符串，虽然不是完全必要，不过用于调试和测试还是很不错的。
    def __repr__(self):
        return '<Role {}> '.format(self.name)
