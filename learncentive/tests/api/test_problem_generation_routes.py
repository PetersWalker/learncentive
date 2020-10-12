import json
from learncentive.tests.assertions import assert_correct_problem_set_schema
from learncentive.tests.test_client import client


def test_problem_set_a_la_carte_returns_correct_schema(client):
    api_response = client.get('/problem_generation/5/2')
    assert_correct_problem_set_schema(api_response)


def test_problem_set_generator_returns_200_status(client):
    user_results = {
        'grades': [.92, .5],
        'graded': False,
        'problems': [
            {'question': '', 'answer': '', 'difficulty': 0, 'correct': True},
            {'question': '', 'answer': '', 'difficulty': 0, 'correct': False},
            {'question': '', 'answer': '', 'difficulty': 1, 'correct': False}
        ],
    }

    # first iteration
    json_request1 = json.dumps(user_results)  # py -> json string
    api_response1 = client.get('problem_generation/{}'.format(json_request1))  # json string -> response object
    assert api_response1.status == '200 OK'
    assert_correct_problem_set_schema(api_response1)

    # second iteration
    json_request2 = json.dumps(api_response1.json)  # response object -> jsonbytes -> string
    api_response2 = client.get('problem_generation/{}'.format(json_request2))
    assert api_response2.status == '200 OK'
    assert_correct_problem_set_schema(api_response2)

# def test_problem_set_request_with_no_url_data(client):
#     api_response = client.get('/api/problem_set_generator')
#     assert api_response.status == '200 OK'
#     assert_correct_problem_set_schema(api_response)
