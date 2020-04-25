import numpy as numpy

a = numpy.arange(81)
b = numpy.reshape(a, (9, 9))
c = numpy.reshape(a, (3, 27))
d = numpy.reshape(a, (27, 3))
#musi mieć tyle samo elementów
print(b)
print(c)
print(d)