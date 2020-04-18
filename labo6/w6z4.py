import numpy as np

def generuj(l, p):
    t = np.logspace(1, p, base=l, num=p, dtype='int64')
    return t


a = generuj(2, 4)
print(a)