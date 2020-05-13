"""This module contains and evaluates a function which caches a list
of random numbers. These random numbers are used in the creation of
randomly-generated problems. using this pre-calculated bank of random numbers
saves comptation time upfront"""

from random import randint

from flask_caching import Cache

#cache object instance
cache = Cache()

#pre-generated random numbers for seeding problems
@cache.cached(key_prefix='random_bank', timeout=2)
def create_cached_random_bank():
    random_bank = [randint(1, 10) for x in range(1000)]
    return random_bank
