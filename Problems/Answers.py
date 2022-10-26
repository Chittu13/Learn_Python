# 1. write a program to find most repected characters in a string

string = input("Enter the string: ")  # Input form the user
Empty = {}                            # First we need to take empty dictionary
for i in string:
    if i in Empty:                    # Checking the character in the Empty set is there are not
        Empty[i] += 1
    else:
        Empty[i] = 1

orginal = sorted(Empty.items(), key=lambda Empty: Empty[1], reverse=True)
print(f' Most Repected Character: {orginal[0][0]} ---> {orginal[0][1]}')


# 2. Write a program to find the square root of number using lambda with any code crash


try:
    user = input("Enter the numbers separated by (comma): ")
    user = list(int(i) for i in user.split(','))
    a = list(map(lambda f: f**2, user))
    print(f"squre root of {user} is {a}")
except ValueError:
    print("only numerical, No space:( between numbers use only only comma")



# Write a program, multiple of 3 print "Fizz", multiple of 5 print "Buzz" and both 3&5 multiple prints "FizzBuzz" 

def fizz(x):
    if x%3==0 and x%5==0:
        return "FizzBuzz"
    elif x%3==0:
        return "Fizz"
    elif x%5==0:
        return "Buzz"
    else:
        return x
y=int(input("Enter the number:) "))
print(fizz(y))



# write number that print even number from a range and finally print how many even numbers you got


x=int(input("Enter the first range of number: "))
y=int(input("Enter the second range of number: "))
count=0
store=[]
for i in range(x,y+1):
    if i%2==0:
        store.append(i)
        count+=1
print(f"Number of even numbers: {store}")
print(f"The total number of even numbers is {count}")

