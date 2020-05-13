from random import randint
import operator as op

from learncentive.src.cache import create_cached_random_bank


class Problem():
#Base class for arithmetic problems

    dunder = {'+':op.__add__, 'x':op.__mul__}

    def __init__(self, string='', answer=0):
        self.string = string
        self.answer = answer

    def __repr__(self):
        return self.string

    @classmethod
    def randomly_generate(cls, seed=randint(0, 900)):
        random_bank = create_cached_random_bank()

        int_1 = random_bank[seed]
        int_2 = random_bank[seed+1]

        cls.string = '{}*{}'.format(int_1, int_2)
        cls.answer = '{}'.format(int_1*int_2)
        return cls
