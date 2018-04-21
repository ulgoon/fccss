from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "Flask init complete!"

# TODO: localhost:5000/calculate로 들어왔을 때
# 1+3 의 결과값을 클라이언트에 넘겨주기

@app.route('/calculate')
def calc():
    sum = 0
    sum = 1 + 3
    return str(sum)

if __name__ == '__main__':
    app.run(host="127.0.0.1")
