import unittest
from random import randint
import re

from learncentive.tests.test_client import client
from learncentive.src.problem import generate, Problem, _get_integers_from_cache

# DELETE import and first test when second test is successful
from learncentive.resource.problem_set import generate_problem_handle_index


def test_cache_index_not_out_of_range_with_seed():
    prob = generate_problem_handle_index('multiplication')
    assert prob

def test_get_integers_from_cache():
    values = _get_integers_from_cache(2)
    assert len(values) == 2


def test_randomly_generate_multiplication_problem(client):
    test_problem = generate('multiplication')
    assert eval(test_problem.string) == int(test_problem.answer)


def test_randomly_generate_addition_problem(client):
    test_problem = generate('addition')
    assert eval(test_problem.string) == int(test_problem.answer)


def test_randomly_generate_subtraction_problem(client):
    test_problem = generate('subtraction')
    assert eval(test_problem.string) == int(test_problem.answer)


def test_randomly_generate_division_problem(client):
    # Due to floating point arithmetic, it's sufficient to check answer
    # within a hundreth
    test_problem = generate('division')
    exact_answer = eval(test_problem.string)
    assert (exact_answer - .01) < test_problem.answer < (exact_answer + .01)


def test_randomly_generate_composite_mult_add_problem(client):
    test_problem = generate('multiplication', 'addition')
    correct_format = re.match('[0-10]\*[0-10]\+[0-10]', test_problem.string)
    assert eval(test_problem.string) == int(test_problem.answer)
    assert correct_format
