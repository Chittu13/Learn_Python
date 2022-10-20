
# I have created a txt file named (ge.txt) & some txt is present 


"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

txt=open("ge.txt",'r') 
print(txt.read())
txt.close()

txt=open("ge.txt",'r') 
print(txt.readline())             # It will read the first line contant


txt=open("ge.txt",'r')
for x in txt:
    print(x)



"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content


f=open("ge.txt",'a')
f.write("\nhello mother fucker:)")
f.close()

f=open("ge.txt",'r')
for x in f:
    print(x)
f.close()



"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist


f=open("hah.txt",'x')
f=open("hah.txt",'a')
f.write("Hello mother fucker haha:) ")
f.close()
f=open("hah.txt",'r')
print(f.read())