import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats

n = 1000
percentiles = 0.9
def func(n):
    X = [0]*n
    for i in range(n):
        temp = 0
        for j in range(4):
            temp += (np.random.randn())**2
        X[i] = temp
    return sorted(X)

X = func(n)
X.insert(0, 0)
X.append(20)
Y = np.arange(0, 1, 1/n)
Y = list(Y)
Y.append(1)
Y.insert(0, 0)

temp = 0
percentile = 0
s = 0
for i in range(len(X)):
    if (abs(stats.chi2.cdf(X[i], df=4) - Y[i]) > temp) :
        temp = abs(stats.chi2.cdf(X[i], df=4) - Y[i])
    if (Y[i]>percentiles and s == 0):
        s = 1
        percentile = X[i]
        
print("The maximum difference is: ", temp)
print("The {}th percentile is : {}".format(int(percentiles*100), percentile))
print ("The {}th theoretical percentile is : {}".format(int(percentiles*100),stats.chi2.ppf(percentiles, 4)))

plt.step(X, Y)
plt.plot(np.linspace(0,20,100),stats.chi2.cdf(np.linspace(0,20,100),df=4))
plt.show()


