import re
from learncentive.tests.test_client import client

def test_homepage_load(client):
    response = client.get('/')
    assert b'learncentive' in response.data


def test_problem_set_returns_5_problems_in_json_format(client):
    api_response_json = client.get('/api/problem_set/5/multiplication')
    assert api_response_json.is_json

    api_response_dict = api_response_json.get_json()
    assert len(api_response_dict) == 5

def test_problem_set_size_up_to_1000(client):
    # available random bank is only 1000 integers
    maximum = 1000
    api_response_json = client.get(
        '/api/problem_set/{}/multiplication'.format(maximum)
    )
    api_response_dict = api_response_json.get_json()

    assert  len(api_response_dict) == maximum
