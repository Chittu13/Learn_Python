# Basic program of lambda function

## lambda function using map

### Multiplying the two lists

```python
x = [2, 3, 45, 1]
y = [2, 3, 4, 4]
a = map(lambda a, b: a*b, x, y)
print(list(a))
```


### Adding +1 to the list of numbers

```python
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
x = map(lambda a: a+1, y)
print(list(x))
```


### Program for squareing of the numbers using map lambda function

```python
x = input("Enter the numbers separated by (comma): ")
x = list(int(i) for i in x.split(','))
a = list(map(lambda f: f**2, x))
print(a)
```

# lambda function using filter

### program for checking even numbers using lambda filter function

```python
x=[2,3,42,1,1,0,4]
y=filter(lambda n:n%2==0, x)
print(list(y))
```

### program for checking even numbers greater than '2'  using lambda filter function

```python
x=[1,2,3,4,5,6,7,8,9]
y=filter(lambda a: (a%2==0)and a>2  ,x )
print(list(y))
```
