import random as r

A = [[r.randint(1,10) for wiersz in range(4)] for kolumna in range(4)]

print(A)

B = [A[i][i] for i in range(4)]
print(B)