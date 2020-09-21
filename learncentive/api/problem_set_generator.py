from random import randint
import json
from flask_restful import Resource

from learncentive.problem_generation.problem_set import ProblemSet

# this whole module will change based on new way of generating problems
# 1. initial get(user history/skill level in database)
# 2. each subsequet get:
#       get(grade)

class ProblemSetGenerator(Resource):

    """ API response is of the form:

       {'quantity':{0:2, 1:1},
        'correct': {0:1, 1:0},
        'grades': {0:.92, 1:.5},
        'graded': False,
        'problems': [
            {'question': '', 'answer':'', 'difficulty': 0, 'result':True},
            {'question': '', 'answer':'', 'difficulty': 0, 'result':False},
            {'question': '', 'answer':'', 'difficulty': 1, 'result':False}
            ],
        }
    """

    def get(self, problem_set):
        old_problem_set = ProblemSet.from_json(problem_set)
        new_problem_set = old_problem_set.new_problem_set()
        return new_problem_set.to_json()

class ProblemSetALaCarte(Resource):

    def get(self, amount_of_probs, type_of_prob):
        new_problem_set = ProblemSet.alacarte(amount_of_probs, type_of_prob)
        return new_problem_set.to_json()

def create_problem_set(amount_of_probs, type_of_prob):
    problem_set = [generate_problem_handle_index(type_of_prob)
                   for i in range(amount_of_probs)]
    return problem_set
