import numpy as numpy

def diag():
    a = numpy.arange(25)
    w1 = 0
    w2 = 1
    a[0] = w1
    a[1] = w2
    for x in range(2, 25):
        a[x] = w1+w2
        w1 = w2
        w2 = a[x]
    a = a.reshape((5,5))
    return a

a = diag()
print(a)