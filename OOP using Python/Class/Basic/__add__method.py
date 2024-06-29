'''
__add__() magic method
Python __add__() method adds two objects and returns 
a new object as a resultant object in Python. 
'''
# methods with double underscores (__method__) are special methods that have specific meanings.
# The __add__ method is designed to handle addition operations 
# between two instances of the same class(here Person class)
# If you define the __add__ method in the Person class, 
# it's specifically for handling addition operations involving instances of the Person class.
# You can't directly use the __add__ method of the Person class to perform addition 
# operations with instances of other classes ,
# if you want to do so,u will get TypeError

class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __add__(self, other):
            total_age = self.age + other.age
            total_weight = self.weight + other.weight
            joint_name=self.name+other.name
            return total_age, total_weight ,joint_name

obj1 = Person("Alim", 25, 90)
obj2 = Person("karim", 30, 60)

print(obj1 + obj2)  # Output: (55, 150)
