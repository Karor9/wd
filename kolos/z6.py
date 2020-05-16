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
        t[k][k] = 0
    print("Tablica po zmianie")
    for i in range(0, 10):
        print(t[i])

tablica()
