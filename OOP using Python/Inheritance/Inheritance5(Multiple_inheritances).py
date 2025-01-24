
'''
Multiple inheritances: When a child class inherits from multiple parent classes, 
it is called multiple inheritances. 
In multiple inheritances, all the features of the base classes are inherited into the derived class. 
'''


class Father:
    def __init__(self,fname):
        self.fname=fname

class Mother:
    def __init__(self,mname):
        self.mname=mname
    
class Son(Father,Mother):
    def __init__(self, fname,mname):
        super().__init__(fname) #We can also do :  Father.__init__(self, fname)
        Mother.__init__(self,mname)
    def display_parent_info(self):
        print("Father name: ", self.fname)
        print("Mother name: ",self.mname)

obj=Son("Nannu","Taslima")
obj.display_parent_info()



'''
We cann't use super() for all parent classes;
he super() mechanism works based on the Method Resolution Order (MRO), which means it only calls the next class in the inheritance chain as defined by the MRO.
Therefore, you cannot directly use super() to call both Father and Mother's __init__ methods
like super().__init__(fname)  
     super().__init__(mname)

According to the above code, the MRO is:

[Son, Father, Mother, object]

So, if you call super().__init__() in Son, it will invoke Father's __init__ method, but it won't automatically call Mother's __init__ method.
'''

'''
But if we want to use super for both Father and Mother class:
There is a solution called 
Cooperative Initialization
'''

class Father:
    def __init__(self,fname,**kwargs):
        super().__init__(**kwargs)
        self.fname=fname

class Mother:
    def __init__(self,mname,**kwargs):
        super().__init__(**kwargs)
        self.mname=mname
    
class Son(Father,Mother):
    def __init__(self, fname,mname):
        super().__init__(fname=fname, mname=mname)  # Pass arguments for both parents
        
    def display_parent_info(self):
        print("Father name: ", self.fname)
        print("Mother name: ",self.mname)

obj=Son("Nannu","Taslima")
obj.display_parent_info()




        




















        
