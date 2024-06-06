import math 
n = int(input('>'))
r = int(input('>'))

def func(a) :
    return math.factorial(a)

ncr = func(n)/(func(r)*func(n-r))
print(ncr%1000003)
    