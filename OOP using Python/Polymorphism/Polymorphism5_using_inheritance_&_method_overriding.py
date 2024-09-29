'''
What is method overriding in polymorphism?

Method overriding occurs when a subclass provides a specific implementation of a method 
that is already defined in its superclass.This allows the subclass to customize or 
completely replace the behavior of the method inherited from the superclass.
'''

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

'''
The Animal class defines a method "speak" that raises a NotImplementedError. 
This(NotImplementedError) serves as an abstract method, which means that it is intended to be overridden in subclasses.
By raising NotImplementedError, 
you enforce that any subclass of Animal must provide its own implementation of the speak method.
'''
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create a list of Animal objects
animals = [Dog(), Cat()]

# Call the speak method on each object
'''
A loop iterates through the list and calls the speak method on each object.
Due to polymorphism, the correct speak method for each object type (either Dog or Cat) is called.
'''
for animal in animals:
    print(animal.speak())

'''
Output
Woof!
Meow!

'''

