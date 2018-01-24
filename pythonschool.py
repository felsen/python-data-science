"""
Ref: https://pythonschool.net/data-structures-algorithms/algorithms-and-data-structures/

Algorithm's and Data Structure's:
---------------------------------

Algorithm's:
------------

1) Linear Search
2) Binary Search
3) Bubble Sort
4) Insertion Sort
5) Quick Sort

Data Structure's:
-----------------

1) Stack
2) Queue
3) Linked List
4) Binary Tree

===================================

Linear Search or Sequential Search:
-----------------------------------

Finding the element from the list, traveling from start to end of the list.
At any point of time if the element is found from the list, then the search will be stopped.
Always this will start from the position 0.

Example: linear_search() function.

Binary Search:
--------------
Finding the midpoint of the list, then spliting into two list.
then travelling from start to end in each list.

Example: binary_search(), binary_search_1() function.

Bubble Sort:
------------
There are many ways to do Bubble sort; This is one of the efficient way to sort list.
comparing the first two elements and swaping those two elements and for other elements also.

Example: bubble_sort() function.

Insertion Sort:
---------------
Inserting the item one by one and comparing with the other elements.

Example: insertion_sort() function.

Stack:
------
FILO - First In Last Out
Stack will store all the items one by one, when it's takes out the last item will taken first.

Example: Stack class.

Queue:
------
FIFO - First In First Out
Queue will store all the items one by one, first entered item will always taken first out.

Example: Queue class

Linked List:
------------
Each item will be considered as a Node; Every node will be connected with next node using pointers.

There are three types of linked list,
   1) Singly Linked List
   2) Doubly Linked List
   3) Circular Linked List

Reference: 
   http://stackabuse.com/python-linked-lists/
   https://dbader.org/blog/python-linked-list
   https://www.pythoncentral.io/singly-linked-list-insert-node/

Example: Node class


"""


def linear_search(search_list, search_item):
    position, found = 0, False
    while position < len(search_list) and not found:
        if search_list[position] == search_item:
            found = True
        position += 1
    return (found, search_item, position, search_list)

# print(linear_search([23, 56, 2, 9, 5, 7, 78, 45], 5))


def binary_search(search_list, search_item):
    first, last, found = 0, len(search_list)-1, False
    while first <= last and not found:
        midpoint = (first + last) // 2  # Python3.6
        if search_list[midpoint] == search_item:
            found = True
        else:
            if search_item < search_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return (found, search_item, search_list)

# print(binary_search([2, 3, 4, 5, 6, 7, 8, 9, 10], 7))


def binary_search_1(search_list, search_item):
    midpoint = len(search_list) // 2  # Python3.6
    if search_list[:midpoint][-1] >= search_item:
        return linear_search(search_list[:midpoint], search_item)
    elif search_list[midpoint:][-1] >= search_item:
        return linear_search(search_list[midpoint:], search_item)

# print(binary_search_1([2, 3, 4, 5, 6, 7, 8, 9, 10], 7))


def bubble_sort(sort_list):
    for i in range(len(sort_list)):
        for j in range(i):
            if sort_list[j] > sort_list[j+1]:
                temp = sort_list[j]
                sort_list[j] = sort_list[j+1]
                sort_list[j+1] = temp
    return sort_list

# print(bubble_sort([1,85,4,3,2,5,6,7]))


def insertion_sort(sort_list):
    for i in sort_list:
        ind = sort_list.index(i)
        while (ind > 0):
            if sort_list[ind-1] > sort_list[ind]:
                sort_list[ind-1], sort_list[ind] = sort_list[ind], sort_list[ind-1]
            else:
                break
            ind = ind - 1
    return sort_list

# print(insertion_sort([1, 5, 4, 3, 2, 6, 7, 8]))
# print(insertion_sort([16, 19, 11, 15, 10, 12, 14]))


class Stack:
    
    """
    Simple stack implementation.
    """

    def __init__(self):
        self.stack_data = []

    def is_empty(self):
        return self.stack_data == []

    def push(self, item):
        self.stack_data.append(item) # Each item will be added in the stack.

    def pop(self):
        self.stack_data.pop() # Item will be removed which is added recently.

    def peek(self):
        return self.stack_data[len(self.stack_data)-1] # This will show, the item which is going to remove.

    def size(self):
        return len(self.stack_data) # Total size of the stack

# sd = Stack()
# sd.push("felix")
# sd.push("stephen")
# sd.push("steve")
# sd.push("felsen")
# print(sd.stack_data)
# sd.pop()
# print(sd.peek())
# sd.pop()
# print(sd.peek())


class Queue:

    """
    Simple Queue Implementation.
    """

    def __init__(self):
        self.queue_data = []

    def is_empty(self):
        return self.queue_data == []

    def push(self, item):
        self.queue_data.append(item) # All the items will be added in the queue.

    def pop(self):
        self.queue_data.pop(0) # Item will be removed 

    def size(self):
        return len(self.queue_data)

    def peek(self):
        return self.queue_data[0]

# qd = Queue()
# qd.push("felix")
# qd.push("stephen")
# qd.push("steve")
# qd.push("felsen")
# print(qd.queue_data)
# qd.pop()
# print(qd.peek())
# qd.pop()
# print(qd.peek())


class Node:
    
    """
    Node Implementation for Linked List.
    """

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def has_data(self):
        found = False
        if data is not None:
            found = True
        return found

