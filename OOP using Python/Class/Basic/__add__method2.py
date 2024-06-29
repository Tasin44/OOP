

#the __add__method can add only two object,but if we want to add more than two objects:
class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Person):
            tot_age = self.age + other.age
            tot_weight = self.weight + other.weight
            joint_name = self.name + other.name
            return Person(joint_name, tot_age, tot_weight)
        return NotImplemented

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}"

# Creating Person objects
obj1 = Person("Tasin", 29, 20)
obj2 = Person("Kamal", 25, 40)
obj3 = Person("Rahim", 30, 80)
obj4 = Person("Jamil", 55, 20)

# Chaining additions
result = obj1 + obj2 + obj3 + obj4 + 7  # This will raise a TypeError

# Printing the result
print(result)
'''
If you try to add a Person object to an integer like 7 
(i.e., result = obj1 + obj2 + obj3 + obj4 + 7), 
the absence of the "if isinstance(other, Person)" check 
and the "return NotImplemented" statement in the __add__ method 
will cause a runtime error because the __add__ method's addition operation 
expects another Person object(like obj5).

Here’s what will happen step by step:

Adding obj1 and obj2:
intermediate1 = obj1 + obj2  # This creates a new Person object

Adding intermediate1 and obj3:
intermediate2 = intermediate1 + obj3  # This creates another new Person object

Adding intermediate2 and obj4:

intermediate3 = intermediate2 + obj4  # This creates yet another new Person object

Attempting to Add intermediate3 and 7:

result = intermediate3 + 7  # This will cause an error

Here's what the error might look like:
AttributeError: 'int' object has no attribute 'age'

but if we use return NotImplemented,then will occur type error
TypeError: unsupported operand type(s) for +: 'Person' and 'int'

'''

