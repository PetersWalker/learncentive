from wtforms import Form, StringField, PasswordField, SubmitField, validators


class RegistrationForm(Form):
    name = StringField('Username', [validators.length(80)])
    email = StringField('Email', [validators.length(120)])
    password = PasswordField('Email', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Submit')

