from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os
#database
from database.config import db, User, Task
#routes
from routes.auth import bp as bp_auth
from routes.task import bp as bp_task

load_dotenv(".env.local")

app = Flask(__name__)
app.secret_key = os.getenv("APP_KEY")

app.register_blueprint(bp_auth)
app.register_blueprint(bp_task)

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

@app.get("/ok")
def health_check ():
    return jsonify({"msg": "ok"})

@app.errorhandler(404)
def not_found (error):
    return render_template("pages/errors/404.html", error=error)

with db:
    db.create_tables([User, Task])