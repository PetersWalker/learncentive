from learncentive.src.cache import random_list_of_integers
from learncentive.tests.test_client import client

random_bank = random_list_of_integers()

def test_access_values(client):
    assert len(random_bank) == 1000, 'cant access cache'
