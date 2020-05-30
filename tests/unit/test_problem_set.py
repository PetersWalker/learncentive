from learncentive.resource.problem_set import _try_generating_problem_with_random_seed
from learncentive.tests.test_client import client

def test_cache_index_not_out_of_range_with_seed():
    prob = _try_generating_problem_with_random_seed('multiplication', 1000)

    assert prob
