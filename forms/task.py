from wtforms import Form, StringField, validators

class TaskForm(Form):
    title = StringField("Title", [validators.DataRequired()])
    content = StringField("Content")