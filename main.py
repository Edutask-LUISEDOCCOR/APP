from flask import Flask

app = Flask(__name__)

@app.get("/")
def index ():
    return "<h1>hello word</h1>"
