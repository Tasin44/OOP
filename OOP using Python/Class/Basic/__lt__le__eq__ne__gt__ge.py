class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # They are all boolean method
    def __lt__(self,other):
        return(self.x,self.y)<(other.x,other.y)
    def __le__(self,other):
        return(self.x,self.y)<=(other.x,other.y)
    def __eq__(self,other):
        return(self.x,self.y)==(other.x,other.y)
    def __ne__(self,other):
        return(self.x,self.y)!=(other.x,other.y)
    def __gt__(self,other):
        return(self.x,self.y)>(other.x,other.y) 
    def __ge__(self,other):
        return(self.x,self.y)>=(other.x,other.y)

point1=Point(5,2)
point2=Point(3,4)


print("point1 < point2:", point1 < point2)
print("point1 <= point2:", point1 <= point2)
print("point1 == point2:", point1 == point2)
print("point1 != point2:", point1 != point2)
print("point1 > point2:", point1 > point2)
print("point1 >= point2:", point1 >= point2)

'''
in lexicographical order, (5, 2) is greater than (3, 4) because 5 > 3.
Therefore, point1 > point2 evaluates to True.
'''

#if we want to compare by user defined function
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def greater(self,other):
        return (self.x,self.y)>(other.x,other.y)

point1=Point(5,2)
point2=Point(8,9)
point3=Point(1,3)

print("point2 > point1", point1.greater(point2))

print("point2 > point1 and point1>point3 and point2<point3:", point1.greater(point2),point1.greater(point3),point3.greater(point2))
        
print("point2 > point1 and point1>point3 and point2<point3:", point2.greater(point1),point2.greater(point3),point2.greater(point1))
        
