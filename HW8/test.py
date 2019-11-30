import numpy as np

f = np.loadtxt('states.txt')
sum = 0
for i in range(len(f) - 1):
    sum += (f[i+1][0] - f[i][0]) ** 2 + (f[i+1][1] - f[i][1]) ** 2
print(sum)


