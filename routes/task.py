from flask import Blueprint, render_template, session
from decorators.auth import requires_login

bp = Blueprint("task", __name__, url_prefix="/task")

@bp.get("/")
@requires_login
def index ():
    username = session["username"]
    return render_template("pages/task/index.html", username=username)
