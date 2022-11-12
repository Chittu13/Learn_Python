# Numeric magic methods in class


```python
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

p=Point(5,2)
x=Point(1,2)
a=p+x
print(f"{a.x},{a.y}")
b=p-x
print(f"{b.x},{b.y}")
c=p*x
print(f"{c.x},{c.y}")
```



# Comparison magic methods in class

- eq    - equal to (==)
- ne    - not equal to (!=)
- lt    - less then (<)
- gt    - grater then (>)
- le    - less then equal to (>=)
- ge    - grater then equal to (<=)



```python
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __eq__(self,other):                                     
        return self.x==other.x and self.y==other.y              
                                                                
    def __gt__(self,other):                                    
        return self.x>other.x and self.y>other.y                
                                                                
    
    def __le__(self,other):
        return self.x<=other.x and self.y<=other.y
p=Point(1,2)
x=Point(1,2)
print(p==x)
print(p<x)
print(p<=x)
```



# Program for adding of two numbers using class 


```python
class Point:
    def __init__(self,x,y):      #This def block is constructor def 
        self.x=x                 #This are instance attributes or This are attributes belong to Point Object 
        self.y=y
    def draw(self):
        return(f'{self.x}+{self.y}={self.x+self.y} ')
p=Point(2,4)
print(p.draw())
```
