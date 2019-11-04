import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    p = []
    for i in range(len(x)):
        for j in range(len(y)):
            p.append(x[i]+y[j])
    p = np.array(p)
    p = p.reshape((10,-1))
    print(p.shape[0])
    return p

n = 10
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)
# use plt.contourf to filling contours
# X, Y and value for (X,Y) point
plt.contourf(X, Y, f(x, y), 8, alpha=.75, cmap=plt.cm.hot)
plt.show(0)


        


