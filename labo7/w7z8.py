import numpy as numpy

def rzad(tab):
    size = int(tab.size**(1/2))
    for a in tab:
        print(a, end=' ')

t = numpy.array([[5, 3, 6], [2, 5, 1], [2, 4, 7]])

rzad(t)
