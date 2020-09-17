from random import randint
import json
from flask_restful import Resource

from learncentive.problem_generation.problem import generate
from learncentive.problem_generation.cache_config import cache_index
from learncentive.problem_generation.problem_set import ProblemSet

# this whole module will change based on new way of generating problems
# 1. initial get(user history/skill level in database)
# 2. each subsequet get:
#       get(grade)

#  need to make a universal problemset object
class ProblemSetGenerator(Resource):

    def get(self, problem_set):
        old_problem_set = ProblemSet.from_json(problem_set)
        new_problem_set = old_problem_set.new_problem_set()
        return new_problem_set.to_json()

class ProblemSetALaCarte(Resource):

    def get(self, amount_of_probs, type_of_prob):
        new_problem_set = create_problem_set(amount_of_probs, type_of_prob)
        response = construct_json_response(new_problem_set)

        return response

def create_problem_set(amount_of_probs, type_of_prob):
    problem_set = [generate_problem_handle_index(type_of_prob)
                   for i in range(amount_of_probs)]

    return problem_set


def construct_json_response(problem_set):
    problem_dict = {}

    for i, problem in enumerate(problem_set):
        problem_dict[i] = {
            'question': problem.question,
            'answer': problem.answer}

    return problem_dict


def generate_problem_handle_index(type_of_prob):
    try:
        problem = generate(type_of_prob)
    except IndexError:
        cache_index.set_to(0)
        problem = generate(type_of_prob)

    return problem
