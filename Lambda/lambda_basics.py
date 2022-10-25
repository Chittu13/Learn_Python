

def add(a, b): return a+b
def sub(a, b): return a-b
def mul(a, b): return a*b
def div(a, b): return a/b


first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
per = input('Enter the operation you want to perform like: "+  -  *  /": ')
if per == "+":
    print(add(first, second))
elif per == "-":
    print(sub(first, second))
elif per == "*":
    print(mul(first, second))
elif per == "/":
    print(div(first, second))
else:
    print("Please enter the right operation :( ")
