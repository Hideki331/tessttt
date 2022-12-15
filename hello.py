from flask import Flask
from flask import render_template

app = Flask(__name__)

bullets = [

    'aaaa1',
    'aaaa2',
    'aaaa3',
    'aaaa4',
    'aaaa5',
    'aaaa6'
]

@app.route("/")
def hello_world():
    return render_template('hello.html',bullets=bullets)