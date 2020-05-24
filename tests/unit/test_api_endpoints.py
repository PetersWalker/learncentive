import re
from learncentive.tests.test_client import client

def test_homepage_load(client):
    response = client.get('/')
    assert b'learncentive' in response.data

def test_problem_set_returns_valid_arithmetic_expression(client):
    """ test api get response. should get a response of the form {3x5', '15'} """
    api_response_dict = client.get('/api/problem_set/5').get_json()
    problem_regex = '[0-9]*[0-9]'

    for problem in api_response_dict:
        assert re.search(problem_regex, problem), '{} != {}'.format(problem_regex, problem)


def test_problem_set_returns_5_problems(client):
    api_response_dict = client.get('/api/problem_set/5').get_json()
    assert len(api_response_dict) == 5

def test_response_is_in_json_format(client):
    api_response_dict = client.get('/api/problem_set/5')
    assert api_response_dict.is_json()
