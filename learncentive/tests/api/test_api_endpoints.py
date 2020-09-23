import re
import json

from learncentive.tests.test_client import client
from learncentive.problem_generation.problem_set import ProblemSet

def test_homepage_load(client):
    response = client.get('/')
    assert b'learncentive' in response.data

def test_problem_set_alacarte_returns_problems_in_json_format(client):
    api_response_json = client.get('/api/problem_set_generator/5/2')
    assert api_response_json.is_json

def test_problem_set_alacarte_size_response_up_to_2000(client):
    max_tested = 2000
    api_response = client.get(
        '/api/problem_set_generator/{}/3'.format(max_tested))
    problem_set = ProblemSet(json.loads(api_response.get_json()))
    assert  len(problem_set.problems) == max_tested

def test_problem_set_generator_returns_200_status(client):
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
#     json_data = json.dumps(user_results)
#     api_response = client.get('/api/problem_set_generator/{}'.format(json_data))
#     assert api_response.status == '200 OK'
#     #assert len(api_response == 5)
