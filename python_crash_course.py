"""
The content of the file is taken from the book Python Crash Course.

Reference: http://ap-n.us/books/Programming/Python%20Crash%20Course.pdf

"""


"""
Naming and Variables:

>> Variable should not starts with numbers
>> Variable should be in Lowercase always.
>> Avoid python keywords to assign a variable name.
>> use a proper keyword,
   Ex: 
     f_n should be first_name
     name_of_the_person should be person_name.
"""


>>> message = "Python crash course reader.!"
>>> print(mesage)
Traceback (most recent call last):
  File "python_crash_course.py", line 22, in <module>  
    print(mesage)                                                                                                                      
NameError: name 'mesage' is not defined 


"""
String: is a series of charactors, anything inside the quotes is considered as a string,
this will be in single quotes or double quotes.
"""

>>> string_one = 'This is a single quote string!'
>>> string_tow = "This is a double quote string!"
>>> string_three = """ This is a trible quote string and also called Docs string! """
>>> name = "ada lovelace"
>>> print(name.title())
"Ada Lovelace"
>>> print(name.upper())
"ADA LOVELACE"
>>> print(name.lower())
"ada lovalace"
>>> message = 'One of Python's strengths is its diverse community.'
  File "<stdin>", line 44
    message = 'One of Python's strengths is its diverse community.'
                             ^
SyntaxError: invalid syntax


"""
Positional Argument's:
    Positional arguments will be accessed via index.
    Ex: *args

Keyword Argument's:
    Keyword arguments will be accessed via key-value pair.
    Ex: **kwargs

Error:
    TypeError: function() missing 2 required positional arguments: arg1, arg2

Optional Argument's:
    To aviod argument's error pass the default value to the positional argument's.
"""


class Dog:
    
    """
    Dog sitting / rolling model.
    """
    
    def __init__(self, name=None, age=None):
        """
        Dog is the class which has initiated with the name and age.
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        Dog sitting command.
        """
        return "{} is now sitting..".format(self.name.title())

    def roll(self):
        """
        Dog rolling command.
        """
        return "{} is rolling now..".format(self.name.title())
    

class Car:
    
    """
    Simple attempt to represent a car.
    """

    def __init__(self, make=None, model=None, year=None):
        """
        Initiating a car variable with basic attributes.
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        Getting a full descriptive name of the car.
        """
        return "{} car {} model {} make".format(self.make.title(),
                                                self.model.title(),
                                                self.year)

    def read_odometer(self):
        """
        Reading the odometer value.
        """
        return "Speed of the car per KM {}".format(self.odometer_reading)

    def update_odometer(self, milage):
        """
        Updating the odometer value in the device.
        """
        if self.odometer_reading <= milage:
            self.odometer_reading = milage:

    def increment_odometer(self, milage):
        """
        Incrementing the odometer value.
        """
        self.odometer_reading += milage


class ElectricCar(Car):
    """
    Passing parent class arguments to child class( Inheritance )
    """
    def __init__(self, make, model, year):
        """
        Initialize the attributes of parent class
        """
        super().__init__(make, model, year)

