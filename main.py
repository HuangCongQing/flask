from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/tip1')
def tip1():
    return 'tip1'

if __name__ == '__main__':
    app.debug = True
    app.run(port=9000)
