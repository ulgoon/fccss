from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Flask!"

@app.route('/hello')
def hello():
    sum = 0
    for i in range(1,10+1):
        sum = sum + i
    return str(sum)

if __name__ == "__main__":
    app.run(host = "127.0.0.1")
