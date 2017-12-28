code=''
attempts = 3
while code != 'codeCODE' and attempts > 0:
    code=input("Please enter the code: ")
    if code == 'codeCODE':
        print("Success")
    else:
        attempts = attempts - 1
        print("Incorrect, please try again, you have " + str(attempts) + " attempt(s) left")    