import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax1 = fig.add_subplot( 121 , projection = '3d' )
ax2 = fig.add_subplot( 122, projection='3d')
# generuj dane.
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)

X2 = np.arange(- 5 , 5 , 0.1 )
Y2 = np.arange(- 5 , 5 , 0.1 )
X2, Y2 = np.meshgrid(X2, Y2)
R2 = np.sqrt(X2** 2 + Y2** 2 )
Z2 = np.sin(R2)
# rysuj powierzchnię.
surf = ax1.plot_surface(X, Y, Z, cmap =cm.coolwarm, linewidth = 0 , antialiased = False )
ax1.set_zlim(- 1.01 , 1.01 )
ax1.zaxis.set_major_locator(LinearLocator( 10 ))
ax1.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))

surf = ax2.plot_surface(X2, Y2, Z2, cmap =cm.coolwarm, linewidth = 0 , antialiased = True )
ax2.set_zlim(- 1.01 , 1.01 )
ax2.zaxis.set_major_locator(LinearLocator( 10 ))
ax2.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
# Dodanie paska kolorów.
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )
plt.show()