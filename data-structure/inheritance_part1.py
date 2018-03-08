"""
Inhertance Implementation Part1
"""


class Car(object):

   wheels = 4

   def __init__(self, make, model):
       self.make = make
       self.model = model


   @staticmethod
   def make_car_sound():
       return "VRooooooon"



class Vechile(object):
 
   @classmethod
   def is_motercycle(cls):
	return cls.wheels == 2




"""
--------------------------------------------------------------
"""   


if __name__ == '__main__':
    obj = Car(make="Ford", model="1000e")
    print(obj.wheels)
    print(Car.wheels)
    print(obj.make_car_sound())
