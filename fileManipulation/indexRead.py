#r opens file for reading only, cursor at first position in file
#r+ opens existing file for reading and writing

#read a file
file=open('example.txt', 'r')
content=file.read()
print(content)

#reset pointer to top of file
file.seek(0)


#read and remove line break
c1=file.readlines()
c1=[i.rstrip('\n') for i in c1]
print(c1)

file.seek(0)

#close file from python process
file.close()