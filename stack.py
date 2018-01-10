"""
Stack Implementation.
"""


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        self.items == []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


a = Stack()
print(a.is_empty())
a.push('felix')
a.push('stephen')
a.push(3)
a.pop()
a.size()
