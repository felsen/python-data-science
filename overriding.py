"""
Overriding concept's in Python.

Two methods with the same name but doing different task, which means one methods is overriding another.

Ref: https://www.codesdope.com/python-lets-override/
"""


class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth


class Square(Rectangle):
    
    def __init__(self, side):
        self.side = side
        Rectangle.__init__(self, side, side)

    def get_area(self):
        return self.side * self.side

s = Square(4)
r = Rectangle(4, 2)
print(s.get_area())
print(r.get_area())
