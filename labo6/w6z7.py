import numpy as numpy

def diag(n):
    d1 = numpy.ones((n,n))
    d2 = numpy.ones((n, n))
    d = d1 + d2
    for x in range(0, n):
        for y in range(0, n):
            pomoc = abs(x-y)
            if x != y:
                d[x][y] += (2 * pomoc)
    return d

a = diag(3)
print(a)

a = diag(6)
print(a)