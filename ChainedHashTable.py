from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):
    class Node():
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList):
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=np.object)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def _hash(self, key: int) -> int:
        return self.z * hash(key) % (2 ** self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n

    def find(self, key: object) -> object:
        h = self._hash(key)
        for i in range(0, len(self.t[h])):
            if self.t[h][i].key == key:
                return self.t[h][i].value
        return None

    def add(self, key: object, value: object):
        if self.find(key) is not None:
            return False
        if self.n + 1 > len(self.t):
            self.resize()
        hash_value = self._hash(key)
        self.t[hash_value].append(self.Node(key, value))
        self.n = self.n + 1
        return True

    def remove(self, key: int) -> object:
        if self.find(key) == None:
            return None
        else:
            hash_value = self._hash(key)
            list = self.t[hash_value]
            temp = None
            for i in range(0, len(list)):
                if list[i].key == key:
                    self.n = self.n - 1
                    temp = list.remove(i)
            if len(self.t) > 3 * self.n:
                self.resize()
            return temp

    def resize(self):
        if self.n == len(self.t):
            self.d = self.d + 1
        else:
            self.d -= 1
        temp = self.alloc_table(2 ** self.d)
        for i in range(len(self.t)):
            for j in range(self.t[i].size()):
                u = self.t[i].get(j)
                temp[self._hash(u.key)].append(u)
        self.t = temp

    def __str__ (self):
        s = "\n"
        for i in range(len(self.t)):
            s += str(i) + " : "
            for j in range(len(self.t[i])):
                k = self.t[i].get(j)  # jth node at ith list
                s += "(" + str(k.key) + ", " + str(k.value) + "); "

            s += "\n"
        return s



    # def __str__(self):
    #     s = "["
    #     for i in range(len(self.t)):
    #         for j in range(len(self.t[i])):
    #             k = self.t[i][j]
    #             s += str(k.key)
    #             s += ":"
    #             s += str(k.value)
    #             s += ";"
    #     return s + "]"