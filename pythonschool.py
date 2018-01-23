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

Example: binary_search() function.

"""


def linear_search(search_list, search_item):
    position, found = 0, False
    while position < len(search_list) and not found:
        if search_list[position] == search_item:
            found = True
        position += 1
    return (found, search_item, position, search_list)

print(linear_search([23, 56, 2, 9, 5, 7, 78, 45], 5))


def binary_search(search_list, search_item):
    midpoint = len(search_list) // 2  # Python3.6
    if search_list[:midpoint][-1] > search_item:
        return linear_search(search_list[:midpoint], search_item)
    else:
        return linear_search(search_list[midpoint:], search_item)

print(binary_search([2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
