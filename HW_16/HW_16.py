from flask import flask

app = flask(__name__)


@app.route("/")
def hello():
    return 'Hello,World'

@app.route("/user")
def hello():
    return "My name ivan"