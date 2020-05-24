from random import randint

from flask.json import jsonify
from flask_restful import Resource

from learncentive.src.problem import Problem
from learncentive.src.cache import create_cached_random_bank

class ProblemSet(Resource):

    def get(self, amount_of_probs):
        #probably a better way of doing this
        response = self._construct_json_response(amount_of_probs)
        return response

    def _construct_json_response(self, amount_of_probs):
        problem_dict = {}
        seed = randint(0, 900)
        for i in range(amount_of_probs):

            problem = Problem.randomly_generate(seed=seed)
            problem_dict[i] = {
                'question': problem.string,
                'answer': problem.answer
                }
            seed += 1
        return jsonify(problem_dict)


        "problemset[1]['answer']"
