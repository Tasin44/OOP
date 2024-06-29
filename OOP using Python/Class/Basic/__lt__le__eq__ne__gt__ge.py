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
        

        