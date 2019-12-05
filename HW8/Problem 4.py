import numpy as np
import math
import matplotlib.pyplot as plt
import time


def judge(d, t):
    if d < 0:
        out_put = 1
    else:
        d = math.exp(-d / 100*(t)) #parameter 1
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


def switch(states):
    states = states
    cities2 = states.copy()
    while 1:
##        cit1 = math.ceil(np.random.rand() * (states.shape[1]))
##        factor = math.ceil(np.random.normal(0,10))
##        if cit1 - abs(factor) < 1 or cit1 + abs(factor) > (states.shape[1] - 1):
##            break
##        elif abs(np.random.normal(0, 1)) > 1: break
##        temp = cities2[:, cit1].copy()
##        cities2[:, cit1] = cities2[:, cit1 + factor].copy()
##        cities2[:, cit1 + factor] = temp.copy()
        cit1 = math.ceil(np.random.rand() * (states.shape[1] - 1))
        cit2 = math.ceil(np.random.rand() * (states.shape[1] - 1))
        if abs(np.random.normal(0, 1)) > 1: break
        temp = cities2[:, cit1].copy()
        cities2[:, cit1] = cities2[:, cit2].copy()
        cities2[:, cit2] = temp.copy()
    return cities2


states = np.loadtxt('states.txt')
np.random.shuffle(states)
CA = np.array([[38.555605, 18.531074]])
states = np.concatenate((CA, states),axis=0)
states = states.T

tmp, min_temp = 1e4, 1e-3
s_old = dist(states)
cit_new = states
s_new = s_old
counter, t = 0, 0

plt.ion()
while tmp > min_temp:
    plt.clf()
    #plt.scatter(18.531074, 38.555605, color= "r")
    cit_new = switch(states)
    s_new = dist(cit_new)
    dE = (s_new - s_old) * 1  #parameter 2
    j = judge(dE, tmp)
    if j:
        states = cit_new
        s_old = s_new
    if dE < 0:
        # counter = 0
        tmp = 1e4/(1+t)
        plt.plot(states[1], states[0])
        plt.pause(0.001)
    # else:
    #     counter += 1
    t += 1

plt.ioff()
print(states)
