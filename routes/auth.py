from flask import Blueprint, render_template
from forms.auth import LoginForm

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login")
def login () :
    form = LoginForm()
    return render_template("auth/index.html", title="Login", form=form)