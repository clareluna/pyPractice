names=['tony', 'dexter', 'tucker', 'clare']

for name in names:
    if 't' in name:   
        print(name)
    else:
        print('sorry ' + name)    


#Iterate through multiple lists at once

humans = [True, False, False, True]

for name,human in zip(names, humans):
    typeof='human'
    if not human:
        typeof = 'dog'
    print(name + " is a " + typeof)        