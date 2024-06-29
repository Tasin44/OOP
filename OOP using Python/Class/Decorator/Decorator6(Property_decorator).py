#Getter, Setter, and Deleter
#source:https://youtu.be/d2m07ENg-tA?feature=shared
#also,read this blog:https://www.geeksforgeeks.org/getter-and-setter-in-python/

#STEP:1
class Person:
    def __init__(self,first,last,address):
        self.first=first
        self.last=last
        self.address=address
        self.email=self.first+'.'+self.last+'@gmail.com'

    def full_name(self):
        return self.first+' '+self.last

per=Person('Sam','Edison','BD')

print(per.full_name())
print(per.email)




#STEP:2
class Person:
    def __init__(self,first,last,address):
        self.first=first
        self.last=last
        self.address=address
        self.email=self.first+'.'+self.last+'@gmail.com'

    def full_name(self):
        return self.first+' '+self.last

per=Person('Sam','Edison','BD')

print(per.full_name())
print(per.email)
per.first='Samuel'
print(per.full_name())
#full_name is a method,so if we change any variable of person class,
# it'll show impact on the full_name 
print(per.email)
#but the email won't change because email still inside my init method,so no change will occur

#So if we want to change the email too,


#STEP:3
class Person:
    def __init__(self,first,last,address):
        self.first=first
        self.last=last
        self.address=address

    def full_name(self):
        return self.first+' '+self.last

    def email(self):
        return self.first+self.last+'@gmail.com'

per=Person('Sam','Edison','BD')

print(per.full_name())
print(per.email)
per.first='Samuel'
print(per.full_name())
print(per.email())
#now my email will change if I change any first or last name,
#because now email is a method


#STEP:4
#using property decorator,it's also called 
#Getter method

class Person:
    def __init__(self,first,last,address):
        self.first=first
        self.last=last
        self.address=address
    @property
    def full_name(self):
        return self.first+' '+self.last
    @property
    def email(self):
        return self.first+self.last+'@gmail.com'

per=Person('Sam','Edison','BD')

print(per.full_name)
print(per.email)
per.first='Samueel'
print(per.full_name)#even if it's a method,by using property decorator,we can use them as variable 
print(per.email)##even if it's a method,by using property decorator,we can use them as variable 
'''
now full_name and email are method who are pass as argument to their own property decorator,
from decorator they internally call the full_name & email method 
& the value'll be returned below(full_name,email).
If I do it without the property decorator method,it'll only print the reference 
'''



#STEP:5 setter method
'''
#first read this code & try to understand then go below
class Person:
    def __init__(self,first,last,address):
        self.first=first
        self.last=last
        self.address=address
    @property
    def full_name(self):
        return self.first+' '+self.last
    @property
    def email(self):
        return self.first+self.last+'@gmail.com'

per=Person('Sam','Edison','BD')

print(per.full_name)
print(per.email)
per.full_name='tomas alva'#we can't do this change like this because full_name is a method,we can't
                        #set value to method,we can set value to an attribute 
print(per.full_name)
print(per.email)
'''
'''
if we try to change or initialize to a method,it won't happen directly,
Sothat we need to use setter method 
'''

#so if we want to change fullname,we'll use setter method

class Person:
    def __init__(self,first,last,address):
        self.first=first
        self.last=last
        self.address=address
    @property
    def fullname(self):
        return self.first+' '+self.last

    @fullname.setter
    def fullname(self,name):
        self.first,self.last=name.split()
        #here self.first will be stored as tomas,
        #self.last will be stored as alva 
    

per=Person('Sam','Edison','BD')

per.fullname='tomas alva'
print(per.fullname)#if we don't use property before setter ,we can't call fullname as a variable 

'''
@fullname.setter to create the setter method.
This allows fullname to be set directly, splitting the input string into first and last names.
'''


#STEP:6 DELETE
'''
class Person:
    def __init__(self,first,last,address):
        self.first=first
        self.last=last
        self.address=address
    @property
    def fullname(self):
        return self.first+' '+self.last

    @fullname.setter
    def fullname(self,name):
        self.first,self.last=name.split()
    

per=Person('Sam','Edison','BD')

per.fullname='tomas alva'
print(per.fullname)
del per.fullname
#now we can't delete a method in this way,we can delete attribute like first,second this way

del per.first
print(per.first)#it'll return 'Person' object has no attribute 'first',that means first deleted
'''

#using deleter
class Person:
    def __init__(self,first,last,address):
        self.first=first
        self.last=last
        self.address=address
    @property
    def fullname(self):
        return self.first+' '+self.last

    @fullname.setter
    def fullname(self,name):
        self.first,self.last=name.split()
    @fullname.deleter
    def fullname(self):
        self.first=None
        self.last=None
        print('Full name deleted...')

per=Person('Sam','Edison','BD')

per.fullname='tomas alva'
print(per.fullname)
del per.fullname
print(per.first)
print(per.last)





