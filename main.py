from flask import Flask, render_template
from routes.auth import bp as bg_auth

app = Flask(__name__)
app.register_blueprint(bg_auth)

@app.get("/")
def index ():
    return render_template("index.html", name="Luis Eduardo")

@app.errorhandler(404)
def not_found (error):
    print(error)
    return render_template("errors/404.html", error=error)
