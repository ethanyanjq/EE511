import random
import math
import numpy as np
from matplotlib import pyplot as plt

def poisson_rec(lbd):
    sum = []
    i = 0
    F = P = math.exp(-1*lbd)
    while(F<0.99999):
        sum.append(P)
        P = P*(lbd/(i+1))
        F += P
        i += 1
    return sum

a = poisson_rec(120)
aa = np.linspace(1, len(a), len(a))
plt.bar(aa, a)
plt.show()
