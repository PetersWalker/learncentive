from random import randint
from learncentive.src.cache import random_list_of_integers

class Problem():

    def __init__(self, string='', answer=0):
        self.string = string
        self.answer = answer

    def __repr__(self):
        return self.string

    @staticmethod
    def generate(type_of_prob, random_seed=randint(0,1000)):
        if type_of_prob is None:
            raise "learncentive: No Problem Type Specified"
        if random_seed is None:
            raise "no random_seed given"

        problem_catalog = {
            'multiplication': MultiplicationProblem,
            'addition': AdditionProblem,
            'subtraction': SubtractionProblem
            }
        return problem_catalog[type_of_prob].randomly_generate(random_seed)


class MultiplicationProblem(Problem):

    @classmethod
    def randomly_generate(cls, random_seed, integers_needed=2):
        _format_problem(cls, random_seed, operator='*', integers_needed=2,)


        return cls

class AdditionProblem(Problem):

    @classmethod
    def randomly_generate(cls, random_seed, integers_needed=2):
        _format_problem(cls, random_seed, operator='+', integers_needed=2,)


        return cls

class SubtractionProblem(Problem):

    @classmethod
    def randomly_generate(cls, random_seed):
        _format_problem(cls, random_seed, operator='-', integers_needed=2,)

        return cls


def _format_problem(cls, random_seed, operator, integers_needed, ):
    int_1, int_2 = _get_integers_from_cache(random_seed, integers_needed)
    cls.string = '{}{}{}'.format(int_1, operator, int_2)
    cls.answer = eval(cls.string)
    cls.next_index = random_seed + integers_needed


def _get_integers_from_cache(random_seed, integers_needed):
    random_bank = random_list_of_integers()

    if random_seed >= len(random_bank) - integers_needed:
        random_seed = 0
    integers = (random_bank[random_seed+i] for i in range(integers_needed))

    return integers

    #need several different types of problems:
    #       mult, div, add, sub, algebra,
