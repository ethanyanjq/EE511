import numpy as np


def my_func(x,y):
    return np.exp((x+y)**2)

N = 10000
fX = np.random.rand(1,N)
fY = np.random.rand(1,N)
X = my_func(fX,fY)
print('Mean is:', str(np.mean(X)))
print(2*np.std(X)/np.sqrt(N))

N_is = 10000
U = np.random.rand(2,N_is)
X_is = np.log(1+(np.exp(1)-1)*U)
T = np.power((np.exp(1)-1),2)*np.exp((np.power(np.sum(X_is,axis=0),2)) - np.sum(X_is,axis=0))
print('Mean is:',str(np.mean(T)))
print(2*np.std(T)/np.sqrt(N))