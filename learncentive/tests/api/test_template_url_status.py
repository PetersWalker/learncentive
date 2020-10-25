from learncentive.tests.fixtures import client

template_urls = [
    '',
    '/catalog',
    '/users/account',
    '/classroom',
    '/admin'
]


def test_status_of_template_routes(client):
    for url in template_urls:
        status = client.get(url).status
        assert (status == '200 OK') or (status == '308 PERMANENT REDIRECT'), \
            'check the templating imports {} returned {}'.format(url, status)
