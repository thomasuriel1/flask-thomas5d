from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/quien')
def hello():
    return 'Argentino 1-0 Corinthians'