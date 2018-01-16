"""
Dequeue Implementation.
"""

class Dequeue:

    def __init__(self, ):
        self.dequeue = []

    def is_empty(self, ):
        return self.dequeue == []

    def add_rear(self, item):
        self.dequeue.insert(0, item)

    def add_front(self, item):
        self.dequeue.append(item)

    def remove_rear(self,):
        self.dequeue.pop(0)

    def remove_front(self,):
        self.dequeue.pop()
        # self.dequeue.pop(-1)

    def size(self, ):
        return len(self.dequeue)



d = Dequeue()
d.add_rear(4)
d.add_rear('dog')
d.add_front('cat')
d.add_front(True)
d.size()
d.is_empty()
d.add_rear(8.4)
d.remove_rear()
d.remove_front()


