# Multiplying the two lists

x = [2, 3, 45, 1]
y = [2, 3, 4, 4]
a = map(lambda a, b: a*b, x, y)
print(list(a))


# Adding +1 to the list of numbers

y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
x = map(lambda a: a+1, y)
print(list(x))


# Program for squareing of the numbers using map lambda function

x = input("Enter the numbers separated by (comma): ")
x = list(int(i) for i in x.split(','))
a = list(map(lambda f: f**2, x))
print(a)
