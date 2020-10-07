from random import randint
import json
from flask_restful import Resource

from learncentive.problem_generation.problem_set import ProblemSet

class ProblemSetGenerator(Resource):
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
    def get(self, json_data):
        old_problem_set = ProblemSet(json.loads(json_data))
        new_problem_set = old_problem_set.new_problem_set()
        return json.dumps(vars(new_problem_set))

class ProblemSetALaCarte(Resource):

    def get(self, amount_of_probs, type_of_prob):
        new_problem_set = ProblemSet.alacarte(amount_of_probs, type_of_prob)
        return json.dumps(vars(new_problem_set))
