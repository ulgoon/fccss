from flask import Flask
from flask import render_template
from flask import request
import sqlite3 as lite


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc')
def calc():
    # result => 3, 1
    result = 3 + 1
    return render_template('calc.html', msg = result)

# to show users list from users.db
@app.route('/users')
def users():
    conn = lite.connect("users.db")
    conn.row_factory = lite.Row

    cur = conn.cursor()
    cur.execute('select * from users;')

    rows = cur.fetchall()

    return render_template('users.html', rows = rows)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/postuser', methods=['POST', 'GET'])
def postuser():
    if request.method == 'POST':
        try:
            name = request.form['name']
            age = request.form['age']
            lang = request.form['lang']

            with lite.connect('users.db') as conn:
                cur = conn.cursor()

                cur.execute("insert into users(name, age,lang) \
                    values (?,?,?);", (name,age,lang))
                conn.commit()
                msg = "Sign up is successfull"
        except:
            conn.rollback()
            msg = "Sign up failed"
        finally:
            return render_template("signup.html", msg=msg)
            conn.close()




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
