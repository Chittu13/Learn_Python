class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __eq__(self,other):                                     # eq   equal to (==)
        return self.x==other.x and self.y==other.y              # ne   not equal to (!=)
                                                                # lt   less then (<)
    def __gt__(self,other):                                     # gt   grater then (>)
        return self.x>other.x and self.y>other.y                # le   less then equal to (>=)
                                                                # ge   grater then equal to (<=)
    
    def __le__(self,other):
        return self.x<=other.x and self.y<=other.y
    
        
        

p=Point(1,2)
x=Point(1,2)
print(p==x)
print(p<x)
print(p<=x)