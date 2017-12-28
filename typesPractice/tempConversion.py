def c_to_f(deg):
    return deg*(9/5)+32

def f_to_c(deg): 
    return deg*(5/9)-32

temps = [10, -1, 20, 100]

for temp in temps:
    print(c_to_f(temp))
#print(c_to_f(20))
#print(c_to_f(2))
#print(c_to_f(10))
#print(c_to_f(100))
#print(f_to_c(32))
#print(f_to_c(0))
#print(f_to_c(100))
