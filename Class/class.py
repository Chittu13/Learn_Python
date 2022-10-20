
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
        
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)
    
    def __mul__(self, other):
        return Point(self.x*other.x,self.y*other.y)
        
    def __div__(self, other):
        return Point(self.x/other.x,self.y/other.y)


p=Point(5,2)
x=Point(1,2)
a=p+x
print(f"{a.x},{a.y}")
b=p-x
print(f"{b.x},{b.y}")
c=p*x
print(f"{c.x},{c.y}")
d=p/x
print(f"{d.x},{d.y}")
