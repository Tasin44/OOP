
#if we use two or more __ (underscore)before any attribut,then it'll consider as a restricted access
#private attribute(variable) only accessible only inside this class.
'''
Private Attribute
A private attribute is an attribute that is not meant to be accessed 
directly from outside the class.

Private Method
A private method is a method that is not meant to be called from outside the class.

'''
class Person:
    def __init__(self,name,password,phone):
        self.identity=name
        self.__paword=password # Private attribute
        self.number=phone

user=Person('Tasin','abcd123','01893')
print(user.__paword)
#AttributeError: 'Person' object has no attribute '__paword'

#solution
class Person:
    def __init__(self,name,password,phone):
        self.identity=name
        self.__paword=password
        self.number=phone
    def get_attribute(self):
        print(self.__paword)

user=Person('Tasin','abcd123','01893')
user.get_attribute()


#if we make any method private,then it won't be accessible outside of the class 
class Person:
    def __init__(self,name,password,phone):
        self.identity=name
        self.__paword=password
        self.number=phone
    def __get_attribute(self): #private_method
        print(self.__paword)

user=Person('Tasin','abcd123','01893')
user.__get_attribute()
#Error:AttributeError: 'Person' object has no attribute '__get_attribute'


#solution:
class Person:
    def __init__(self,name,password,phone):
        self.identity=name
        self.__paword=password
        self.number=phone
    def ___get_attribute(self):
        print(self.__paword)
    def public_attribute(self):
        print('This is public now')
        self.___get_attribute()# Calling the private method from within the class

user=Person('Tasin','abcd123','01893')
user.public_attribute()
















