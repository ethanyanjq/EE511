import matplotlib.pyplot as plt
import math
import numpy as np


def judge(diff, t):
    if diff < 0:
        out_put = 1
    else:
        diff = math.exp(-diff / (3 * t))
        if diff > np.random.rand():
            out_put = 1
        else:
            out_put = 0
    return out_put


def func_calculation(x, y):
    return 837.9658 - x * math.sin(math.sqrt(abs(x))) - y * math.sin(math.sqrt(abs(y)))


lower_bound, upper_bound = -500, 500
t, counter = 0, 0
temp = 1e4
min_temp = 1e-3

x_old = (upper_bound - lower_bound) * np.random.rand() + lower_bound
y_old = (upper_bound - lower_bound) * np.random.rand() + lower_bound
x_new, y_new = x_old, y_old
s_old = func_calculation(x_old, y_old)
s_new = s_old

plt.ion()
N_r = 500
x = np.linspace(-N_r, N_r, 100)
y = np.linspace(-N_r, N_r, 100)
X, Y = np.meshgrid(x, y)
Z = 837.9658 - X * np.sin(np.sqrt(abs(X))) - Y * np.sin(np.sqrt(abs(Y)))

plt.figure(num=None, dpi=100)
plt.contourf(X, Y, Z)
plt.pause(1)

while temp > min_temp:
    delta = np.random.normal(0, 200)
    x_new = x_old + delta
    if x_new < lower_bound or x_new > upper_bound:
        x_new = x_new - delta
    delta = np.random.normal(0, 200)
    y_new = y_old + delta
    if y_new < lower_bound or y_new > upper_bound:
        y_new = y_new - delta
    s_new = func_calculation(x_new, y_new)

    dE = s_old - s_new
    j = judge(dE, temp)
    if j:
        s_old, x_old, y_old = s_new, x_new, y_new
    if dE < 0:
        temp = 1e4 / (1 + t)
    else:
        counter += 1
    t += 1
    plt.scatter([x_old], [y_old], marker='x', c='#DC143C')
    plt.pause(0.001)
    if counter > 50:
        break

plt.ioff()
plt.show()
print(x_old, y_old, s_old)
