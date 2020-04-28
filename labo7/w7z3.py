import numpy as numpy

a = numpy.array ([1, 2, 3])
b = numpy.array ([4, 3, 1])

b = numpy.reshape(b, (3,1))

print(numpy.dot(a,b))
