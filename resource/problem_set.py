from random import randint

from flask.json import jsonify
from flask_restful import Resource

from learncentive.src.problem import Problem

class ProblemSet(Resource):

    def get(self, amount_of_probs, type_of_prob):
        response = self._construct_json_response(amount_of_probs, type_of_prob)
        return response


    def _construct_json_response(self, amount_of_probs, type_of_prob):
        problem_dict = {}
        seed = randint(0, 1001)

        for i in range(amount_of_probs):
            problem, next_seed = _try_generating_problem_with_random_seed(type_of_prob, seed)
            seed = next_seed

            problem_dict[i] = {
                'question': problem.string,
                'answer': problem.answer
                }

        return jsonify(problem_dict)

def _try_generating_problem_with_random_seed(type_of_prob, seed):
    try:
        problem, next_index = Problem.generate(type_of_prob, seed)
    except IndexError:
        seed = 0
        problem, next_index = Problem.generate(type_of_prob, seed)

    return problem, next_index


        # def _provide_random_integers(amount_needed, random_seed):

# edge cases:
#
# index error: index out of range for cached random_bank
#       solve: if list index out of range provide new random_seed

#problem:
#
# problems reuse tehe last random seed in the next problem
# solved: add two, Bad design
