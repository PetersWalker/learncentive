from random import randint
from learncentive.src.cache import random_list_of_integers
from learncentive.src.cache_config import cache_index

# TODO
# remove random seed from this level of abstraction

def generate(type_of_prob):
    if type_of_prob is None:
        raise "learncentive: No Problem Type Specified"

    problem = problem_catalog[type_of_prob]()

    return problem

class Problem():

    def __init__(self):
        val_1, val_2 = _get_integers_from_cache(self.vals_needed)
        self.string = self.string_pattern.format(val_1, self.operator, val_2)
        self.answer = eval(self.string)


def _get_integers_from_cache(values_needed):
    random_bank = random_list_of_integers()
    integers = []

    for i in range(values_needed):
        try:
            integers.append(random_bank[cache_index.current_value+i])
        except IndexError:
            cache_index.reset()
            integers.append(random_bank[cache_index.current_value+i])

    cache_index.set_to(cache_index.current_value + values_needed)

    return integers

class MultiplicationProblem(Problem):
    operator = '*'
    vals_needed = 2
    string_pattern = '{}{}{}'


class AdditionProblem(Problem):
    operator = '+'
    vals_needed = 2
    string_pattern = '{}{}{}'


class SubtractionProblem(Problem):
    operator = '-'
    vals_needed = 2
    string_pattern = '{}{}{}'


class DivisionProblem(Problem):
    operator = '/'
    vals_needed = 2
    string_pattern = '{}{}{}'


problem_catalog = {
    'multiplication': MultiplicationProblem,
    'addition': AdditionProblem,
    'subtraction': SubtractionProblem,
    'division': DivisionProblem
    }
