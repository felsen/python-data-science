"""
Searching and Sorting.

1. Sequential's search(seq_search)
   Comparing the search item with the each element one by one incrementing the index of the list.
"""


def seq_search_1(search_lst, search_item):
    found, element = False, 0
    if not found:
        for i in search_lst:
            if search_item == search_lst[element]:
                found = True
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
        else:
            position = position + 1
    return (found, search_item, position)


print(seq_search_2([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(seq_search_2([1, 2, 3, 4, 5, 6, 7, 8, 9], 12))

