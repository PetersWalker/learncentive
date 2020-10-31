from flask import request, jsonify, render_template, Blueprint, redirect, url_for
from flask_jwt_extended import (
    create_access_token, create_refresh_token, set_access_cookies,
    set_refresh_cookies, jwt_refresh_token_required, get_jwt_identity,
    unset_jwt_cookies, jwt_required
)

from learncentive.extensions import db
from learncentive.blueprints.users.models import User
from learncentive.blueprints.users.forms.login_signup import SignupForm, LoginForm


blueprint = Blueprint('users', __name__, template_folder='templates')


@blueprint.route('/account')
@jwt_required
def account():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    return render_template('account.html', user=user)


@blueprint.route('/register', methods=['POST'])
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
        response = jsonify({'register': True})

        return response, 201
    else:
        return 'bad request, invalid form', 400


@blueprint.route('/token/auth', methods=['POST'])
def login():
    form = LoginForm(request.form)
    user = User.query.filter_by(email=form.email.data, password=form.password.data).first()

    if user:
        # create tokens
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        # set cookies and response.
        response = redirect(url_for('users.account'))
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response

    else:
        return jsonify({'login': False}), 401


@blueprint.route('/token/refresh', methods=['POST', 'GET'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)

    response = jsonify({'refresh': True})
    set_access_cookies(response, access_token)
    return response, 200


@blueprint.route('/token/remove', methods=['POST'])
def logout():
    response = jsonify({'logout': True})
    unset_jwt_cookies(response)
    return response, 200
