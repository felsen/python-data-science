"""
Example of Public, Private and Protected variables in Python.

Defaultly all the variables are public.

Any variable which is starts with _protected is Protected variable.

Any variable which is starts with __private is Private variable.

Ref: http://radek.io/2011/07/21/private-protected-and-public-in-python/

"""


class PublicCup:
    
    def __init__(self):
        self.color = None
        self.content = None

    def fill(self, flavour):
        self.content = flavour

    def empty(self):
        self.content = None

pb = PublicCup()
pb.color = "red"
pb.content = "coffee"
pb.fill("tea")
print(pb.content)
pb.empty()
print(pb.content)


class ProtectedCup:

    def __init__(self):
        self.color = None
        self._content = None

    def fill(self, flavour):
        self._content = flavour

    def empty(self):
        self._content = None

pt = ProtectedCup()
pt.color = "blue"
pt._content = "tea"
print(pt._content)


class PrivateCup:

    def __init__(self, color):
        self._color = color
        self.__content = None

    def fill(self, flavour):
        self.__content = flavour

    def empty(self):
        self.__content = None

