"""
property.
"""


class Person:

    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise AttributeError("Expected string.")
        self._first_name = value

    # @first_name.deleter
    # def first_name(self):
    #     raise AttributeError("Can't delete attribute.")

    def __del__(self):
        raise AttributeError("Can't delete attribute")


p = Person("felix")
print(p.first_name)
p.first_name = "stephen"
print(p.first_name)
del p.first_name

