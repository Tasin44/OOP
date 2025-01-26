class Student:
    all_students = {}  # Class-level dictionary to store all students

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        Student.all_students[student_id]=self  # # Add to class-level dictionary

    @classmethod
    def find_student(self, student_id):
        if student_id in self.all_students:
                stdobj = self.all_students[student_id]
                print(f"Found: {stdobj.name} with ID {stdobj.student_id}")
                return
        print(f"No student found with ID {student_id}")

# Create students
student1 = Student("Alice", 101)
student2 = Student("Bob", 102)

# Search for a student
Student.find_student(102)  # Output: Found: Bob with ID 102
Student.find_student(103)  # Output: No student found with ID 103

'''
Why Use a Class-Level Dictionary?

    Fast Access:
        You can directly access an object using its key without looping through all items.
    Centralized Data:
        All instances can share and access the same data.
    Automatic Updates:
        Every time an object is added, it's stored in a shared location.

'''

