from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    username = StringField("Username", [validators.Length(min=4, max=25), validators.DataRequired()])
    password = PasswordField("Password", [validators.Length(min=5), validators.DataRequired()])