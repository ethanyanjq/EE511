import numpy as np
from numpy import random as nr
from matplotlib import pyplot as plt
from itertools import groupby

N = 100
M = 10
uni_seq = nr.randint(0, M, N)
freq_count = []
for i, group in groupby(sorted(uni_seq), key=lambda x:x):
    freq_count.append(list(group))
loss = [0]*M
chi = 0
for i in range(M):
    loss[i] = abs(len(freq_count[i])-N/M)
    chi += (loss[i] - N/M)**2 *(M/N)
print(chi)
print(loss)

freq_count_2 = freq_count
freq_count_2.append([])
M+=1
loss_2 = [0]*M
chi_2 = 0
for i in range(len(freq_count_2)):
    if (i == 0):
        loss_2[i] = abs(len(freq_count_2[i])-0)
    else:
        loss_2[i] = abs(len(freq_count_2[i])-N/M)
        chi_2 += (loss_2[i] - N/M)**2 *(M/N)
print(chi_2)
print(loss_2)
    




#uni_seq = nr.rand(N)*(M-1)
#plt.hist(uni_seq)
#freq_count = []
#mean = []
#for i, group in groupby(sorted(uni_seq), key=lambda x:x//1):
#    freq_count.append(list(group))
#    
#print(freq_count)
#
#summ = [1000/10]*len(freq_count)
    


