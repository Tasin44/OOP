#Question: a function returns something or an argument is passed to the function

def hello_decorator(sum_two_numbers):
    def inner1(*args, **kwargs):
        
        print("before Execution")
        
        # getting the returned value
        returned_value = sum_two_numbers(*args, **kwargs)
        print("after Execution")
        
        # returning the value to the original frame
        return returned_value
        
    return inner1#Return the inner1 function from hello_decorator.


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
'''
Apply the hello_decorator to sum_two_numbers using the @hello_decorator syntax. 
This is equivalent to writing sum_two_numbers = hello_decorator(sum_two_numbers).
The sum_two_numbers function is now wrapped by the inner1 
function defined inside hello_decorator.

'''
a, b = 1, 2

# getting the value through return of the function
#Call the decorated(wraped) sum_two_numbers function with a and b as arguments.
print("Sum =", sum_two_numbers(a, b))


