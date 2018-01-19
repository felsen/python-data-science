"""
Sum of List of Numbers.
"""

def sum_of_list_1(num_list):
    s = 0
    for i in num_list:
        s += i
    return s

print(sum_of_list_1([1,2,3,4,5,6,7,8,9]))


def sum_of_list_2(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sum_of_list_2(num_list[1:])

print(sum_of_list_2([1,2,3,4,5,6,7,8,9]))
