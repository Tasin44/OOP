
'''
Why Use a Class-Level List?

    Centralized Storage:
        All instances of the class can share and contribute to a common list.
        Useful for tracking or searching through all objects of the class without relying on external data structures.

    Easier Management:
        You can easily add, remove, or search for instances without needing to keep track of each one manually.

    Shared Across Instances:
        The list is not specific to one instance. All objects of the class have access to it.
'''

          
'''with class-level list'''

# Example -1 

class Student:
    all_students = []  # Class-level list to store all students

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        #reason behind using self explained below
        Student.all_students.append(self)  # Automatically add to class-level list

    @classmethod
    def find_student(self, student_id):
        for student in self.all_students:
            if student.student_id == student_id:
                print(f"Found: {student.name} with ID {student.student_id}")
                return
        print(f"No student found with ID {student_id}")

# Create students
student1 = Student("Alice", 101)
student2 = Student("Bob", 102)

# Search for a student
Student.find_student(102)  # Output: Found: Bob with ID 102
Student.find_student(103)  # Output: No student found with ID 103


'''
Why Student.all_students.append(self) and not Student.all_students.append(self.name) or self.student_id?
✅ Reason:

Because you're trying to store the entire student object, not just a single attribute like their name or ID.

Student.all_students.append(self)

Here, self refers to the current instance of the Student class (i.e., an object like student1, student2, etc.). 
By appending self, you're saving the full object with all its attributes (name, student_id, and any future attributes).

🔍 What happens if you did this?

    Student.all_students.append(self.name)
    → You’d only store names (["Alice", "Bob"]), and you couldn't search by student_id later.

    Student.all_students.append(self.student_id)
    → You’d only store IDs ([101, 102]), and you'd lose the name info.

✅ By storing the whole object (self), you can:

    Access student.name

    Access student.student_id

    Extend later with more attributes (like age, grade, etc.)

Bonus: When you're iterating in find_student():

for student in self.all_students:
    if student.student_id == student_id:

This only works because student here is a full object, not just an ID or name. That’s why .student_id works!
'''



# =================================================================================================================================================================================

# Example -2 

class Employee:
  list_of_emp=[]
  
  def __init__(self,name,emp_id):
    self.name=name.lower() # Store name in lowercase
    self.emp_id=emp_id
    Employee.list_of_emp.append(self)
  
  @classmethod
  def find_emp(self,emp_name):
    # emp_name=emp_name.lower()# Convert search input to lowercase
    for emp in self.list_of_emp:
      if emp.name==emp_name.lower():# Convert search input to lowercase during search
        print(f"Employee found with named search {emp_name} whose id {emp.emp_id}")
        return
    print(f"No Employee found with the name {emp_name}")
  
emp1=Employee("Akram",20062)
emp2=Employee("Khan",20073)

# Example usage
emp1 = Employee("Akram", 20062)
emp2 = Employee("Khan", 20073)

Employee.find_emp("Akram")   # Should find
Employee.find_emp("akram")   # Should also find
Employee.find_emp("AKRAM")   # Should also find
Employee.find_emp("John")    # Should not find




# =================================================================================================================================================================================

'''without class level list '''

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

# You'd need an external list to store all students
all_students = []

# Create students
student1 = Student("Alice", 101)
student2 = Student("Bob", 102)

# Manually add them to the list
all_students.append(student1)
all_students.append(student2)

# Search for a student
search_id = 102
for student in all_students:
    if student.student_id == search_id:
        print(f"Found: {student.name} with ID {student.student_id}")


