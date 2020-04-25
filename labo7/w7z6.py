import numpy as numpy
import math as m

def obliczCosinus(tab):
    size = tab.size
    copyTab = tab.ravel()
    copyTab = copyTab.astype('float64')
    result = tab * 0
    result = result.astype('float64')
    for i in range (0, size):
        copyTab[i] = m.cos(copyTab[i])
    result = numpy.reshape(copyTab, (2, 3))
    
    return result

a = numpy.array([[1, 33, 64], [214, 90, 180]])
b = obliczCosinus(a)
print(b)
