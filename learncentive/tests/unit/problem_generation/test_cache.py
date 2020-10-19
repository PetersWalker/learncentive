from learncentive.blueprints.problem_generation.cache import random_list_of_integers

random_bank = random_list_of_integers()

def test_access_values():
    assert len(random_bank) == 1000, 'cant access cache'
