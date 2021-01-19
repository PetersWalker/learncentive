import json

def assert_correct_problem_set_schema(response):
    data = json.loads(response.data)
    assert 'course_id' in data
    assert 'grades' in data
    assert 'graded' in data
    assert 'problems' in data

    assert all(x in data['problems'][0] for x in ['question', 'answer', 'difficulty', 'correct']), '{} doesnt match'.format(data['problems'])
    assert isinstance(data, dict)
    assert isinstance(data['grades'], list), '{} is not a list'.format(data['grades'])
    assert isinstance(data['problems'], list), '{} is not a list'.format(data['problems'])



"""
API response is

user_results = {
        'course_id': UUID
        'grades': [.92, .5],
        'graded': False,
        'problems': [
            {'question': '', 'answer':'', 'difficulty': 0, 'correct':True},
            {'question': '', 'answer':'', 'difficulty': 0, 'correct':False},
            {'question': '', 'answer':'', 'difficulty': 1, 'correct':False}
            ],
        }
"""