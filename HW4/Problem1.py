import numpy as np
import math
from matplotlib import pyplot as plt

def fun1(x):
    return math.exp(x**2 + x)

def fun2(x):
    return math.exp(-1*x**2)  

def fun3(x, y):
    return math.exp(-1*(x+y)**2)

#N = 100000    
#x_min = -2
#x_max = 2
#x_seq = [0]*N
#for i in range(N):
#    x_seq[i] = fun1(np.random.uniform(x_min,x_max))
#y = sum(x_seq)*(x_max - x_min)/N
#print(y)

#N = 10000 
#x_min = 0
#x_max = 1
#x_seq = [0]*N
#for i in range(N):
#    temp = np.random.uniform(x_min,x_max)
#    x_seq[i] = fun2(1/temp - 1) / (temp)**2
#y = 2*sum(x_seq)*(x_max - x_min)/N
#print(y)

N = 10000 
x_min = 0
x_max = 1
x_seq = [0]*N
for i in range(N):
    x_seq[i] = fun3(np.random.uniform(x_min,x_max), np.random.uniform(x_min,x_max))
y = sum(x_seq)*(x_max - x_min)/N
print(y)

    

    

    
