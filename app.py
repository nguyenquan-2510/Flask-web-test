from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hahahah hello from flask !"

@app.route('/id')
def id():
    return "???"

@app.route('/name')
def name():
    return "Hello world"