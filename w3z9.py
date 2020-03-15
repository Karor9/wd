
def iloczyn(*liczby ):
    if len(liczby) == 0:
        return 0
    suma=1
    for i in liczby:
        suma*=i
    return suma

print(iloczyn(1,2,3,4, 5, 6, 234))
print(iloczyn())