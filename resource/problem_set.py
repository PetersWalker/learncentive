from flask_restful import Resource
from learncentive.src.problem import Problem
from learncentive.src.cache import create_cached_random_bank

from random import randint

class ProblemSet(Resource):

    def get(self, amount_of_probs):
        #probably a better way of doing this
        problem_dict = {}
        seed = randint(0,900)
        for i in range(amount_of_probs):

            problem = Problem.randomly_generate(seed=seed)
            problem_dict[problem.string] = problem.answer
            seed += 1
        return problem_dict
