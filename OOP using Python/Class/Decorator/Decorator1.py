
'''
A decorator is a function that takes another function 
as an argument and returns a new function, 
usually adding some functionality to the original 
function without modifying its code directly.

in this code, 
wrapper_function serves as a decorator that decorates
original_function by adding extra functionality to it.
'''

def wrapper_function(func):#step 2
    def inner_function():#step 3
        print("Before calling the function")
        func()  # Call the original function
        print("After calling the function")
    return inner_function#step 4

def original_function():
    print("This is the original function")

# Wrap the original function with the wrapper function
wrapped_function=wrapper_function(original_function)#step 1

'''
We wrap the original_function with the wrapper_function 
by assigning the result of wrapper_function(original_function) to wrapped_function.
'''
# Call the wrapped function
wrapped_function()#step 5

'''
print(wrapper_function(original_function)) 

If i want to print like 
(wrapper_function(original_function))
that means printing the result of
calling wrapper_function(original_function) directly.
However, wrapper_function(original_function) returns the inner_function, 
not the result of calling the inner_function. 
Therefore, when you print wrapper_function(original_function),
means you're printing the reference of the inner_function, 
not executing it.
'''