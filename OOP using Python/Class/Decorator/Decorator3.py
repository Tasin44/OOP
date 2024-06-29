
#Question:find out the execution time of a function using a decorator.

# importing libraries
import time
import math

# decorator to calculate duration taken by any function.
#Decorator Definition:
def calculate_time(factoria):
    
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()
        
        factoria(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", factoria.__name__, end - begin)

    return inner1

#Decorator Application:
@calculate_time
def factorial(num):

# sleep 2 seconds because it takes very less time so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)

'''
1.
import time: The time module is used to measure the time taken by a function to execute.
import math: The math module here is used to calculate the factorial of a number.

2.
calculate_time function:This function takes another function func as an argument.

3.
Define inner1 function:
(i)inner1 accepts any number of positional (*args) and keyword arguments (**kwargs).
(ii)begin = time.time() record the current time before the execution of the factorial function.
(iii)func(*args, **kwargs) calls the original function func with the provided arguments.
(iv)end = time.time() stores the current time after the execution of func.
(v)print("Total time taken in : ", func.__name__, end - begin) calculates and 
prints the total time taken by func to execute.
(vi)func.__name__:
In Python, func.__name__ is an attribute that gives the name of the function as a string. 

4.Return inner1 from calculate_time:
The inner1 function is returned, effectively wrapping the original function func.

5.Decorator Application:
The @calculate_time decorator is applied to the factorial function.
This is equivalent to writing factorial = calculate_time(factorial).
The factorial function now has the additional behavior defined in inner1 
(timing of the function execution).

6.When factorial(10) is called, it actually calls the inner1 function 
defined inside the calculate_time decorator.

'''