from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc')
def calc():
    # result => 3, 1
    result = 3 + 1
    return render_template('calc.html', msg = result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
