# I have created a txt file named (name.txt) & some txt is present 

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

txt=open("name.txt",'r')         # Opening the file
print(txt.read())                # Reading the contant of the file
txt.close()                      # And closing the file

txt=open("name.txt",'r') 
print(txt.readline())             # It will read the first line contant


txt=open("name.txt",'r')
for x in txt:
    print(x)



# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content


f=open("name.txt",'a')
f.write("\nhello how are you :)")  
f.close()

f=open("name.txt",'r')
for x in f:
    print(x)
f.close()

# Or you can this method you no need to close the file 

with open("name.txt",'r') as f:
    for x in f:
        print(x)



# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist


f=open("create.txt",'x')
f=open("create.txt",'a')
f.write("Hello mother fucker haha:) ")
f.close()
f=open("create.txt",'r')
print(f.read())