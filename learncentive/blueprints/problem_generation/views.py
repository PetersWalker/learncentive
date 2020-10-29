from flask import jsonify, json, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from .problem_set import ProblemSet
from learncentive.blueprints.users.models import User


blueprint = Blueprint('problem_generation', __name__)


# API routes serving React app in classroom template
@blueprint.route('/<int:amount_of_probs>/<int:type_of_prob>', methods=['GET'])
@jwt_required
def problem_set_a_la_carte(amount_of_probs, type_of_prob):
    new_problem_set = ProblemSet.alacarte(amount_of_probs, type_of_prob)
    return jsonify(vars(new_problem_set))


@blueprint.route('/<string:json_data>', methods=['GET'])
@jwt_required
def problemset_from_old(json_data):

    if json.loads(json_data) == 'first':
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        grades = user.grades
        new_problem_set = ProblemSet.from_grades(grades)

    else:
        old_problem_set = ProblemSet(json.loads(json_data))
        new_problem_set = old_problem_set.new_problem_set()

    return jsonify(vars(new_problem_set))


""" API response is of the form:
   {'grades': [.92, .5]
    'graded': False,
    'problems': [
        {'question': '', 'answer':'', 'difficulty': 0, 'result':True},
        {'question': '', 'answer':'', 'difficulty': 0, 'result':False},
        {'question': '', 'answer':'', 'difficulty': 1, 'result':False}
        ],
    }
"""
