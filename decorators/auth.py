from flask import  redirect, url_for, session

from functools import wraps
def requires_login(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if ("username" not in session and "user_id" not in session):
            return redirect(url_for("index"))
        else:
            return f(*args, **kwargs)
    return decorator

def no_requires_login(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if ("username" in session and "user_id" in session):
            return redirect(url_for("task.index"))
        else:
            return f(*args, **kwargs)
    return decorator