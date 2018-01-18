"""
Linked List Implementation.
"""

class Node:
    
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self, ):
        return self.data

    def get_next(self, ):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    
    def __init__(self, ):
        self.head = None

    def is_empty(self, ):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self, ):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found



mylist = UnorderedList()
mylist.add(10)

"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, ):
        self.head = None


if __name__ == '__main__':
    l = LinkedList()
    l.head = Node(1)
    l1 = Node(2)
    l2 = Node(3)

"""
