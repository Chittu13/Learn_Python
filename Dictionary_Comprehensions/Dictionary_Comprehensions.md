# Dictionary_Comprehensions


## Example 1:

```pyton
x=[]
for i in range(5):
    x.append(i*2)
print(x)
```

## Is same as 

```python
x={i*2 for i in range(5)}
print(x) 
```

## Example 2:

```python
y={1:"hello",2:"how",3:"are",4:"you"}

for key in y:
    print(key,y[key])
```

## Is same as

```python
for key in y.items():
    print(key)
print(y)
```
