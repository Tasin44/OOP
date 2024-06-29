class Calculation:
    def __init__(self,value):
        self.value=value
    def __call__(self,x):
        tsum=self.value+x
        tsub=self.value-x
        tmult=self.value*x
        tdiv=self.value/x
        return tsum,tsub,tmult,tdiv
        
# Create an instance of MyClass
obj = Calculation(10)

# Call the instance as if it were a function
result = obj.__call__(5)  # Equivalent to obj(5)
print(result)    # Output: 15,5,50,2.0

'''
"def __call__(self, *args: Any, **kwds: Any) -> Any:" where 

*args: Any, **kwds: Any: 
This part of the function signature defines two parameter lists:

*args is a tuple that collects any positional 
arguments passed to the function. 
The * symbol indicates that any number 
of positional arguments can be accepted.

**kwds is a dictionary that collects 
any keyword arguments passed to the function.
The ** symbol indicates that any number of 
keyword arguments can be accepted.

-> Any: This part of the function signature 
indicates the return type of the function. 
In this case, Any means that the function 
can return any type of data.

pass: This line is a placeholder statement 
that does nothing. It's often used when 
you want to define a function or method 
without implementing its behavior yet.

'''