"""
Insertion Sort Implementation:
    Take the first element and compare with all the elements; then insert it,    
    Note: If any duplicate elements present in the insertion sort, then then algorithm will fail.

Reference Link:
    http://www.geekviewpoint.com/python/sorting/insertionsort
    https://www.studytonight.com/data-structures/insertion-sorting
    http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
"""


def insertion_sort(sort_list):
    for index in range(len(sort_list)):
        position = index
        while ( position > 0 and sort_list[index] < sort_list[position-1]):
            sort_list[position] = sort_list[position-1]
            position -= 1
        sort_list[position] = sort_list[index]
    return sort_list


def insertion_sort_2(sort_list):
    sort_list = set(sort_list)
    for i in sort_list:
        ind = sort_list.index(i)
        while (ind > 0) :
            if sort_list[ind-1] > sort_list[ind]:
                sort_list[ind-1], sort_list[ind] = sort_list[ind], sort_list[ind-1]
            else:
                break
            ind = ind - 1
    return sort_list

print(insertion_sort_2([1, 5, 4, 3, 2, 6, 7, 8]))
print(insertion_sort_2([16, 19, 11, 15, 10, 12, 14]))

