import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 20, 20)

plt.plot(x, 1/x, label='Funkcja 1/x')

plt.xlabel('x')
plt.ylabel('f(x)')

plt.legend()
plt.show()