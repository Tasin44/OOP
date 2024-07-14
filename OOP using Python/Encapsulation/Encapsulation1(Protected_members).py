'''
Encapsulation is the concept of bundling the data (attributes) and methods (functions) 
that operate on the data into a single unit, or class, and restricting access to some of the object's components. 
This means that the internal representation of an object is hidden from the outside.

Encapsulation describes the idea of wrapping data and the methods that work on data within one unit. 
This puts restrictions on accessing variables and methods directly 
and can prevent the accidental modification of data. To prevent accidental change, 
an object’s variable can only be changed by an object’s method. 
Those types of variables are known as private variables.

Protected Members:
Protected members are those that are intended to be accessed only within the class 
and its subclasses.In Python, protected members are defined by prefixing the member 
name with a single underscore (_).

'''
#In Python,encapsulation is achieved using private and protected members.

#EXAMPLE-1
class Base(object):
    def __init__(self):
        self._a=2
class derived(Base):
    def __init__(self):
       Base.__init__(self)
       print("Calling protected member of base class: ",self._a)
       self._a+=3
       print("Calling protected member of child class: ",self._a)

obj1=derived()


#EXAMPLE-2
class BaseClass:
    def __init__(self):
        self._protected_attribute = 42  # Protected attribute

    def _protected_method(self):
        print("This is a protected method.")

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        print(self._protected_attribute)  # Accessing protected attribute
        self._protected_method()  # Accessing protected method

obj = DerivedClass()
print(obj._protected_attribute)  # This will work, but it's not recommended
obj._protected_method()  # This will work, but it's not recommended

'''
In the above example:
# _protected_attribute and _protected_method are protected members.
# Protected members can be accessed within the class and its subclasses.
# Accessing protected members outside the class or its subclasses is technically allowed but is discouraged.
'''
