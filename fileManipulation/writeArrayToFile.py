#w opens an existing file or creates a new one, writes only
#w+ same as above, also reads

arr = [1,2,3]

file=open('numsArrFile.txt', 'w+')

for i, a in enumerate(arr):
    if i == len(arr) - 1:
        file.write(str(a))
    else:    
        file.write(str(a) + '\n')

file.seek(0)

print(file.read())

file.close()
