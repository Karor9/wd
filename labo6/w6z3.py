import numpy as np

def funk(n):
    tb = np.zeros(shape=(n, n))
    for i in range(0, n):
        t = np.arange(1+(n*i), n*(i+1)+1, 1)
        tb[i] = t
    return tb      

a = funk(6)
print(a)