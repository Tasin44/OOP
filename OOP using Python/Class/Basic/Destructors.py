
#To know more:https://www.geeksforgeeks.org/destructors-in-python/

'''
Syntax of destructor declaration : 
 
def __del__(self):
  # body of destructor
'''
#ex:1
class Employee:
      def __init__(self):
         print('Employee created')
      def __del__(self):
         print('Destructor called, Employee deleted.')

obj= Employee()
del obj

'''
Note : The destructor was called after the program ended or when all the 
references to object are deleted i.e when the reference count becomes zero, 
not when object went out of scope
'''


#EX:2

# Python program to illustrate destructor
#This example gives the explanation of above-mentioned note. 
class Employee:

	# Initializing
	def __init__(self):
		print('Employee created')

	# Calling destructor
	def __del__(self):
		print("Destructor called")

def Create_obj():
	print('Making Object...')
	obj = Employee()
	print('function end...')
	return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

'''
Output

Calling Create_obj() function...
Making Object...
Employee created
function end...
Program End...
Destructor called

Here, notice that the destructor is called after the ‘Program End…’ printed.
'''






