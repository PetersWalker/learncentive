from learncentive.problem_generation.problem_set import ProblemSet

from learncentive.tests.test_client import client

user_results = {'meta': {'quantity':{0:2, 1:1}},
                'problems': {
                    0:{'question': '', 'answer':'', 'difficulty': 0, 'result':True},
                    1:{'question': '', 'answer':'', 'difficulty': 0, 'result':False},
                    2:{'question': '', 'answer':'', 'difficulty': 1, 'result':False}
                    }
                }

def test_grade(client):
    test_set = ProblemSet(user_results)
    assert test_set.graded == False
    test_set.grade()
    assert test_set.grades == {0:.5, 1:0}
    assert test_set.graded == True

# def test_generate_next_set_from_graded_set(client):
#     test_set = ProblemSet(user_results)
#     test_set.grade()
#     new_set = test_set.new()
#     assert new_set
