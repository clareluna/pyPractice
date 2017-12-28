#with statement allows you to manipulate file 
#without having to close it at the end

with open('example.txt', 'w+') as file:
    print(file)
    content=file.readlines()
    print(content)

    for line in content:
        print(line)
        if 'christmas' in line:
            file.write('\n')
        else:
            file.write(line)

    file.seek(0)

    print(file.read())            