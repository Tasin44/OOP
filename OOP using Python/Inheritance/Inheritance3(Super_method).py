
#Single inheritance example-3

'''
The super() function is a built-in function that returns the objects 
that represent the parent class. 
It allows to access the parent class’s methods and attributes in the child class.
It enabling you to extend and customize the functionality inherited from the parent class.

Multiple Inheritance: In cases of multiple inheritance,super() ensures that the method 
resolution order (MRO) is followed,and all necessary initializations are performed.

The super function should be called as a function like super()., not as a class attribute like super.
'''

class Person(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        return f"{self.name}\nhis id {self.id}\nincome: {self.salary}\ndesignation: {self.position}"
        #we can return f using both ' or "

class Employee(Person):
    def __init__(self,name,id,salary,position):

        # Initialize the parent class attributes first
        super().__init__(name,id)
        '''
        If don't invoke the __init__() of the parent class then 
        its instance variables would not be available to the child class.
        '''
        # Then initialize the child class specific attributes
        self.salary=salary
        self.position=position

obj=Employee("Tasin",62,62000,"intern")

print(obj.display())

'''
Order of Initialization:
1.The parent class attributes (name and id) are initialized first.
2.The child class specific attributes (salary and position) are initialized afterward.
'''
