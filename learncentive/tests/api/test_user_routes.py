from learncentive.tests.fixtures import client
from learncentive.users.models import User

def test_register_new_user(client):
    route = '/register'
    form_data = {
        'name': 'pete',
        'email': 'peter@learncentive.com',
        'password': 'testpass',
    }

    response = client.post(route, data=form_data)
    assert response.status == '201 CREATED'

    db_user = User.query.filter_by(name='pete').first()
    assert db_user.email == 'peter@learncentive.com'
    assert db_user.password == 'testpass'

