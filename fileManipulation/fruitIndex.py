file=open('fruits.txt', 'r')
content=file.readlines()

#remove linebreak from text
content=[i.rstrip('\n') for i in content]

for line in content:
    print(len(line))
file.close()
