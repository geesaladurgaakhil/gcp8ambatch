import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the First Python Application!!"

@app.route("/test1")
def test1():
    return "Response from Test API 1"

@app.route("/test2")
def test2():
    return "Response from Test API 2"

@app.route("/test3")
def test3():
    return "Response from Test API 3"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
