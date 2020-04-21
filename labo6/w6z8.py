import numpy as numpy

def diag(a, par):
    y = int(numpy.size(a, 0)) #poziomo
    x = int(numpy.size(a, 1)) #pionowo
    if (x%2 == 1 and par < 0) or (y%2 == 1 and par >= 0):
        print("Dzielenie niemożliwe")
        return a
    if par >= 0:
        splitY = int(y/2)
        s = numpy.zeros((splitY, x))
        for i in range(0, splitY):
            for j in range(0, x):
                s[i][j] = a[i][j]
        return s
    if par < 0:
        splitX = int(x/2)
        s = numpy.zeros((y, splitX))
        for i in range(0, y):
            for j in range(0, splitX):
                s[i][j] = a[i][j]
        return s
    return a

a = ([1, 2, 3], [1, 2, 3])
b = ([1, 32, 3, 4, 33, 4], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
print(diag(a, 1)) # >=0 poziome, <0 pionowe
print(diag(b, -1))