import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
import time

def marsaglia(n):
    R1 = []
    R2 = []
    for i in range (n):
        x = (np.random.rand())*2 - 1
        y = (np.random.rand())*2 - 1
        s = x ** 2 + y ** 2
        if (s < 1):
            a1 = x * ((-2 * np.log(s)/s) ** 0.5)
            a2 = y * ((-2 * np.log(s)/s) ** 0.5)
            R1.append(13**0.5 * a1+3)
            R2.append(13**0.5 * a2+3)
    return (R1, R2)

def theoretical(x,mu,sigma):
    pdf = np.exp(-((x - mu)**2)/(2*sigma**2))/(sigma * np.sqrt(2*np.pi))
    return pdf

start = time.time()    
(R1, R2) = marsaglia(1000000)
end = time.time()
plt.hist(R2, bins = 200, density = 1, label = 'Marsaglia method')
print ("The computational time of Marsaglia method is {} seconds".format(end - start))

x = np.arange(-20,20,0.1)
y = theoretical(x, 3, 13**0.5)
plt.plot(x,y, color='r',linewidth = 2, label = 'Theoretical pdf')
plt.legend()
plt.show()


