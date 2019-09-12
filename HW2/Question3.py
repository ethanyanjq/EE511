import numpy as np
from numpy import random as nr
from matplotlib import pyplot as plt
from itertools import groupby

N = 1000
M = 10
uni_seq = nr.randint(0, M, N)
freq_count = []
plt.hist(uni_seq)
plt.show()
for i, group in groupby(sorted(uni_seq), key=lambda x:x):
    freq_count.append(list(group))

dd = []
for l in range(10):
    dd.append(len(freq_count[l]))
print(dd)

loss = [0]*M
chi = 0
for i in range(M):
    loss[i] = abs(len(freq_count[i])-N/M)
    chi += (loss[i] - N/M)**2 *(M/N)
print(chi)
print(loss)

freq_count_2 = freq_count
freq_count_2.append([])
loss_2 = [0]*(M+1)
chi_2 = 0
for i in range(1, len(freq_count_2)):
    loss_2[i] = abs(len(freq_count_2[i])-N/M)
    chi_2 += (loss_2[i] - N/M)**2 *(M/N)
del loss_2[0]
print(chi_2)
print(loss_2)



