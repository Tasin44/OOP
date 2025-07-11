
#single inheritance example-4

# parent class
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def display(self):
    print(self.name, self.age)
 
# child class
class Student(Person):
  def __init__(self, name, age, dob):
    self.sName = name 
    #here, attribute names must be different from parent class attribute name because here we want to initialize and display different name and age compare to parent class
    self.sAge = age
    self.dob = dob
    # inheriting the properties of parent class
    super().__init__("Rahul", age)
 
  def displayInfo(self):
    print(self.sName, self.sAge, self.dob)
 
obj = Student("Mayank", 23, "16-03-2000")
obj.display()
obj.displayInfo()



# Output:
# Rahul 23
# Mayank 23 16-03-2000



