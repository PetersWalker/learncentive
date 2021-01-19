from learncentive.tests.fixtures import client

'''These tests are for non logged in user'''

template_urls = {
    '/': '200 OK',
    '/catalog': '200 OK',
    '/users/account': '401 UNAUTHORIZED',
    '/classroom': '401 UNAUTHORIZED',
}


def test_status_of_template_routes(client):
    for url, status in template_urls.items():
        result = client.get(url).status
        assert result == status, "'{}' returned {} vice {}".format(url, result, status)
