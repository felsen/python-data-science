"""
property.
"""


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected string.")
        self._first_name = value

    @property
    def last_name(self):
        self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected string.")
        self._last_name


p = Person("felix")
print(p.first_name)
p.first_name = "stephen"
print(p.first_name)
del p.first_name

