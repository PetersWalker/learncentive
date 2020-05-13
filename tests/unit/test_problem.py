import unittest

from learncentive.src.problem import Problem


class TestProblem(unittest.TestCase):
    # Since these problems are generated randomly, during testing a new problem
    # object will be created for every unit test thus increasing the breadth of
    # the testing.


    def test_init_Problem(self):
        test_problem = Problem(string='1 + 4', answer=5)

        self.assertTrue(test_problem.answer == 5)
        self.assertTrue(test_problem.string == '1 + 4')
        self.assertTrue(repr(test_problem) == test_problem.string)

    def test_randomly_generate(self):
        # The random class method should accept a single number as a seed and produce
        # an expression and answer as attributes.
        # Use a lambda function to override the randint function in the
        # Problem module and use our predetermined seed of 5.

        test_problem = Problem.randomly_generate()
        assert eval(test_problem.string) == int(test_problem.answer)
