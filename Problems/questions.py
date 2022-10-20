1. write a program to find most repected characters in a string   

st=input("Enter the string: ")  #Input form the user
x={}  #First we need to take empty dictionary
for i in st:
    if i in x:
        x[i]+=1
    else:
        x[i]=1

y=sorted(x.items(),key=lambda x:x[1],reverse=True)
print(y)

try:
  x=int(input("Enter the age: "))
  print(x)
except ValueError:
    print("Enter the correct age")