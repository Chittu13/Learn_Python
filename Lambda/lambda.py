# Basic of lambda function 

x=input("Enter the number you want to squre the number: ")
x=list(int(i) for i in x.split(','))
a=list(map(lambda f:f**2, x ))
print(a)


x= lambda a,b: a+b
print(x(2,3))

