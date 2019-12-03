import numpy as np
import matplotlib.pyplot as plt

N_r = 500
x = np.linspace(-N_r,N_r,100)
y = np.linspace(-N_r,N_r,100)
X, Y = np.meshgrid(x, y)
Z = 837.9658 - X * np.sin(np.sqrt(abs(X))) - Y * np.sin(np.sqrt(abs(Y)))

plt.figure(num=None,dpi=100)
plt.contourf(X,Y,Z)
plt.show()