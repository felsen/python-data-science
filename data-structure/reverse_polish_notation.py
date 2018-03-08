"""
Reverse Polish Notation Implemntation.
"""

import re

def reverse_polish_notation(expression):
    expr_lst = ["+", "-", "*", "/"]
    print(re.findall(r"(\d+)", expression))
    print(re.findall(r"(\W+)", expression))




if __name__ == '__main__':
    reverse_polish_notation("1 2 +")

