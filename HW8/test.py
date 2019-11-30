import numpy as np

f = np.loadtxt('states1.txt')
b = np.array([[9,9]])
f = np.concatenate((f,b),axis=0)
print(f)


