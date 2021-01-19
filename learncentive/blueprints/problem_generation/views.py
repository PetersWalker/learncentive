from flask import jsonify, json, Blueprint, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required

from .problem_set import ProblemSet
from learncentive.blueprints.classroom.models import User
# from learncentive.utils import jwt_required_else_redirect


blueprint = Blueprint('problem_generation', __name__)

"""

DEPRECIATED, NO LONGER TESTED

# API routes serving problems to the React app in classroom template
@blueprint.route('/<int:amount_of_probs>/<int:difficulty>/<int:course_id>', methods=['GET'])
@jwt_required
def problem_set_a_la_carte(amount_of_probs=10, difficulty=0, course_id=0):
    new_problem_set = ProblemSet.alacarte(amount_of_probs, difficulty, course_id)
    return jsonify(vars(new_problem_set))
    
"""

@blueprint.route('/<string:json_data>', methods=['GET'])
@jwt_required
def problem_set_from_old(json_data):

    if json_data == 'first':
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        grades = user.grades
        new_problem_set = ProblemSet.from_grades(grades)

    else:
        old_problem_set = ProblemSet(json.loads(json_data))
        new_problem_set = old_problem_set.new_problem_set()

    response = make_response(jsonify(vars(new_problem_set)))

    response.headers.add("Access-Control-Allow-Credentials", "true")
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:8080")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


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
