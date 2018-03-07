"""
Inheritance Implemntation..
"""


class Person(object):

    def __new__(cls, *args, **kwargs):
	instance = super(Person, cls).__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class NewPerson(Person):

    pass


class Employee(NewPerson):

    def is_employee(self):
        return True


"""
------------------------------------------------------------------------------
"""


class Base1(object):

    def __init__(self):
        self.str1 = "Geek1"


class Base2(object):

    def __init__(self):
        self.str2 = "Geek2"


class Derived(Base1, Base2):

    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

    def print_strs(self):
        return "{} {}".format(self.str1, self.str2)


"""
------------------------------------------------------------------------------
"""


class Base3(object):

    def __init__(self, x):
        self.x = x


class Derived1(Base3):

    def __init__(self, x, y):
        Base3.x = x
        self.y = y

    def print_xy(self):
        return "{} {}".format(self.x , self.y)


"""
-----------------------------------------------------------------------------
"""


class Base4(object):

    def __init__(self, x):
        self.x = x


class Derived4(Base4):

    def __init__(self, x, y):
        super(Derived4, self).__init__(x)
        self.y = y

    def print_xy(self):
        return "{} {}".format(self.x, self.y)


"""
-----------------------------------------------------------------------------
"""


class X(object):

    def __init__(self, a):
        self.num = a

    def double(self):
        return self.num * 2


class Y(X):

    def __init__(self, a):
        X.__init__(self, a)
        
    def triple(self):
        return self.num * 3


"""
----------------------------------------------------------------------------
"""


class Person1(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee1(Person1):

    def __init__(self, name, eid):
        super(Employee1, self).__init__(name)
        self.eid = eid

    def is_employee(self):
        return True

    def get_empid(self):
        return self.eid


"""
----------------------------------------------------------------------------
"""


if __name__ == '__main__':

    """
    """
    person = Person(name="felix")
    print(person.is_employee())

    new_person = NewPerson(name="stephen")
    print(new_person.is_employee())
    
    employee = Employee(name="felsen")
    print(employee.is_employee())
    print(employee.get_name())
    """
    """
    ob = Derived()
    print(ob.print_strs())
    """
    """
    b3 = Base3(x=2)
    print(b3.x)

    d0 = Derived1(x=4, y=5)
    print(d0.print_xy())
    """
    """
    d1 = Derived4(10, 20)
    print(d1.print_xy())
    """
    """
    obj = Y(4)
    print(obj.double())
    print(obj.triple())
    """
    """
    emp = Employee1(name='employee_name', eid=12)
    print(emp.get_name())
    print(emp.get_empid())
    print(emp.is_employee())
    """
    """
