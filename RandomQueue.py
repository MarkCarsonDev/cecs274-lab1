import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> np.object:
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        if self.n == 0:
            raise IndexError()
        i = random.randint(0, self.n - 1)
        self.a[self.j % len(self.a)], self.a[(self.j + i) % len(self.a)] = \
            self.a[(self.j + i) % len(self.a)], self.a[self.j % len(self.a)]
        return super().remove()
