import numpy as np
from scipy.stats import levy_stable
import matplotlib.pyplot as plt
N = 1000
##alpha, beta = 1.8, 0.75
##r = levy_stable.rvs(alpha, beta, size=N, scale = 0.3)
##plt.hist(r,bins = 30,label = "α=2 and β=0.75")

##alpha, beta = 2, 0.75
##r = levy_stable.rvs(alpha, beta, size=N, scale = 1)
##plt.hist(r,alpha= 0.5,bins = 20,label = "Theoretical and β=0.75")
##plt.legend()
##plt.show()

alpha, beta = 0.5, 0
r = levy_stable.rvs(alpha, beta, size=N, scale = 1)
x = np.linspace(0,999,1000)
plt.plot(x,r)
plt.legend()
plt.show()
