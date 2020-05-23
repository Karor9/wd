import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Ustawiamy seed by za każdym razem wyglądało identycznie
np.random.seed( 404080914 )


def randrange(n, min, max):
    return (max - min)*np.random.rand(n) + min


fig = plt.figure()
ax1 = fig.add_subplot( 121 , projection = '3d' )
ax2 = fig.add_subplot( 122, projection = '3d')

n = 20

x = randrange(n, 23 , 32 )
y = randrange(n, 0 , 100 )
z = randrange(n, 0, 0)

ax1.scatter(x, y, z, color ='red', marker ='o')

ax1.set_xlabel( 'X Label' )
ax1.set_ylabel( 'Y Label' )
ax1.set_zlabel( 'Z Label' )

x = np.linspace( 0 , 32 , 5 )
y = randrange(5, 0, 100)
ax2.plot(x, y, zs = 0 , zdir = 'z')

plt.show()