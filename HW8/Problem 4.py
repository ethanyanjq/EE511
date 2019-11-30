import numpy as np
import math
import matplotlib.pyplot as plt


def judge(d, t):
    if d < 0:
        out_put = 1
    else:
        d = math.exp(-d / (5 * t))
        if d > np.random.rand():
            out_put = 1
        else:
            out_put = 0
    return out_put


def dist(states):
    dist_sum = 0
    for i in range(len(states) - 1):
        dist_sum += (states[i + 1][0] - states[i][0]) ** 2 + (states[i + 1][1] - states[i][1]) ** 2
    return dist_sum

def solve(city):



states = np.loadtxt('states.txt')
plt.plot(states[0], states[1])
plt.show()
