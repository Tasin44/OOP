'''
The below code shows how Python can use two different class types, in the same way.
We create a for loop that iterates through a tuple of objects. 
Then call the methods without being concerned about which class type each object is.
We assume that these methods actually exist in each class. 
'''

class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

'''
Output

New Delhi is the capital of India.
Hindi is the most widely spoken language of India.
India is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.

'''

#Ex-2
class Student(object):
    def name(self):
        print("Student name is Tasin")
    def age(self):
        print("Student age 24")
    def weight(self):
        print("Student weight is 67")
    
class Teacher(object):
    def name(self):
        print("Teacher name is Abdur Rahim")
    def age(self):
        print("Teacher age 50")
    def weight(self):
        print("Teacher weight 80")



obj=Student()
obj2=Teacher()

for i in (obj,obj2):
    i.name()
    i.age()
    i.weight()