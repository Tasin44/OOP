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


#STEP:2 class method

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

'''
it's always better to use classmethod to change or update the class variable,
instead of instance method,
if u want to update instance variable = use instance method
if u want to update class variable = use classmethod
'''



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
  







#STATIC METHOD

'''
Here we'll use staticmethod to print information,the
staticmethod doesn't take any argument because it doesn't belong to class
(it doesn't process anything to class),
it's a kind of standalone function 
When we'll use staticmethod:
if we want to something inside class but it's not related to anything to do with the class 
information means no process is going to happen because of that,
then we should use static method 
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


