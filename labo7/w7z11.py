import numpy as numpy

a = numpy.arange(12)
b = numpy.reshape(a, (3, 4))
c = numpy.reshape(a, (4, 3))
d = numpy.reshape(a, (2, 6))
bp = b.ravel()
cp = c.ravel()
dp = d.ravel()
print(b)
print(c)
print(d)
print(bp)
print(cp)
print(dp)

#tak