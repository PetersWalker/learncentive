from random import randint

class CacheIndex():

    def __init__(self):
        self.current_value = randint(0,1001)

    def set_to(self, new_index):
        self.current_value = new_index

    def reset(self):
        self.set_to(randint(0,1001))

cache_index = CacheIndex()
