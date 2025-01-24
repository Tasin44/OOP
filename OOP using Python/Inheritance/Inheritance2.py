
#Single Inheritance example-2

#Subclassing (Calling constructor of parent class)

#Single Inheritance: A child class inherits from one parent class.
class Person(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        return f'{self.name},his id {self.id},income: {self.salary}, designation: {self.position}'

class Employee(Person):
    def __init__(self,name,id,salary,position):

        # Initialize the parent class attributes first
        super().__init__(name, id)  # Recommended way to call parent class's __init__
        
        """or we can also do in this way """
        #Person.__init__(self,name,id)
        
        '''
        If we don't invoke the __init__() of the parent class then 
        its instance variables would not be available to the child class.
        '''
        # Then initialize the child class specific attributes
        self.salary=salary
        self.position=position

obj=Employee("Tasin",62,62000,"intern")

print(obj.display())

'''
1.The display method in the Person class take references of self.salary and self.position.

2.Must be wirte Person.__init__(self,name,id) before 
self.salary=salary
self.position=position
because  it's generally good practice to call the parent class's __init__ method 
before initializing attributes specific to the child class if the parent class 
depends on those attributes. 

Initialization Order: 
The super() function is the recommended way to call the parent class's methods because it ensures proper method resolution order (MRO) in cases of multiple inheritance.

The parent class __init__ method should be called first 
to set up the name and id attributes.

Child-Specific Attributes: After calling the parent class __init__ method, 
the salary and position attributes specific to the Employee class are initialized.

'''

'''

Protected, Public, and Private Members:

super() and Industry.__init__(...) can access public and protected members of the parent class without any issues.
For private members (those with names starting with __, like __salary), name mangling applies.


'''





