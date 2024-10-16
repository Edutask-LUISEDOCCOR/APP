from flask import Blueprint, render_template, session, request, url_for, redirect, flash
from decorators.auth import requires_login
from models.user import UserModel
from models.task import TaskModel
from forms.task import TaskForm

bp = Blueprint("task", __name__, url_prefix="/task")
user_model = UserModel()
task_model = TaskModel()

@bp.get("/")
@requires_login
def index ():
    tasks =  user_model.getById(session["user_id"]).tasks
    return render_template("pages/task/index.html", username=session["username"], tasks=tasks)

@bp.get("/delelte/<int:task_id>")
def delete(task_id):
    pass

@bp.get("/update/<int:task_id>")
def update(task_id):
    pass

@bp.route("/create", methods=["GET", "POST"])
def create():
    form = TaskForm(request.form)
    if(request.method == "POST" and form.validate() ):
        if(task_model.create(title=form.title.data, content=form.content.data, user_id=session["user_id"])):
            return redirect(url_for("task.index"))
        else:
            flash("Error creating task")
    return render_template("pages/task/form.html", form=form, username=session["username"], title="Create a new task") 