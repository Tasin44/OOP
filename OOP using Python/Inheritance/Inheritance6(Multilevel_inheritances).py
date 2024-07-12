
'''
Multilevel inheritance: When we have a child and grandchild relationship. 
This means that a child class will inherit from its parent class, 
which in turn is inheriting from its parent class.
'''

'''
Base or Super class. Note object in bracket.
(Generally, object is made ancestor of all classes)
In Python 3.x "class Person" is equivalent to "class Person(object)"
'''

class Base(object):
	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name


# Inherited or Sub class (It's parent class name in bracket)
class Child(Base):
	# Constructor
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	# To get name
	def getAge(self):
		return self.age


# Inherited or Sub class (It's parent class name in bracket)
class GrandChild(Child):
	# Constructor
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	# To get address
	def getAddress(self):
		return self.address


g = GrandChild("Abdur Rahman", 55 , "Noida")
print(g.getName(), g.getAge(), g.getAddress())
