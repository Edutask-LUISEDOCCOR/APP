from flask import Flask, render_template, session
from database.config import db, User
#routes
from routes.auth import bp as bp_auth

app = Flask(__name__)
app.secret_key = "secret_key"

app.register_blueprint(bp_auth)

@app.before_request
def init_database():
     db.connect()

@app.after_request
def close_database(response):
    db.close()
    return response

@app.get("/")
def index ():
    users = User.select().count()
    return render_template("index.html", users=users)

@app.errorhandler(404)
def not_found (error):
    print(error)
    return render_template("pages/errors/404.html", error=error)

with db:
    db.create_tables([User])