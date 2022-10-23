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
