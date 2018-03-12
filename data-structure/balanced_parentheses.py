from __future__ import print_function
from __future__ import absolute_import
from stack import Stack


__author__ = 'Felix Stephen'

def balanced_parentheses(parentheses):
    """ Use a stack to check if a string of parentheses are balanced."""
    stack = Stack(len(parentheses))
    for parenthesis in parentheses:
        if parenthesis == '(':
            stack.push(parenthesis)
        elif parenthesis == ')':
            stack.pop()
    return not stack.is_empty()


if __name__ == '__main__':
    examples = ['((()))', '((())']
    print('Balanced parentheses demonstration:\n')
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))


#def balanced_para(paran):
#    a, b = [], []
#    for i in paran:
#        if i == "(":
#            a.append(i)
#        elif i == ")":
#            b.append(i)
#    if len(a) == len(b):
#        print("{} - True".format(paran))
#    else:
#        print("{} - False".format(paran))


#if __name__ == '__main__':
#    balanced_para("((()))))")

