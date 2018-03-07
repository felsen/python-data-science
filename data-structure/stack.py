"""
Stack Implementation.
"""
__author__ = "Felix Stephen"



class Stack(object):
    """
    Simple Stack implementation.
    """
    def __init__(self, limit=10):
	"""
	Initiating the stack and limit if the of the pushing item to the stack.
	"""
        self.stack = []
        self.limit = limit
    
    def __str__(self):
	"""
	To understand the stack elements.
	"""
	return str(self.stack)
    
    def is_bool(self):
	"""
	checking if the stack has element or not
	"""
        return not(bool(self.stack))
        
    def is_empty(self):
	"""
	checking the stack is empty or not.
	"""
        return not(bool(self.stack))

    def size(self):
	"""
	total size of the stack.
	"""
        return len(self.stack)

    def push(self, item):
	"""
	Appending the every item to the stack.
	"""
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(item)
    
    def pop(self):
	"""
	pop will remove the item from the last item of the stack.
	"""
        if self.stack:
            self.stack.pop()
        else:
            raise IndexError("pop from an empty stack..!")
    
    def peek(self):
	"""
	finding the next poping item from the stack
	"""
        return self.stack[-1]



class StackOverflowError(BaseException):
    pass



if __name__ == '__main__':
    limit = 13
    stack = Stack(limit=limit)
    for i in range(limit):
        stack.push(i)

    print(stack.is_empty())
    print(stack.size())
    print(stack.__str__())
