import numpy as np

a = np.arange(0.2, 6, 0.3, dtype="float")
print(a)
a.as(int)
print(a)