import  pymysql
from app import app
import mysql
from flask import jsonify
from flask import flash, request
#from werkzeug import generate_password_hash, check_password_hash


@app.route('/AccTot/Acc')
def Acc():
    try:
        conn = pymysql.connect(host='127.0.0.1', database='ciwa', user='root', password='1234')
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('SELECT CiwaType, COUNT(*) FROM internal_detection WHERE( (Datetime BETWEEN "2020-06-01 00:00:00" AND "2020-06-10 00:00:00") AND Accepted=1)')
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e_1:
        print(e_1)

    finally:
        cur.close()
        conn.close()

@app.route('/AccTot/Tot')
def Tot():
    try:
        conn = pymysql.connect(host='127.0.0.1', database='ciwa', user='root', password='1234')
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute('SELECT CiwaType, COUNT(*) FROM apperance_detection WHERE Datetime BETWEEN "2020-06-01 00:00:00" AND "2020-06-10 00:00:00"')
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e_2:
        print(e_2)

    finally:
        cur.close()
        conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'Not Found:' +request.url,
        }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run()
