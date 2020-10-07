import re
import json

from learncentive.tests.test_client import client
from learncentive.problem_generation.problem_set import ProblemSet

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
    user_results = {
        'grades': [.92, .5],
        'graded': False,
        'problems': [
            {'question': '', 'answer':'', 'difficulty': 0, 'correct':True},
            {'question': '', 'answer':'', 'difficulty': 0, 'correct':False},
            {'question': '', 'answer':'', 'difficulty': 1, 'correct':False}
            ],
        }
    #first iteration
    json_data = json.dumps(user_results)
    api_response = client.get('/api/problem_set_generator/{}'.format(json_data))
    assert api_response.status == '200 OK'
    # #second iteration
    json_data_2 = api_response.get_json()
    api_response_2 = client.get('/api/problem_set_generator/{}'.format(json_data_2))
    assert api_response_2.status == '200 OK'
