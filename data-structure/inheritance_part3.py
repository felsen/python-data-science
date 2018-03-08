"""
MRO Implementation Part III
"""


class X():

    def who_am_i(self):
        print("X")


class Y():

    def who_am_i(self):
        print("Y")


class A(X, Y):

    def who_am_i(self):
        print("A")


class B(Y, X):

    def who_am_i(self):
        print("B")


class F(A, B):

    def who_am_i(self):
        print("F")



if __name__ == '__main__':
    """
    """
    f = F()
    f.who_am_i()
