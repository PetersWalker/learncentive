from itertools import zip_longest

from learncentive.blueprints.problem_generation.cache import random_list_of_integers
from learncentive.blueprints.problem_generation import config

index = config.cache_index

def generate_problem(*type_of_prob):
    if type_of_prob is None:
        raise Exception("learncentive: No Problem Type Specified")
    elif len(type_of_prob) == 1:
        only_type, = type_of_prob
        problem = problem_catalog[only_type]()
    else: #compositeproblem
        problem = CompositeProblem(*type_of_prob)

    return problem

class Problem():

    def __init__(self):
        val_1, val_2 = _get_integers_from_cache(self.vals_needed)
        self.question = self.string_pattern.format(val_1, self.operator, val_2)
        self.answer = eval(self.question)

    def __repr__(self):
        return self.question

def _get_integers_from_cache(values_needed, cache_index=index):
    random_bank = random_list_of_integers()
    integers = [
        str(random_bank[(cache_index.current_value + i) % len(random_bank)]) 
        for i in range(values_needed)
        ]

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

class CompositeProblem(Problem):
# not appropriate as separate class, needs to be a subset of generate funtion or
# class "Problem"'s init method
    def __init__(self, *type_of_prob):
        vals_needed = 0
        operators = []
        self.question = ''

        for prob in type_of_prob:
            temp_prob = problem_catalog[prob]
            vals_needed += (temp_prob.vals_needed)
            operators.append(temp_prob.operator)

        ints = _get_integers_from_cache(vals_needed-len(operators)+1)
        string = zip_longest(ints, operators, fillvalue='')

        for tup in string:
            self.question += tup[0] + tup[1]

        self.answer = eval(self.question)

# #mul div add
# operator = '*'
# vals_needed = 2
# string_pattern = '{}{}{}'
#
# now
# operators = [*, /, +]
# vals_needed = 6
# string_pattern '{}{}{}{}{}{}{}{}{}' 9

# needed
# operators = [*, /, +]
# vals_needed = 4
# string_pattern '{}{}{}{}{}{}{}' 7
# string = '1*2/4+8'

# now
# operators = [*, ln, /, +]
# vals_needed = 7

# needed
# operators = [*, ln, /, +]
# vals_needed = 4

#vals needed is sum of vals needed - len(operators) +1

problem_catalog = {
    0: AdditionProblem,
    1: SubtractionProblem,
    2: MultiplicationProblem,
    3: DivisionProblem,
    }
