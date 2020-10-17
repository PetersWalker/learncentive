from flask import Blueprint, request, render_template, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token, set_access_cookies,
    set_refresh_cookies, jwt_refresh_token_required, get_jwt_identity,
    unset_jwt_cookies
)

from learncentive.extensions import db
from learncentive.users.models import User
from learncentive.users.forms.login_signup import SignupForm, LoginForm

users = Blueprint('users', __name__)

@users.route('/register', methods=['POST'])
def register():
    form = SignupForm(request.form)
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
        return 'bad request, invalid form', 400


@users.route('/token/auth', methods=['POST'])
def login():
    form = LoginForm(request.form)
    user = User.query.filter_by(email=form.email.data, password=form.password.data).first()

    if user:
        # create tokens
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        # construct cookies and response.
        response = jsonify({'login': True})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response, 200

    else:
        return jsonify({'login': False}), 401


@users.route('/token/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)

    response = jsonify({'refresh': True})
    set_access_cookies(response, access_token)
    return response, 200


@users.route('/token/remove', methods=['POST'])
def logout():
    current_user = get_jwt_identity()
    response = jsonify({'logout': True})
    unset_jwt_cookies(response)
    return response, 200