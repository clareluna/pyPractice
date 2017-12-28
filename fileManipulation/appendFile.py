#a opens existing file with cursor at end of file
#a+ opens existing file, if not found creates new file, cursor at end of file

file=open('fruits.txt', 'a+')

file.write("\nadded to the end")

file.seek(0)

print(file.read())

file.close()