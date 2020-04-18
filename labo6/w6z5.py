import numpy as numpy

def diag(n):
    t = numpy.arange(n, 0, -1)
    d = numpy.zeros((n, n))
    for i in range(0, n):
        d[i][i] = t[i]
    return d

a = diag(3)
print(a)