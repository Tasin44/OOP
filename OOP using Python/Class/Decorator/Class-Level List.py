
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

class Student:
    all_students = []  # Class-level list to store all students

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        Student.all_students.append(self)  # Automatically add to class-level list

    @classmethod
    def find_student(cls, student_id):
        for student in cls.all_students:
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











