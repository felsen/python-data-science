"""
Queue Implemention.
"""

class Queue:

    def __init__(self,):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self,):
        self.queue.pop()

    def size(self,):
        return len(self.queue)

q = Queue()
q.enqueue("hello")
q.enqueue("yes")
q.enqueue(3)
q.dequeue()
print(q.size())
