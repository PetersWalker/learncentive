from flask import Blueprint, request, jsonify

from learncentive.extensions import db
from learncentive.users.models import User

users = Blueprint('users', __name__)


@users.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    test = User.query.filter_by(email=email).first()
    if test:
        return jsonify(message="that email already exists"), 409
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        grades = [0]
        user = User(name=name, email=email, password=password, grades=grades)
        db.session.add(user)
        db.session.commit()
        return jsonify('success'), 201
