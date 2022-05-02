from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: np.object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < 0 or i > self.n:
            raise IndexError()
        if i < self.n / 2:
            p = self.dummy.next
            k = 0
            while k < i:
                p = p.next
                k += 1
        else:
            p = self.dummy
            k = self.n
            while k > i:
                p = p.prev
                k -= 1
        return p

    def get(self, i) -> np.object:
        if i < 0 or i >= self.n:
            raise IndexError
        return self.get_node(i).x

    def set(self, i: int, x: np.object) -> np.object:
        if i < 0 or i > self.n:
            raise IndexError
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w: Node, x: np.object) -> Node:
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        if self.n == 1:
            self.dummy.next = u
            self.dummy.prev = u
        return u

    def add(self, i: int, x: np.object):
        if i < 0 or i > self.n:
            raise IndexError()
        return self.add_before(self.get_node(i), x)

    def _remove(self, w: Node):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        if self.n == 0:
            self.dummy.next = self.dummy
            self.dummy.prev = self.dummy
        return w.x

    def remove(self, i: int):
        if i < 0 or i >= self.n:
            raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: np.object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        if self.n <= 0:
            return True
        nodeEnd = self.dummy.prev
        nodeStart = self.dummy.next
        for i in range(self.n // 2):
            if nodeEnd.x != nodeStart.x:
                return False
            else:
                nodeEnd = nodeEnd.prev
                nodeStart = nodeStart.next
        return True

    def reverse(self):
        head = self.dummy.next
        tail = self.dummy.prev
        previous = self.dummy
        current = self.dummy.next
        curr_nxt = current.next

        while current is not self.dummy:
            current.next = previous
            current.prev = curr_nxt

            previous = current
            current = curr_nxt
            curr_nxt = curr_nxt.next

        self.dummy.next = tail
        self.dummy.prev = head

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
