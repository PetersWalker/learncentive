import json

from learncentive.tests.test_client import client
from learncentive.problem_generation.problem_set import ProblemSet

user_results = {'quantity':{0:2, 1:1},
                'correct': {0:1, 1:0},
                'grades': {0:.92, 1:.5},
                'graded': False,
                'problems': [
                    {'question': '', 'answer':'', 'difficulty': 0, 'result':True},
                    {'question': '', 'answer':'', 'difficulty': 0, 'result':False},
                    {'question': '', 'answer':'', 'difficulty': 1, 'result':False}
                    ],
                }
'''need to run on multiple edge cases:
    grades are preserved from previous difficulties
    grades are rounded up to hundreth place'''

def test_grade(client):
    test_set = ProblemSet(user_results)

    assert test_set.graded == False

    test_set.grade()

    assert test_set.grades == {0:.71, 1:.25}
    assert test_set.graded == True

def test_new_problem_set(client):
    old_set = ProblemSet(user_results)
    new_set = old_set.new_problem_set()

    assert type(new_set) == ProblemSet

def test_problem_set_is_json_serializable_with_no_newline_chars(client):
    new_set = ProblemSet(user_results).new_problem_set()
    try:
        json_data = new_set.to_json()
        assert True
    except:
        assert False


    assert ProblemSet.from_json(json_data).graded == False

def test_keys_in_json_response_are_converted_back_to_ints_from_str(client):
    '''This test was created from trouble decoding json back to
    the ProblemSet object. the ProblemSet object schema has
    integers as keys for some of its fields. JSON doesn't allow
    integers to be keys causing KeyErrors and TypeErrors when
    using dicts and manipulating the keys.

    solutions: post processing after deserialization (maybe expensive?)
               object_hook maybe?
               custom json decodeer?
    '''
    json_data = json.dumps(user_results)
    test_set = ProblemSet.from_json(json_data)
    for i in test_set.quantity.keys(): assert type(i) == int
    for i in test_set.correct.keys(): assert type(i) == int
    for i in test_set.grades.keys(): assert type(i) == int


def test_generate_next_set_from_graded_set(client):
    test_set = ProblemSet(user_results)
    new_set = test_set.new_problem_set()
    assert new_set
