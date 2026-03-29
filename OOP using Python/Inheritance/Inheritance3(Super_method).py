
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
'''
in django 
Why super().save(*args, **kwargs)?

It calls the parent class's save method to actually save the object to the database after your custom logic.
What are *args and **kwargs?

They capture and pass through any arguments the save method receives:

    *args = positional arguments (like force_insert, using)

    **kwargs = keyword arguments (like force_insert=True, using='default')

Example:
# When Django calls save with arguments:
article.save(force_insert=True, using='default')

# Without *args, **kwargs:
def save(self):
    super().save()  # ❌ Loses force_insert and using arguments

# With *args, **kwargs:
def save(self, *args, **kwargs):
    super().save(*args, **kwargs)  # ✅ Preserves all original arguments
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
