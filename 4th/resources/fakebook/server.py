from flask import Flask, render_template, request
import sqlite3 as lite


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# signup => 사용자가 정보를 입력하는 페이지
@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            name = request.form['name']
            age = request.form['age']
            lang = request.form['lang']

            with lite.connect('users.db') as conn:
                cur = conn.cursor()
                cur.execute('INSERT INTO user(name, age, lang) VALUES(?,?,?);', (name, age, lang))
                conn.commit()

                msg = "Sign up Success"
        except:
            conn.rollback()
            msg = "Sign up Failed"
        finally:
            return render_template("signup.html", msg = msg)

# users => 모든 사용자를 조회할 수 있는 페이지
@app.route('/users')
def users():
    conn = lite.connect('users.db')
    conn.row_factory = lite.Row

    cur = conn.cursor()
    cur.execute("SELECT * from user;")

    rows = cur.fetchall()
    conn.close()
    return render_template("users.html", rows = rows)


@app.route('/hello')
def hello():
    sum = 0
    for i in range(1,10+1):
        sum = sum + i
    return str(sum)

if __name__ == "__main__":
    app.run(host = "127.0.0.1")
