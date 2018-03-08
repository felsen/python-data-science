"""
MRO - Inheritance Implementation Part II
"""


class A:
 
    def who_am_i(self):
        print("A")


class B(A):

    def who_am_i(self):
        print("B")


class C(A):

    def who_am_i(self):
        print("C")


class D(B, C):

    def who_am_i(self):
        print("D")


"""
----------------------------------------------------
"""


class A1:

    def who_am_i(self):
        print("A1")


class B1(A1):

    def who_am_i(self):
        print("B1")


class C1(A1):

    def who_am_i(self):
        print("C1")


class D1(B1, C1):

    pass


"""
----------------------------------------------------
"""


class A2:

    def who_am_i(self):
        print("A2")


class B2(A2):

    pass


class C2(A2):

    def who_am_i(self):
        print("C2")


class D2(B2, C2):

    pass


"""
----------------------------------------------------
"""


class A3:

    pass


class B3(A3):

    pass


class C3(A3):

    def who_am_i(self):
        print("C3")


class D3(B3, C3):

    pass 


"""
---------------------------------------------------
"""


class A4(object):

    def who_am_i(self):
        print("A4")


class B4(A4):

    pass


class C4(A4):

    def who_am_i(self):
        print("C4")


class D4(B4, C4):

    pass


"""
--------------------------------------------------
"""

if __name__ == '__main__':
    """
    """
    d = D()
    d.who_am_i()
    """
    """
    d1 = D1()
    d1.who_am_i()
    """
    """
    d2 = D2()
    d2.who_am_i()
    """
    """
    d3 = D3()
    d3.who_am_i()
    """
    """
    d4 = D4()
    d4.who_am_i()
