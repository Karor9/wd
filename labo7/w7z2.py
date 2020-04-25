import numpy as numpy

def min(tab):
    #przejazd po macierzy
    size = int(tab.size**(1/2))
    w = numpy.arange(size)
    k = numpy.arange(size)
    for i in range(0, size):
        w[i] = tab[i][0]
        k[i] = tab[0][i]
        for j in range (0, size):
            if w[i] > tab[i][j]:
                w[i] = tab[i][j]
            if k[i] > tab[j][i]:
                k[i] = tab[j][i]
    print(w)
    print(k)
        


t = numpy.array([[5, 3, 6], [2, 5, 1], [2, 4, 7]])
c = numpy.array([[62, 23, 146, 22], [52, 27, 12, 6], [326, 25, 37, 89], [25432, 235, 32, 22]])
min(t)
min(c)