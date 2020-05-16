import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 20, 20)
print(x)
fig, ax = plt.subplots()
plt.plot(x, x**-1, 'g--')
plt.plot(x, x**-1, 'g^')
plt.title("wykres x  F(x)")
plt.xlabel('f(x)')
plt.ylabel('x')
ax.plot(20,1)
ax.annotate('Max Value',
            xy=(1, 1),
            xycoords='data',
            xytext=(10, 1),
            arrowprops=
                dict(facecolor='black', shrink=0.05),
                horizontalalignment='left',
                verticalalignment='top')


plt.show()