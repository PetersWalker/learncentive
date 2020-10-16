from learncentive.tests.fixtures import client
from learncentive.users.models import User

def test_register_new_user(client):
    route = 'users/register'
    form_data = {
        'name': 'pete',
        'email': 'peter@learncentive.com',
        'password': 'testpass',
        'confirm': 'testpass'
    }

    response = client.post(route, data=form_data)
    assert response.status == '201 CREATED'

    db_user = User.query.filter_by(name='pete').first()
    assert db_user.email == 'peter@learncentive.com'
    assert db_user.password == 'testpass'
    assert db_user.grades == [0]

def test_already_registerd(client):
    route = 'users/register'
    form_data = {
        'name': 'pete',
        'email': 'peter@learncentive.com',
        'password': 'testpass',
        'confirm': 'testpass'

    }

    client.post(route, data=form_data)
    response = client.post(route, data=form_data)
    assert response.status == '409 CONFLICT'

def test_invalid(client):
    route = 'users/register'
    form_data = {
        'name': 'peter',
        'email': 'peter@learncentive.com',
        'password': 'testpass',
        'confirm': 'testfail'
    }
    response = client.post(route, data=form_data)
    assert response.status == '400 BAD REQUEST'


