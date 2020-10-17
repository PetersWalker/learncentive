from learncentive.tests.fixtures import client
from learncentive.admin.configure import admin

def test_admin_page(client):
    response = client.get('/admin')
    assert response.status == '200 OK'

