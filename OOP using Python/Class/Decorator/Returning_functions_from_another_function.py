
# Define a function named create_adder that takes a parameter x
def create_adder(x):
    def adder(y):# Define a nested function named adder that takes a parameter y
        return x+y
    return adder

# Call create_adder with argument 15, which returns a new function that adds 15 to its argument
add_15=create_adder(15)

# Call the function returned by create_adder(15) with argument 10 and 15 and print the result

print(add_15(10))  # Output: 25
print(add_15(10))  # Output: 25
print(add_15(20))  # Output: 35

'''
simply , when I call add_15=create_adder(15), 
the add_15 contains the "return adder" function results, which is 15+y, 
then when I call add_15(10) , it consider the value of y as 10 , 
'''
'''
❓ Your confusion:
You're wondering why the second print(add_15(10)) gives 25 again, and not something like 35, as if it's accumulating or storing the result somehow.

✅ Answer:

Each call to add_15(y) just adds 15 to whatever you pass in as y. 
    There is no memory of past calls. The function doesn’t increment or remember previous values. Here's what’s happening:

    create_adder(15) creates a closure: a function adder(y) that captures the variable x = 15.

    add_15 is now a function that takes a number y and returns 15 + y.

    So:

        add_15(10) → 15 + 10 = 25

        add_15(10) again → 15 + 10 = 25 (not remembered, just recomputed)

        add_15(20) → 15 + 20 = 35

There’s no state being stored inside the function—only the variable x = 15 is "remembered", not the previous result.

'''
================================================================================================================================================================

def create_counter_adder(x):
    total = 0
    def adder(y):
        nonlocal total
        total += x + y
        return total
    return adder

counter_add_15 = create_counter_adder(15)

print(counter_add_15(10))  # 25
print(counter_add_15(10))  # 25+15+10=50
print(counter_add_15(20))  # 50+15+20=85


'''
❌ If you remove nonlocal, like this:

def create_counter_adder(x):
    total = 0
    def adder(y):
        total += x + y   # ERROR here
        return total
    return adder

You’ll get:
UnboundLocalError: local variable 'total' referenced before assignment
'''

'''
🧠 Why this happens:

In Python, if you assign a value to a variable inside a function, Python assumes it's a local variable, unless you explicitly tell it otherwise using nonlocal or global.

So in this line:

        total += x + y

Python interprets it as:

        total = total + x + y

It tries to find a local variable total, but it doesn't exist yet (because total = 0 is in the enclosing scope, not the local one), so it raises an error.
✅ What nonlocal does:

nonlocal total tells Python:

    “Hey, I want to use the total variable from the nearest enclosing scope that is not global.”

So it accesses the total defined in the enclosing create_counter_adder function—not creating a new local total, but modifying the existing one.

'''
