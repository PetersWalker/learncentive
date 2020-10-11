import json

from learncentive.problem_generation.problem_set import ProblemSet

user_results = {
    'grades': [.92, .5],
    'graded': False,
    'problems': [
        {'question': '', 'answer': '', 'difficulty': 0, 'correct': True},
        {'question': '', 'answer': '', 'difficulty': 0, 'correct': True},
        {'question': '', 'answer': '', 'difficulty': 1, 'correct': True},
        {'question': '', 'answer': '', 'difficulty': 2, 'correct': False}
        ],
    }
'''need to run on multiple edge cases:
    grades are preserved from previous difficulties
    grades are rounded up to hundreth place'''

def test_new_problem_set_from_old_problem_set():
    old_set = ProblemSet(user_results)
    new_set = old_set.new_problem_set()
    assert isinstance(new_set, ProblemSet)
    assert new_set.grades == [.96, .75, 0]
    assert len(new_set.problems) == 10
    assert isinstance(vars(new_set), dict)

def test_problem_set_from_grades():
    grades = [.94, .5]
    set_from_grades = ProblemSet.from_grades(grades)
    assert isinstance(set_from_grades, ProblemSet)

def test_problem_set_generates_1001_problem_set_alacart():
     test_set = ProblemSet.alacarte(amount_of_probs=2000, type_of_prob=0)
     assert len(test_set.problems) == 2000

def test_problem_set_is_json_serializable():
    new_set = ProblemSet(user_results).new_problem_set()
    json_data = json.dumps(vars(new_set))
    assert isinstance(json_data, str)

# def test_problem_set_from_data_base_grades():
#     new_set = ProblemSet.from_grades()
#     assert isinstance(new_set, ProblemSet)
