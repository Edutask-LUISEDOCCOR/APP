from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from forms.auth import AuthForm
from models.users import UserModel
from database.config import User
from lib.bcrypt import verify_password
from decorators.auth import no_requires_login


bp = Blueprint("auth", __name__, url_prefix="/auth")
usermodel = UserModel(User)

@bp.route("/login", methods=["GET", "POST"])
@no_requires_login
def login():
    form = AuthForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data
        user = usermodel.getByUsername(username)
        if(user):
            if(verify_password(password, user.password)):
                session["username"] = username
                session["user_id"] = user.id
                return redirect(url_for("task.index"))  
            else: 
               flash("invalid credentials")
        else: 
            flash("The username does not exist")
    return render_template("pages/auth/index.html", opposite="signup", title="Login", form=form)

@bp.route("/signup", methods=["GET", "POST"])
@no_requires_login
def signup():
    form = AuthForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data
        if(not usermodel.getByUsername(username)):
            user = usermodel.create(username, password)
            if(user):
                session["username"] = username
                session["user_id"] = user.id
                return redirect(url_for("task.index"))
            else:
                flash("Error creating user")
        else:
            flash("The username already exists")
    return render_template("pages/auth/index.html", opposite="login", title="Sign Up", form=form)      