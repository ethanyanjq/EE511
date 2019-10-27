import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n - 1))  

def gamma_func(theta):
    n = int(math.floor(theta))
    return (factorial(2 * n) * (math.pi ** 0.5)) / ( (4 ** n) * factorial(n))
    
def gamma_dist(a, b):
    seq = []
    x = np.linspace(0, 25, 200)
    gamma = gamma_func(a)
    for i in range(len(x)):
        seq.append((x[i]**(a-1)) * ((1/b)**a) * (math.e**(-x[i]/b)) / gamma)
    return seq

a = gamma_dist(5.5,1)
x = np.linspace(0, 25, 200)
print(x)
plt.plot(x, a)

lambd = 0.3
x = np.linspace(0, 25, 200)
y = lambd*np.exp(-lambd*(x-4))
plt.plot(x,y)
plt.show()
