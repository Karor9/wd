import itertools as it

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kombinacje = list(it.combinations(liczby,3))
print(kombinacje[0])
print(kombinacje[1])
print(kombinacje[12])
print(kombinacje[4])
print(kombinacje[53])
