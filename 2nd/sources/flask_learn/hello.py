
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "First Flask Application!!!"

@app.route('/about')
def about():
    return "This is about"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
