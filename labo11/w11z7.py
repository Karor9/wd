import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Ustawiamy seed by za każdym razem wyglądało identycznie
np.random.seed( 4040914 )


def randrange(n, min, max):
    return (max - min)*np.random.rand(n) + min


fig = plt.figure()
ax = fig.gca( projection = '3d' )

n = 20

x = randrange(n, 12 , 32 )
y = randrange(n, 0 , 100 )
z = randrange(n, 0, 0)

ax.scatter(x, y, z, color ='red', marker ='o')

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )

x = np.linspace( 12 , 32 , 5 )
y = randrange(5, 0, 20)
ax.plot(x, y, zs = 0 , zdir = 'z', color="green")

plt.show()