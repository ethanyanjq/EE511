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
    
def gamma_dist(a, b, x):
    gamma = gamma_func(a)
    return (x**(a-1)) * ((1/b)**a) * (math.e**(-x/b)) / gamma
    
def gamma_list(a, b):
    seq = []
    x = np.linspace(0, 25, 200)
    gamma = gamma_func(a)
    for i in range(len(x)):
        seq.append((x[i]**(a-1)) * ((1/b)**a) * (math.e**(-x[i]/b)) / gamma)
    return seq

def exp_bound(lambd, x):
    return lambd*np.exp(-lambd*(x-4))

N = 10000
y = []
accept = 0
for i in range(N):
    rand_1 = 25 * np.random.rand()
    rand_2 = exp_bound(0.3, rand_1) * np.random.rand()
    if (rand_2 <= gamma_dist(5.5, 1, rand_1)): 
        y.append(rand_1)
        accept += 1
print("The efficiency of accept and reject is {}".format(accept/N))   
plt.hist(y, density = 1, bins = 100)

a = gamma_list(5.5,1.3)
x = np.linspace(0, 25, 200)
plt.plot(x, a)
plt.show()

