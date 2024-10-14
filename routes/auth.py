from flask import Blueprint, render_template, request
from forms.auth import LoginForm

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        return f"<h1>{form.username.data}"

    return render_template("auth/index.html", title="Login", form=form)

        