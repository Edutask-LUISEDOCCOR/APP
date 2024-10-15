from flask import Blueprint, render_template, session
from decorators.auth import requires_login

bp = Blueprint("task", __name__, url_prefix="/task")

@bp.get("/")
@requires_login
def index ():
    username = session["username"]
    tasks = [
    {
        "title": "Write Blog Post on Python",
        "content": "Draft a comprehensive blog post covering the basics of Python programming, including variables, data types, loops, and functions. Add code examples and practical exercises for beginners to follow along.",
        "isDone": True
    },
    {
        "title": "Update Website Design",
        "content": "Revise the current layout of the homepage and adjust the color scheme for better readability. Ensure the new design is responsive and optimized for both mobile and desktop. Incorporate feedback from the design team.",
        "isDone": True
    },
    {
        "title": "Prepare Presentation for Client Meeting",
        "content": "Create a PowerPoint presentation for the upcoming meeting with the client. Include key project milestones, current progress, and next steps. Highlight potential risks and proposed solutions for discussion.",
        "isDone": False
    },
    {
        "title": "Research Competitor Marketing Strategies",
        "content": "Conduct an in-depth analysis of competitors' social media campaigns and marketing tactics. Identify successful strategies and provide recommendations for how to improve our current marketing approach.",
        "isDone": False

    },
    {
        "title": "Develop User Authentication Module",
        "content": "Implement user login, registration, and password reset functionalities using Flask. Ensure that data validation and error handling are properly configured. Set up JWT for token-based authentication and test thoroughly.",
        "isDone": False
    },
]

    return render_template("pages/task/index.html", username=username, tasks=tasks)
