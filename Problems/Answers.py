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
