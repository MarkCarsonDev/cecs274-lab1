from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()

    def add(self, x: object):
        super().add(x)
        replaced = False

        if self.max_deque.n == 0 or x > self.max_deque.get(0):
            del self.max_deque
            self.max_deque = DLLDeque()
            head = self.max_deque.add(0, x)
            replaced = True
        else:
            for i in range(1, self.max_deque.n):
                if x > self.max_deque.get(i):
                    self.max_deque.set(i, x)

                    for k in range(i+1, self.max_deque.n):
                        self.max_deque.remove_last()
                    replaced = True
                    break
        if not replaced:
            self.max_deque.add_last(x)
    """
    adds an element to the end of this max queue
    INPUT: x the element to add
    """

    def remove(self) -> object:
        temp = super().remove()
        for i in range(0, self.max_deque.n):
            if temp == self.max_deque.get(i):
                self.max_deque.remove(i)
                break
        return temp


    def max(self):
        return self.max_deque.get(0)




# # TESTER
# mq = MaxQueue()
# mq.add(3)
# print("Added:", 3)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
# mq.add(2)
# print("Added:", 2)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
# mq.add(1)
# print("Added:", 1)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
# mq.add(4)
# print("Added:", 4)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
# r = mq.remove()
# print("Removed element:", r)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
# r = mq.remove()
# print("Removed element:", r)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
# r = mq.remove()
# print("Removed element:", r)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
# mq.add(8)
# print("Added:", 8)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
# mq.add(3)
# print("Added:", 3)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
# mq.add(5)
# print("Added:", 5)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
# mq.add(4)
# print("Added:", 4)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
# mq.add(1)
# print("Added:", 1)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
# mq.add(6)
# print("Added:", 6)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")
#
#
# while mq.size() > 0:
#     r = mq.remove()
#     print("Removed element:", r)
#     print("MaxQueue contents:", mq)
#     print("Max Dequeu contents", mq.max_deque)
#     if mq.size() > 0:
#         print("Max element", mq.max(), "\n\n")
#
