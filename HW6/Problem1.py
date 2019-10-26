import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats

def theoretical(x,mu,sigma):
    pdf = np.exp(-((x - mu)**2)/(2*sigma**2))/(sigma * np.sqrt(2*np.pi))
    return pdf

def Generate (n, n1, n2, d1, d2):
    X_seq = []
    Y_seq = []
    Sum = []
    for i in range(n):
        U1 = np.random.rand()
        U2 = np.random.rand()
        X_temp = ((-2 * math.log(U1)) ** 0.5) * math.cos(2*math.pi*U2)
        Y_temp = ((-2 * math.log(U1)) ** 0.5) * math.sin(2*math.pi*U2)
        X_seq.append(X_temp * (d1)**0.5 + n1)
        Y_seq.append(Y_temp * (d2)**0.5 + n2)
        Sum.append(X_temp * (d1)**0.5 + n1 + Y_temp * (d2)**0.5 + n2)
    return (X_seq, Y_seq, Sum)
    
result = Generate(10000, 1, 2, 4, 9)
plt.hist(result[2], density = 1, bins = 300, alpha = 0.9, label = 'N(1,4)+N(2,9)')

x = np.arange(-40,40,0.1)
y = theoretical(x, 3, 13**0.5)
plt.plot(x,y, color='r',linewidth = 2, label = 'Theoretical pdf')
plt.legend()
plt.show()

print("The covariance of X and Y is: \n {}".format(np.cov(result[0], result[1])))
print("The mean of A is : {} and the variance is :{}".format(np.mean(result[2]), np.var(result[2])))
       
        


