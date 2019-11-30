import numpy as np
import math
import matplotlib.pyplot as plt
import time


def judge(d, t):
    if d < 0:
        out_put = 1
    else:
        d = math.exp(-d / (10*t)) #parameter 1
        if d > np.random.rand():
            out_put = 1
        else:
            out_put = 0
    return out_put


def dist(states):
    dist_sum = 0
    for i in range(states.shape[1] - 1):
        dist_sum += (states[0, i + 1] - states[0, i]) ** 2 + (states[1, i + 1] - states[1, i]) ** 2
    return dist_sum


def new_solve(states):
    states = states
    cities2 = states.copy()
    while 1:
        cit1 = math.ceil(np.random.rand() * (states.shape[1] - 1))
        cit2 = math.ceil(np.random.rand() * (states.shape[1] - 1))
        if abs(np.random.normal(0, 1)) > 0.3: break
        temp = cities2[:, cit1].copy()
        cities2[:, cit1] = cities2[:, cit2].copy()
        cities2[:, cit2] = temp.copy()
    return cities2


states = np.loadtxt('states.txt')
np.random.shuffle(states)
states = states.T
#plt.plot(states[0], states[1])
#plt.show()

tmp, min_temp = 1e5, 1
s_old = dist(states)
cit_new = states
s_new = s_old
counter, t = 0, 0

plt.ion()
while tmp > min_temp:
    plt.clf()
    cit_new = new_solve(states)
    s_new = dist(cit_new)
    dE = (s_new - s_old) * 1  #parameter 2
    j = judge(dE, tmp)
    if j:
        states = cit_new
        s_old = s_new
    if dE < 0:
        counter = 0
        tmp = 1e5/(1+t)
        plt.plot(states[0], states[1])
        plt.pause(0.005)
    else:
        counter += 1
    t += 1

plt.ioff()
print(states)
