"""
Stack Implementation.
"""

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
print(a.size())
"""


class Stack:
    
    def __init__(self, ):
        self.items = []

    def is_empty(self, ):
        return self.items == []

    def push(self, value):
        self.items.insert(0, value)

    def pop(self, ):
        self.items.pop(0)

    def peek(self, ):
        return self.items[0]

    def size(self, ):
        return len(self.items)

s = Stack()
s.push('x')
s.push('y')
s.pop()
print(s.peek())




