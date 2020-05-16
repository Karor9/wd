import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as r


b = []

def rzucKostka(n):

    for i in range(n):
        c =r.randrange(1,7,1)
        a =r.randrange(1,7,1)
        b.append(int(a+c))

n = 100
rzucKostka(n)
plt.hist(b, bins=11, facecolor='g', density=True)


plt.xlabel('Sumy')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram sumy rzutów')  
plt.grid(True)
plt.show()