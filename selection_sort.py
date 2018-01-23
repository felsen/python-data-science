"""
Selection Sort Implementation:
    finding the minimum number from the list, then it will be placed in the first position, then repeat the same.

    https://www.geeksforgeeks.org/python-program-for-selection-sort/
"""


def selection_sort(sort_list):
    for i in range(len(sort_list)):
        min_idx = i
        for j in range(i+1, len(sort_list)):
            if sort_list[min_idx] > sort_list[j]:
                min_idx = j
        sort_list[i], sort_list[min_idx] = sort_list[min_idx], sort_list[i]
    return sort_list


print(selection_sort([3, 5, 7, 6, 2, 8, 9, 4]))

