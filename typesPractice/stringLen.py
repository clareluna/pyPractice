def length(str):
    if type(str) == int or type(str) == float:
        return "Sorry integers and floats do not have string length"
    else:
        return len(str)

print(length("My dogs' names are Dexter and Tucker"))
print(length("Dexter"))
print(length("Tucker Pants"))
print(length(10.0))
print(length(100))