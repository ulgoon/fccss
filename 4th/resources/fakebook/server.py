from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# signup => 사용자가 정보를 입력하는 페이지
@app.route('/signup')
def signup():
    return render_template("signup.html")

# users => 모든 사용자를 조회할 수 있는 페이지
@app.route('/users')
def users():
    return render_template("users.html")


@app.route('/hello')
def hello():
    sum = 0
    for i in range(1,10+1):
        sum = sum + i
    return str(sum)

if __name__ == "__main__":
    app.run(host = "127.0.0.1")
