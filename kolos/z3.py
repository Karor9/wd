import random as r

def tablica():
    t = [ [ None for y in range( 10 ) ] 
             for x in range( 10 ) ] 
    for x in range (0, 10):
        for y in range (0, 10):
            liczba = r.randint(1, 10)
            t[x][y] = liczba
    for i in range(0, 10):
        print(t[i])
    for k in range(0, 10):
        print(t[k][k], end=' ')
    print()
    for k in range(0, 10):
        print(t[9-k][k], end=' ')

tablica()
