from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from flask import Flask, request


web = Flask(__name__)
# 建立与mysql数据库的链接
engine = create_engine('mysql+pymysql://root:1234@localhost/ciwa')
# 定义模型类继承父类及数据连接会话
DBsession = sessionmaker(bind=engine)  # 类似于游标
dbsession = scoped_session(DBsession)
Base = declarative_base()  # 定义一个给其他类继承的父类
md = MetaData(bind=engine)  # 元数据: 主要是指数据库表结构、关联等信息


# 定义模型类
class Employees(Base):  # 自动加载表结构
    __table__ = Table('employees', md, autoload=True)


@web.route('/api/employees/save', methods=['post'])  #查employees表的内容
def get_employees():
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
    json_data = request.get_json()
    result_detail = dbsession.query(employees).filter_by(id=json_data.get('id'))
    # 此处调用数据库的操作方法（增删改查）
    if not result_detail or not result_detail.first():
        # 无则插入
        save_date = employees(**dict(json_data))  # 动态传参
        dbsession.add(save_date)
        dbsession.commit()  # 修改类操作需要手动提交
    else:
        # 有则更新
        result_detail.update(json_data)	 # 动态更新
        dbsession.commit()
    return return_dict


if __name__ == '__main__':
    web.run(port=10000, debug=True, host='0.0.0.0', threaded=True)
    result = dbsession.query(employees).filter(employees.ID == 1001001).all()
    print(result)
    print(result[0].Level)




