import matplotlib.pyplot as plt
import math
import random
import numpy as np
from diagram import print_diagram


def judge(d, t):
    if d < 0:
        out_put = 1
    else:
        d = math.exp(-d/(15*t))
        if d > np.random.rand():
            out_put = 1
        else:
            out_put = 0
    return out_put


def func_calculation(x, y):
    return 837.9658 - x * math.sin(math.sqrt(abs(x))) - y * math.sin(math.sqrt(abs(y)))


lower_bound, upper_bound = -500, 500
t, counter = 0, 0
temp = 1e4
min_temp = 1

x_old = (upper_bound - lower_bound) * np.random.rand() + lower_bound
y_old = (upper_bound - lower_bound) * np.random.rand() + lower_bound
x_new, y_new = x_old, y_old
s_old = func_calculation(x_old, y_old)
s_new = s_old

while temp > min_temp:
    delta = np.random.normal(0, 150)
    x_new = x_old + delta
    if x_new < lower_bound or x_new > upper_bound:
        x_new = x_new - delta
    delta = np.random.normal(0, 150)
    y_new = y_old + delta
    if y_new < lower_bound or y_new > upper_bound:
        y_new = y_new - delta
    s_new = func_calculation(x_new, y_new)

    dE = s_old - s_new
    j = judge(dE, temp)
    if j:
        s_old = s_new
        x_old = x_new
        y_old = y_new
    if dE < 0:
        temp = 1e3 / (1 + t)
    else:
        counter += 1
    t += 1
    plt.scatter([x_old], [y_old], marker='x', c='#DC143C')
    if counter > 1e3:
        break

plt.show()
print(x_old, y_old, s_old)
