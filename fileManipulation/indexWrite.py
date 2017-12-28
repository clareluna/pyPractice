#w opens an existing file or creates a new one, writes only
#w+ same as above, also reads
file=open('tests.txt', 'w+')

file.write('Manipulated again and again (and again)!')
#reset cursor
file.seek(0)

print(file.read())

file.close()

