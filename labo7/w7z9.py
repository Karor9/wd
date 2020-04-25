import numpy as numpy

def plaski(tab):
    size = tab.size
    tt = tab.ravel()
    for i in range(0, size):
        print(tt[i], end=', ')

t = numpy.array([[5, 3, 6], [2, 5, 1], [2, 4, 7]])

plaski(t)
