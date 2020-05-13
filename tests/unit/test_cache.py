from learncentive.src.cache import create_cached_random_bank
from learncentive.tests.test_client import client

random_bank = create_cached_random_bank()

def test_access_values(client):
    assert len(random_bank) == 1000, 'cant access cache'
