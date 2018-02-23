"""
difference between str and repr.
"""


class Pair(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Pair({0.x!s} {0.y!s})".format(self)

    def __str__(self):
        return "{0.x!s} {0.y!s}".format(self)


p = Pair(2, 3)
print(p.__str__())  # customer definition
print(p.__repr__())  # Technical definition


_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}-{d.month}-{d.year}'
}


class Date(object):

    __slots__ = ["year", "date", "month"]

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == "":
            code = "ymd"
        fmt = _formats[code]
        return fmt.format(d=self)


d = Date(2018, 02, 22)
print(format(d))
print(format(d, 'mdy'))
print(format(d, 'dmy'))

