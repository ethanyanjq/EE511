import numpy as np
import math


def func(N):
    sum = 0
    for i in range(N):
        x, y = np.random.rand(2)
        sum += np.exp(5 * abs(x - 5) + 5 * abs(y - 5))
    return sum/N

def func1(N):
    sum = 0
    for i in range(N):
        x, y = np.random.rand(2)*2 -[1,1]
        sum += math.cos(math.pi + 5*x + 5*y)
    return 2*2*sum/N

print(func(1000))


