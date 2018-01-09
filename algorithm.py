"""
Algorithm is the stpe by step process to solve the problems.
"""
import time


def sum_of_n(n):
    the_sum = 0
    start_time = time.time()
    for i in range(0, n+1):
        the_sum = the_sum + i
    end_time = time.time()
    print("Time Required: {}".format(end_time-start_time))
    return the_sum

print(sum_of_n(10))

