from random import randint

import operator as op

#Base class for randomly generated arithmetic problems
class Problem(object):
    
    dunder = {'+':op.__add__, 'x':op.__mul__}

    def __init__(self, string='', answer=0):
        self.string = string
        self.answer = answer
        pass

    def __repr__(self):
        return 'Problem: {}'.format(self.string)

    @classmethod
    def random(cls, seed=randint(0,10)):
        cls.string = '{}{}{}={}'.format(1,2,3,4)

        pass
