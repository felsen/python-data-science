"""
Sum of List of Numbers.
"""

def sum_of_list_1(num_list):
    s = 0
    for i in num_list:
        s += i
    return s

print(sum_of_list_1([1,2,3,4,5,6,7,8,9]))
