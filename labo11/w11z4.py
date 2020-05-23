import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# konfiguracja wielkości wykresu, figsize określa wielkość wykresu w calach
fig = plt.figure( figsize =( 8 , 3 ))
ax1 = fig.add_subplot( 121 , projection = '3d' )
ax2 = fig.add_subplot( 122 , projection = '3d' )
ax3 = fig.add_subplot( 222 , projection = '3d' )
ax4 = fig.add_subplot( 221, projection='3d')
ax5 = fig.add_subplot( 131, projection='3d')
# fikcyjne dane
_x = np.arange( 4 )
_y = np.arange( 5 )
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade = True )
ax1.set_title('Wykres zacieniony')
ax2.bar3d(x, y, bottom, width, depth, top, shade = False )
ax2.set_title('Wykres nie zacieniony')
ax3.bar3d(x, y, bottom, width, depth, top, color='green' ,shade=False )
ax3.set_title('Wykres zielony, nie zacieniony')
ax4.bar3d(x, y, bottom, width, depth, top, color='red' ,shade=True )
ax4.set_title('Wykres czerwony, zacieniony')
ax5.bar3d(x, y, bottom, width, depth, top, color='pink' ,shade=True )
ax5.set_title('Wykres różowy, zacieniony')
plt.show()