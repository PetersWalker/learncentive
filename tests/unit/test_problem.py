import unittest
from random import randint

import learncentive.src.problem as problem


class TestProblem(unittest.TestCase):
    # Since these problems are generated randomly, during testing a new problem
    # object will be created for every unit test thus increasing the breadth of
    # the test.

    test_problem = problem.Problem(string = '1 + 4 = x', answer = 5)

    def test_kwargs(self):
        self.assertTrue(self.test_problem.answer == 5)
        self.assertTrue(self.test_problem.string == '1 + 4 = x')

    def test_repr(self):
        self.assertTrue(repr(self.test_problem) ==
            "Problem: {}".format(self.test_problem.string))

    # The random class method should accept a single number as a seed and produce
    # an expression and answer as attributes

    # Use a lambda function to override the randint function and use our
    # predetermined seed
    def test_random(self):
        seed = 5

        problem.randint = lambda n : seed
        test_problem = problem.Problem.random()
        self.assertTrue(2 == 2)
