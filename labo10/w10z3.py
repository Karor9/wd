import math as m
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 30, 301)
sin = [m.sin(k) for k in x]
cos = [m.cos(k) for k in x]

plt.plot(x, sin, label='sin(x)')
plt.plot(x, cos, label='cos(x)')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')

plt.show()