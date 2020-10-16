from flask import Blueprint, request, render_template

from learncentive.extensions import db
from learncentive.users.models import User
from learncentive.users.forms.register import RegistrationForm

users = Blueprint('users', __name__)

@users.route('/register', methods=['POST'])
def register():
    form = RegistrationForm(request.form)
    user_exists = User.query.filter_by(name=form.name.data).first()

    if user_exists:
        return 'Conflict', 409
    elif form.validate():
        user = User(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
            grades=[0])
        db.session.add(user)
        db.session.commit()
        return render_template('catalog.html'), 201
    else:
        return 'bad request', 400
