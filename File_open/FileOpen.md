# File opening 
# Here i have created a txt file named (name.txt) & some txt is present 

- "r" - Read - Default value. Opens a file for reading, error if the file does not exist

- "a" - Append - Opens a file for appending, creates the file if it does not exist

- "w" - Write - Opens a file for writing, creates the file if it does not exist

- "x" - Create - Creates the specified file, returns an error if the file exists

## Basic file reading code

```python
txt=open("name.txt",'r')         # Opening the file
print(txt.read())                # Reading the contant of the file
txt.close()                      # And closing the file
```

# Use this method, no need to close the file every time.

```python
with open("name.txt",'r') as f:
    for x in f:
        print(x)
```


## To read first line contant

```python
txt=open("name.txt",'r') 
print(txt.readline())           
txt.close()
```


## Using for loop to print the contant line by line

```python
txt=open("name.txt",'r')
for x in txt:
    print(x)
```


# Program to write in a file using Append 
 -  "a" - Append - will append to the end of the file
 -  "w" - Write - will overwrite any existing content

```python
f=open("name.txt",'a')
f.write("\nhello how are you :)")  
f.close()

f=open("name.txt",'r')
for x in f:
    print(x)
f.close()
```



# Program to creat a file and write 

- "x" - Create - will create a file, returns an error if the file exist
- "a" - Append - will append to the end of the file


```python
f=open("create.txt",'x')
f=open("create.txt",'a')
f.write("Hello world:) ")
f.close()
f=open("create.txt",'r')
print(f.read())
```
