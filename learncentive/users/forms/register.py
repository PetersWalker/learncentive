from wtforms import Form, StringField, PasswordField, SubmitField, validators


class RegistrationForm(Form):
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

