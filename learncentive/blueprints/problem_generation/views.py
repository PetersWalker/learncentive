from flask import jsonify, json, Blueprint
from .problem_set import ProblemSet


blueprint = Blueprint('problem_generation', __name__)


# API routes serving React app in classroom template
@blueprint.route('/<int:amount_of_probs>/<int:type_of_prob>', methods=['GET'])
def problem_set_a_la_carte(amount_of_probs, type_of_prob):
    new_problem_set = ProblemSet.alacarte(amount_of_probs, type_of_prob)
    return jsonify(vars(new_problem_set))


@blueprint.route('/<string:json_data>', methods=['GET'])
def problemset_from_old(json_data):
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
