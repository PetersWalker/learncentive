import unittest
from random import randint

from learncentive.tests.test_client import client
from learncentive.src.problem import Problem



def test_init_Problem(client):
    test_problem = Problem(string='1 + 4', answer=5)

    assert (test_problem.answer == 5)
    assert (test_problem.string == '1 + 4')
    assert (repr(test_problem) == test_problem.string)

def test_randomly_generate_multiplication_problem(client):
    test_problem, _ = Problem.generate('multiplication', 999)

    assert eval(test_problem.string) == int(test_problem.answer)

def test_randomly_generate_addition_problem(client):
    test_problem, _ = Problem.generate('addition')

    assert eval(test_problem.string) == int(test_problem.answer)

def test_randomly_generate_subtraction_problem(client):
    test_problem, _ = Problem.generate('subtraction')

    assert test_problem
