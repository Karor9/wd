import math as m
def suma(a=1, r=1, ile=10 ):
    return sum(wyraz*r+a for wyraz in range (ile))

print(suma(8, 55, 3))
print(suma(2, 5))