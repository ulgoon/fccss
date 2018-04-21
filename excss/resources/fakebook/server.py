from flask import Flask, render_template, request
import sqlite3 as lite


app = Flask(__name__)

@app.route('/')
def index():
    msg = "Get out of here"
    return render_template("index.html", msg = msg)



@app.route('/users')
def users():
    with lite.connect('users.db') as conn:
        conn.row_factory = lite.Row

        cur = conn.cursor()
        cur.execute("SELECT * from user;")
        rows = cur.fetchall()

    return render_template("users.html", rows = rows)

# TODO: /submit에서 POST로 넘어온 자료를 DB에 저장하기
@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        msg = "submit success"
    else:
        msg = "get success"
    return render_template("users.html", msg = msg)

# TODO: localhost:5000/calculate로 들어왔을 때
# 1+3 의 결과값을 클라이언트에 넘겨주기
@app.route('/calculate')
def calc():
    sum = 0
    sum = 1 + 3
    return str(sum)

if __name__ == '__main__':
    app.run(host="127.0.0.1")
