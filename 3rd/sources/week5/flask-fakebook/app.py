from flask import Flask, render_template, request
import sqlite3 as lite


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            name = request.form['name']
            age = request.form['age']
            email = request.form['email']

            with lite.connect('users.db') as conn:
                cur = conn.cursor()

                cur.execute("INSERT INTO user(name, age, email) VALUES(?,?,?)", (name, age, email))
                conn.commit()

                msg = "signup complete"
        except:
            conn.rollback()
            msg = "signup failed"
        finally:
            return render_template("signup.html", msg = msg)
            conn.close()

@app.route('/users')
def users():
    conn = lite.connect("users.db")
    conn.row_factory = lite.Row
    
    cur = conn.cursor()
    cur.execute("SELECT * from user")

    rows = cur.fetchall()
    conn.close()
    return render_template("users.html", rows = rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7070')
