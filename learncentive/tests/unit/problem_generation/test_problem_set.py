import json

from learncentive.problem_generation.problem_set import ProblemSet

user_results = {'quantity': {0: 2, 1: 1},
                'correct': {0: 2, 1: 1},
                'grades': {0: .92, 1: .5},
                'graded': False,
                'problems': [
                    {'question': '', 'answer': '', 'difficulty': 0, 'result': True},
                    {'question': '', 'answer': '', 'difficulty': 0, 'result': False},
                    {'question': '', 'answer': '', 'difficulty': 1, 'result': False}
                    ],
                }
'''need to run on multiple edge cases:
    grades are preserved from previous difficulties
    grades are rounded up to hundreth place'''

def test_new_problem_set_from_old_problem_set():
    old_set = ProblemSet(user_results)
    new_set = old_set.new_problem_set()
    assert isinstance(new_set, ProblemSet)
    assert new_set.quantity == {1: 8, 2: 2}
    assert new_set.correct == {1: 0, 2: 0}
    assert new_set.grades == {0: .96, 1: .75}
    assert new_set.graded == False
    assert len(new_set.problems) == 10

def test_problem_set_from_grades():
    grades = {0: .94, 1: .5}
    set_from_grades = ProblemSet.from_grades(grades)
    assert isinstance(set_from_grades, ProblemSet)

def test_problem_set_generates_1001_problem_set_alacart():
     test_set = ProblemSet.alacarte(amount_of_probs=1001, type_of_prob=0)
     assert len(test_set.problems) == 1001
     assert test_set.quantity == {0:1001}

def test_problem_set_is_json_serializable():
    new_set = ProblemSet(user_results).new_problem_set()
    try:
        json_data = new_set.to_json()
        assert True
    except:
        assert False
    assert ProblemSet.from_json(json_data).graded == False

def test_keys_in_json_response_are_converted_back_to_ints_from_str():
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
