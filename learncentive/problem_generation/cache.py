"""This module contains a function which caches a list
of random numbers. These random numbers are used in the creation of
randomly-generated problems. using this pre-calculated bank of random numbers
saves comptation time upfront"""

from random import randint

from flask_caching import Cache

cache = Cache()

@cache.cached(key_prefix='random_bank', timeout=3600)
def random_list_of_integers():
    random_bank = [randint(1, 10) for x in range(1000)]
    return random_bank

class CacheIndex():

    def __init__(self):
        self.current_value = randint(0,1001)

    def set_to(self, new_index):
        self.current_value = new_index

    def reset(self):
        self.set_to(randint(0,1001))
