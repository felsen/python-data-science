"""
Searching and Sorting.

1. Sequential's search(seq_search)
   Comparing the search item with the each element one by one incrementing the index of the list.
   If the list is too big then, divide by 2 then, let's check in the both the list by using midpoint.
"""


def seq_search_1(search_lst, search_item):
    found, element = False, 0
    if not found:
        for i in search_lst:
            if search_item == search_lst[element]:
                found = True
                break
            else:
                element = element + 1
    return (found, search_item, element)

print(seq_search_1([1,2,3,4,5,6,7,8,9], 8))
print(seq_search_1([1,2,3,4,5,6,7,8,9], 12))


def seq_search_2(search_lst, search_item):
    position = 0
    found = False
    while position < len(search_lst) and not found:
        if search_lst[position] == search_item:
            found = True
            break
        else:
            position = position + 1
    return (found, search_item, position)

print(seq_search_2([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(seq_search_2([1, 2, 3, 4, 5, 6, 7, 8, 9], 12))


def seq_search_mid(search_lst, search_item):
    position, found, first, last  = 0, False, 0, len(search_lst)-1
    return (found, search_item, found)

