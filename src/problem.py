from random import randint
from itertools import zip_longest

from learncentive.src.cache import random_list_of_integers
from learncentive.src.cache_config import cache_index



# TODO
# remove random seed from this level of abstraction

def generate(*type_of_prob):
    if type_of_prob is None:
        raise "learncentive: No Problem Type Specified"
    if len(type_of_prob) == 1:
        problem = problem_catalog[type_of_prob[0]]()
    else:
        problem = problem_catalog['composite'](*type_of_prob)
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
            integers.append(str(random_bank[cache_index.current_value+i]))
        except IndexError:
            cache_index.reset()
            integers.append(str(random_bank[cache_index.current_value+i]))
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

    def __init__(self, *type_of_prob):
        vals_needed = 0
        operators = []
        self.string = ''

        for prob in type_of_prob:
            temp_prob = problem_catalog[prob]
            vals_needed += (temp_prob.vals_needed)
            operators.append(temp_prob.operator)

        ints = _get_integers_from_cache(vals_needed)

        string = zip_longest(ints, operators, fillvalue='')
        for tup in string:
            self.string += tup[0] + tup[1]

        self.answer = eval(self.string)

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
# operators = [*, ln]
# vals_needed = 2
# string_pattern '{}{}{}{}{}{}{}{}{}'

# needed
# operators = [*, ln]
# vals_needed = 2
# string_pattern '{}{}{}{}{}{}{}{}{}'

problem_catalog = {
    'multiplication': MultiplicationProblem,
    'addition': AdditionProblem,
    'subtraction': SubtractionProblem,
    'division': DivisionProblem,
    'composite': CompositeProblem
    }
