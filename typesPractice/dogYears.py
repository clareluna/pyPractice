def dog_years(age):
    dog_age = age*7
    if dog_age > 49:
        return "You are an old sage in dog years: " + str(dog_age)
    elif dog_age == 49:
        return "You are a prime pooch at " + str(dog_age) + " dog years old!"
    else:
        return "You are a puppy in dog years: " + str(dog_age)    

age = float(input("Please enter your age: "))

print(dog_years(age))