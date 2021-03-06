from learncentive.blueprints.problem_generation.problem import generate_problem, _get_integers_from_cache
from learncentive.tests.fixtures import client

def test_get_integers_from_cache_and_not_out_of_range():
    values = _get_integers_from_cache(2000)
    assert len(values) == 2000


def test_randomly_generate_multiplication_problem(client):
    test_problem = generate_problem(0)
    assert eval(test_problem.question) == int(test_problem.answer)


def test_randomly_generate_addition_problem(client):
    test_problem = generate_problem(1)
    assert eval(test_problem.question) == int(test_problem.answer)


def test_randomly_generate_subtraction_problem(client):
    test_problem = generate_problem(2)
    assert eval(test_problem.question) == int(test_problem.answer)


def test_randomly_generate_division_problem(client):
    # Due to floating point arithmetic, it's sufficient to check answer
    # within a hundreth
    test_problem = generate_problem(3)
    exact_answer = eval(test_problem.question)
    assert (exact_answer - .01) < test_problem.answer < (exact_answer + .01)
    # correct_format = re.match('\d\/\d', test_problem.question)
    # assert correct_format,'{} was the wrong format'.format(test_problem.question)


def test_randomly_generate_composite_mult_add_problem(client):
    test_problem = generate_problem(2, 0)
    assert eval(test_problem.question) == int(test_problem.answer)
    # correct_format = re.match('\d\*\d\+\d', test_problem.question)
    # assert correct_format,'{} was the wrong format'.format(test_problem.question)
