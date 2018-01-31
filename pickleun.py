"""

Pickle Implementation:

Serializing and De-Serializing Python objects is called Pickling / Un-Pickling.

There are two, methods,

1) Dump - Writing Python objects into a file
2) Load - Reading Python objects from a file

Ref: https://pythontips.com/2013/08/02/what-is-pickle-in-python/

"""


import pickle


a = ['test_value', 'test_value_1', 'test_value_2', 'test_value_3', 'test_value_4']

file_name = "pickle.txt"
f = open(file_name, 'wb')
pickle.dump(a, f)
f.close()

fo = open(file_name, 'r')
print(pickle.load(fo))
