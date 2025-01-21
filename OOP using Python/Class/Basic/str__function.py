'''
The __str__() Function

The __str__() function controls what should be returned when the class object is represented as a string.

The __str__ method is a special method in Python that is called by the print function 
and the str function to get the string representation of an object.

To get the default string representation of the object, you should define the __str__ method in the class.

The __str__() method returns a human-readable, or informal, string representation of an object. 
This method is called by the built-in print(), str(), and format() functions. 

If you don’t define a __str__() method for a class, then the built-in object implementation calls the __repr__() method instead.
'''
#example-1
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1) 


#example-2 This approach avoids using __str__ but still allows you to get meaningful output
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 


#This approach avoids using __str__ but still allows you to get meaningful output

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def print(self):
    return f"{self.name},{self.age}"


p1 = Person("John", 36)

print(p1.print())

#__str__() and __repr__() Examples Using a New Class
class Ocean:

    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age
    
    def __str__(self):
        return f'The creature type is {self.name} and the age is {self.age}'

    def __repr__(self):
        return f'Ocean(\'{self.name}\', {self.age})'

c = Ocean('Jellyfish', 5)

print(str(c))
print(repr(c))


