from wtforms import StringField, PasswordField, SubmitField, validators
from flask_wtf import FlaskForm

class SignupForm(FlaskForm):
    name = StringField(
        'Username',
        [validators.length(max=80)],
        render_kw={"placeholder": "Name"}
    )
    email = StringField(
        'Email',
        [validators.length(max=120)],
        render_kw={"placeholder": "Email"}
    )
    password = PasswordField(
        'Password',
        [validators.EqualTo('confirm', message='passwords must match')],
        render_kw={"placeholder": "Password"}
    )
    confirm = PasswordField(
        'Repeat Password',
        render_kw={"placeholder": "Repeat Password"})
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        [validators.length(max=120)],
        render_kw={"placeholder": "Email"}
    )
    password = PasswordField(
        'Password',
        render_kw={"placeholder": "Password"}
    )
