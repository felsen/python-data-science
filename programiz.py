"""
Reference: https://www.programiz.com/python-programming/examples
Ref: https://www.pythoncentral.io/

1) adding two numbers.
2) square root of numbers.
3) calculating the area of triangle.

"""


def add_two_numbers(num_one, num_two):
    total = float(num_one) + float(num_two)
    return "Total - {} + {} = {}".format(num_one, num_two, total)

print(add_two_numbers(12.8, 34.5))


def square_root(num):
    """
    another way of doing the square root is,

    import cmath / import math
    cmath.sqrt(12) >>> (3.46410161514)
    math.sqrt(12) >>> (3.46410161514)
    """
    root = num ** 0.5
    return "Square root of given number is {}".format(root)

print(square_root(8))
print(square_root(12))


def triangle_area(side_a, side_b, side_c):
    sides = (side_a + side_b + side_c) / 2
    area = (sides*(sides - side_a)*(sides - side_b)*(sides - side_c)) ** 0.5
    return "Area of the Triangle is {}".format(area)

print(triangle_area(10, 20, 30))
