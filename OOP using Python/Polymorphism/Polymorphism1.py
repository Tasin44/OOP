'''
The word polymorphism means having many forms. 
In programming,polymorphism means the same function name (but different signatures) 
being used for different types. 
The key difference is the data types and number of arguments used in function.
'''
#Example-1: inbuilt polymorphic functions:

# len() being used for a string
print(len("geeks"))#len 5

# len() being used for a list
print(len([10, 20, 30]))#len 3


#Examples 2: user-defined polymorphic functions: 

def add(x, y, z = 0): 
    return x + y+z

# Driver code 
print(add(7, 3))
print(add(2, 3, 11))


