import math as m
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 30, 301)
sing = [m.sin(k)+2 for k in x]
sind = [m.sin(k)*-1 for k in x]

plt.plot(x, sing, label='sin(x)')
plt.plot(x, sind, label='sin(x)')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')

plt.show()