# program for checking even numbers using lambda filter function

x=[2,3,42,1,1,0,4]
y=filter(lambda n:n%2==0, x)
print(list(y))

# program for checking even numbers greater than '2'  using lambda filter function

x=[1,2,3,4,5,6,7,8,9]
y=filter(lambda a: (a%2==0)and a>2  ,x )
print(list(y))