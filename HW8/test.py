from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt
from math import e
import math

fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(0,1,0.01)
y = np.arange(0,1, 0.01)
X, Y = np.meshgrid(x, y)

plt.xlabel('x')
plt.ylabel('y')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()

