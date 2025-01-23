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

'''
Examples of Protected and private attribute in Encapsulation :
'''

#EXAMPLE-1(Protected Attribute )
class Protected:
    def __init__(self):
        self._age = 30  # Protected attribute, it's accessible in it's own class

class Subclass(Protected):
    def display_age(self):
        print(self._age)  # Protected attribute is also Accessible in subclass

obj = Subclass()#must be call the subclass always 
obj.display_age() # This method within the subclass accesses the protected attribute and prints its value. 



#EXAMPLE-2(Protected Attribute access with the classname )
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



"""
*************************
If you want to access private attributes or private methods outside of their defining class (even in a child class), 
you must use the name-mangled format, which is _ParentClassName__attribute or _ParentClassName__method().

This is because Python uses name mangling to make private members "inaccessible" outside the defining class. 
***********************
"""

class Base:

    def __init__(self):
        self.__privateattribute=5

class derived(Base):

    def __init__(self):
        Base.__init__(self)
        print("Calling private attribute of Base Class: ",self._Base__privateattribute)
        self._Base__privateattribute+=7
        print("Calling private attribute of Child class: ",self._Base__privateattribute)
    
obj=derived()

# output:
# Calling private attribute of Base Class:  5
# Calling private attribute of Child class:  12



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
In Python, the super() function is used to refer to the parent class or superclass. 
It allows you to call methods defined in the superclass(parent class) from the subclass(child class), 
enabling you to extend and customize the functionality inherited from the parent class.

Main: super() allows you to call a parent class's methods or constructor(__init__) from a child class without explicitly naming the parent class.

super() is specifically designed to access protected members or methods (or public ones) of a parent class in a child class. 
It cannot be used to directly access private members or methods, because private members are name-mangled in Python and not directly accessible through super().
super() is also not applicable to access protected attribute
'''


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




Super() examples :



class Parent:
    def __init__(self):
        self.__private = "Private Attribute"
        self._protected = "Protected Attribute"
    
    def __private_method(self):
        print("Parent's Private Method")
    
    def _protected_method(self):
        print("Parent's Protected Method")

    def public_method(self):
        print("Parent's Public Method")

class Child(Parent):
    def show(self):
        # Call protected method
        super()._protected_method()

        # Call public method
        super().public_method()

        # The following will cause an error:
        
        # print("Protected Attribute:", super()._protected)
        # super().__private  # ❌ AttributeError
        # super().__private_method()  # ❌ AttributeError

        # To access private members, use name mangling:
        print("Private Attribute (via name mangling):", self._Parent__private)
        self._Parent__private_method()

obj = Child()
obj.show()
