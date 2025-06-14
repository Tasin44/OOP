'''
✅ 1. Instance Methods
✔️ When to use:

    You want to access or modify data specific to an instance of the class.

    These always take self as the first argument.
'''

def get_emp_details(self):
    print('Name: ', self.fullname)
    print('Salary: ', self.salary)

'''
🔑 Why use:

    To get/set data that belongs to one specific employee (emp1, emp2).

    Needs access to self, because instance data (like self.salary) is unique per object.
'''


========================================================================================================================================================
classmethod and staticmethod
'''
When it's a general information about the whole project or code, then we should use @staticmethod
No need to use self (as a argument) on the @staticmethod, because in staticmethod, we don't use any instance here 
'''
class Geeks:
    course = 'DSA'
    list_of_instances = []

    def __init__(self, name):
        self.name = name
        Geeks.list_of_instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course: {cls.course}"

    @classmethod
    def get_instance_count(cls):
        return f"Number of instances: {len(cls.list_of_instances)}"

    @staticmethod
    def welcome_message():
        return "Welcome to Geeks for Geeks!"

# Creating instances
g1 = Geeks('Alice')
g2 = Geeks('Bob')

# Calling class methods
print(Geeks.get_course())  
print(Geeks.get_instance_count())  

# Calling static method
print(Geeks.welcome_message())



========================================================================================================================================================


#STEP:1
class Employee:
    incriment=0.02 #incriment is a class variable 
    def __init__(self,f,l=None,sal=None):#default arguments,must be filling from right to left .
    # if I miss passing some argument, by default these variables will take None.
    # we can put here some ohter arguments value 

        self.first=f
        self.last=l
        self.salary=sal
        self.fullname=self.first+' '+self.last
    
    def set_incri_salary(self):#it's a instance method
        self.salary+=self.salary*Employee.incriment
    
    def get_emp_details(self):#it's a method
        print('Name: ',self.fullname)
        print('Salary: ',self.salary)

emp1=Employee('Samuel','Edison',10000)
emp2=Employee('Tomas','Alva',20000)
emp1.get_emp_details()
emp2.get_emp_details()
emp1.set_incri_salary()
emp2.set_incri_salary()
emp1.get_emp_details()
emp2.get_emp_details()



========================================================================================================================================================

#STEP:2 class method

'''
it's always better to use classmethod to change or update the class variable,
instead of instance method,
if u want to update instance variable = use instance method
if u want to update class variable = use classmethod
'''

class Employee:
    incriment=0.02 #class variable 
    def __init__(self,f,l=None,sal=None):#it's a instance method

        self.first=f
        self.last=l
        self.salary=sal
        self.fullname=self.first+' '+self.last
    
    def set_incri_salary(self):#it's a instance method
        self.salary+=self.salary*Employee.incriment
    
    def get_emp_details(self):#it's a instance method
        print('Name: ',self.fullname)
        print('Salary: ',self.salary)
    
    @classmethod
    def set_incri_percentage(self,new_percentage):
        self.incriment=new_percentage


emp1=Employee('Samuel','Edison',10000)
emp2=Employee('Tomas','Alva',20000)
Employee.set_incri_percentage(0.07)#using class name to call the class method,
                                   #can also use emp1 or emp2 object to call the class method
emp1.set_incri_salary()
emp2.set_incri_salary()
emp1.get_emp_details()
emp2.get_emp_details()




========================================================================================================================================================

#STEP:3 use class method to create an alternative constructor
#if we don't use classmethod 
class Employee:
    def __init__(self,f,l=None,add=None):#it's a instance method

        self.first=f
        self.last=l
        self.fullname=self.first+' '+self.last
        self.address=add
    
    def get_emp_details(self):#it's a instance method
        print('Name: ',self.fullname)
        print('Address: ',self.address)


emp1=Employee('Samuel','jhon','india')
emp1.get_emp_details()

emp1_info='Sam,Carun,England'
first,second,address=emp1_info.split(',')
'''
Giving the info about the person in a comma separeted string ,& then spreading it with 
the help of split method.Then storing into three different variables 
'''
emp2=Employee(first,second,address)#crating an instance(Employee) and passing these 3 variables
emp2.get_emp_details()
  


#now,if we use the classmethod

class Employee:
    def __init__(self,f,l=None,add=None):#it's a instance method
                            #when i create an obejct of this class ,init method will be called 
        self.first=f
        self.last=l
        self.fullname=self.first+' '+self.last
        self.address=add
    
    def get_emp_details(self):#it's a instance method
        print('Name: ',self.fullname)
        print('Address: ',self.address)
    @classmethod
    def update_new_info(self,info):
       first,second,address=emp1_info.split(',')#spliting the string and storing it into 3 different variables 
       return self(first,second,address)


emp1=Employee('Samuel','jhon','india')
emp1.get_emp_details()

emp1_info='Sam,Ali,Canada'

emp2=Employee.update_new_info(emp1_info)#calling the method with the help of class name
#(by creating instance of Employee class),after that, passing the strings(emp1_info)
#then the strings will go to "update_new_info" and get stored to "info"
emp2.get_emp_details()
  




========================================================================================================================================================


STATIC METHOD

'''
No implicit arguments:
Unlike instance methods (which take self as the first argument) or class methods (which take cls), static methods do not receive any implicit first argument.

Here we'll use staticmethod to print information,
staticmethod associated with the class and can be called directly on the class itself without creating an instance.

Cannot modify class or instance state:
Static methods do not have access to instance-specific attributes or class-specific attributes


When to use static methods:

    When a function is logically related to a class but does not need to access any specific instance or class data.
    For utility functions or helper methods that are relevant to the class but are independent of the object's state.
    To group related functions within a class for better code organization.

    if we want to something inside class but it's not related to anything to do with the class 
    information means no process is going to happen because of that,
    then we should use static method 

When it's a general information about the whole project or code, then we should use @staticmethod
No need to use self (as a argument) on the @staticmethod, because in staticmethod, we don't use any instance here 
'''


class Employee:
    cnt_employee=0
    def __init__(self,f,l=None,add=None):
        Employee.cnt_employee+=1 # or  self.__class__.cnt_employee += 1
        self.first=f
        self.last=l
        self.fullname=self.first+' '+self.last
        self.address=add
    
    def get_emp_details(self):#it's a instance method
        print('Name: ',self.fullname)
        print('Address: ',self.address)
    @staticmethod
    def number_of_employee():
        print(f'Total number of employee:{Employee.cnt_employee},so total {Employee.cnt_employee} objects cereated ')


emp1=Employee('Samuel','jhon','india')
emp2=Employee('Sam','Ali','Canada')

# Accessing instance methods and static method
emp1.get_emp_details()
emp2.get_emp_details()
# Accessing static method
Employee.number_of_employee()


