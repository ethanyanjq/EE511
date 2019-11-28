import numpy as np
import math
from scipy.stats import multivariate_normal


def func(N):
    sum, i = 0, 0
    mean = [0, 0]
    cov = [[0.05, 0], [0, 0.05]]
    while i < N:
        x, y = np.random.multivariate_normal(mean, cov)
        x = abs(x)
        y = abs(y)
        if (x <= 1 and y <= 1):
            var = multivariate_normal(mean, cov)
            px = var.pdf([x, y])*4
            fx = np.exp(5 * abs(x - 5) + 5 * abs(y - 5))
            sum += fx / px
            i += 1
    return sum / N

print(func(1000))


def func1(N):
    sum = 0
    x,y = np.linspace(0,1,10,endpoint=0), np.linspace(0,1,10,endpoint=0)
    for i in x:
        for j in y:
            for k in range(10):
                x0, y0 = np.random.rand(2)
                x0 = x0/10 + i
                y0 = y0/10 + j
                sum += (np.exp(5 * abs(x0 - 5) + 5 * abs(y0 - 5)))/N
    return sum
print(func1(1000))
