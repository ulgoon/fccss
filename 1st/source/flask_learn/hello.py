from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def index(name=None):
#1    return 'hello world'
    return render_template('index.html', name=name)    

@app.route('/about')
def about(name=None):
    return render_template('about.html', name=name)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
