"""
Bubble Sort ;

Comparing the first tow element, once get satisfied then will be started to compare the next element's.

http://www.geekviewpoint.com/python/sorting/insertionsort

https://www.studytonight.com/data-structures/insertion-sorting

"""

def bubble_sort(sort_list):
    for i in range(len(sort_lilst), 0, -1):
        for j in range(i):
            if sort_list[j]>sort_list[j+1]:
                temp = sort_list[j]
                sort_list[j] = sort_list[j+1]
                sort_list[j+1] = temp
    return sort_list
                

def bubble_sort_2(sort_list):
    for i in range(len(sort_list)):
        for j in range(i):
            if sort_list[j] > sort_list[j+1]:
                a = sort_list[j]
                sort_list[j] = sort_list[j+1]
                sort_list[j+1] = a
    return sort_list

print(bubble_sort_2([1,85,4,3,2,5,6,7]))
