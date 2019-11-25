import numpy as np
import math

N = 1000
x = [[0.1], [0.1], [0.1]]
for i in range(N):
    m = math.floor(3 * np.random.rand())
    sum = 0
    e = [0,1,2]
    e.remove(m)
    for j in e:
        sum += (j+1)*x[j][-1]
    rest = 1 - sum
    while 1:
        temp = np.random.exponential(1)
        if temp * (m+1) < rest: break
    x[m].append(temp)

print(np.mean(x[0]+2*np.mean(x[1])+3*np.mean(x[2])))