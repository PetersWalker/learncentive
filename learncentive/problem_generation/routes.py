from flask import Blueprint
import json
problem_generation = Blueprint('problem_generation', __name__)

from learncentive.problem_generation.problem_set import ProblemSet

#API routes serving React app in classroom template
@problem_generation.route('/<int:amount_of_probs>/<int:type_of_prob>', methods=['GET'])
def problem_set_a_la_carte(amount_of_probs, type_of_prob):
    new_problem_set = ProblemSet.alacarte(amount_of_probs, type_of_prob)
    return json.dumps(vars(new_problem_set))

@problem_generation.route('/<string:json_data>', methods=['GET'])
def problemset_from_old(json_data):
    old_problem_set = ProblemSet(json.loads(json_data))
    new_problem_set = old_problem_set.new_problem_set()
    return json.dumps(vars(new_problem_set))


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
