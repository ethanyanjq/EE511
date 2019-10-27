import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
 
def alpha_stable_generate(alpha, beta, n):
    seq = []
    for i in range(n):
        k = (alpha if alpha<=1 else (2-alpha))
        phi0 = -0.5 * beta * k / alpha
        beta_prime = (beta if alpha == 1 else (-1 * math.tan(0.5 * math.pi * (1-alpha) * math.tan(alpha * phi0))))
        u = np.random.rand()
        phi = math.pi * (u-0.5)
        epsilon = 1 - alpha
        w = -1 * math.log(np.random.rand())
        z = (math.cos(epsilon*phi) - math.tan(alpha*phi0)*math.sin(epsilon*phi)/(w*math.cos(phi)))
        mid = math.sin(alpha*phi) - math.tan(alpha*phi0)*math.cos(alpha*phi)/math.cos(phi)
        s = math.tan(alpha*phi0)+z ** (epsilon / alpha) * mid
        seq.append(s)
    return seq
    
a = alpha_stable_generate(1, 0, 1000)
plt.hist(a, bins = 100)
plt.show()
