
# Define a function named create_adder that takes a parameter x
def create_adder(x):
    def adder(y):# Define a nested function named adder that takes a parameter y
        return x+y
    return adder

# Call create_adder with argument 15, which returns a new function that adds 15 to its argument
add_15=create_adder(15)

# Call the function returned by create_adder(15) with argument 10 and print the result
print(add_15(10))

'''
simply , when I call add_15=create_adder(15), 
the add_15 contains the "return adder" function results, which is 15+y, 
then when I call add_15(10) , it consider the value of y as 10 , 
'''

'''
Defining the nested adder function:

    Inside create_adder, another function named adder is defined. This nested function takes one parameter y.
    adder(y) simply returns the sum of x (the parameter of create_adder) and y (the parameter of adder).

Returning a function:

    The create_adder function returns the adder function itself (without calling it). This means create_adder returns a function object that can be called later.

Assigning and using the returned function:

    add_15 = create_adder(15) calls create_adder with 15 as the argument. This assigns the returned adder function (with x set to 15) to the variable add_15.

Calling the returned function:

    print(add_15(10)) calls the function stored in add_15, passing 10 as an argument (y). This results in 15 + 10, which equals 25.
'''
