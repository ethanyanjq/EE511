import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from math import sin, cos, pi , tan, log as sin, cos, pi, tan, log
 
def alpha_stable_generate(alpha, beta, n):
    seq = []
    if (alpha == 1):
        for i in range(n):
            gamma = pi * (np.random.rand() - 0.5)
            lbd = 1
            w = -1*log(1 - np.random.rand())/lbd
            left = (0.5*pi + beta*gamma)*tan(gamma)
            right = beta * log(w*cos(gamma)/(0.5*pi + beta*gamma))
            seq.append(left - right)
    else:
        k = (alpha if alpha<1 else (alpha -2))
        gamma_zero = (-0.5*pi*beta*k/alpha)
        for i in range(n):
            gamma = pi * (np.random.rand() - 0.5)
            lbd = 1
            w = -1*log(1 - np.random.rand())/lbd
            left = sin(alpha)*(gamma-gamma_zero)/(cos(gamma)**(1/alpha))
            mid = cos(gamma - alpha*(gamma-gamma_zero))*(1/w)
            right = mid**((1-alpha)/alpha)
            seq.append(left * right)
    return seq

a = alpha_stable_generate(2, 0, 2000)
plt.hist(a, bins = len(list(set(a))))
plt.show()
