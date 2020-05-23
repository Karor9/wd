import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Ustawiamy seed by za każdym razem wyglądało identycznie
np.random.seed( 404080914 )


def randrange(n, min, max):
    return (max - min)*np.random.rand(n) + min


fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 100

for c, m, low, high in [( 'r' , 'o' , - 50 , - 25 ), ( 'b' , '^' , - 30 , - 5 ), ('g', 'v', -10, 5), ('y', '3', -1, 25), ('m', '+', 4, 55)]:
    x = randrange(n, 23 , 32 )
    y = randrange(n, 0 , 100 )
    z = randrange(n, low, high)
    ax.scatter(x, y, z, c =c, marker =m)

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()