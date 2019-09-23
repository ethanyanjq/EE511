import math
import numpy as np
from matplotlib import pyplot as plt

def cdf_60(p):
    cdf = [0]*60
    temp = 0
    for i in range(60):
        temp += p/(i+1)
        cdf[i] = temp
    return cdf

def prob_pos(cdf, prob):
    if (prob < cdf[0]):
        return 1
    for i in range(59):
        if (prob >= cdf[i] and prob < cdf[i+1]):
            return i+2 
            #We classify it to i+1 and since array starts from 0,i+1 has to plus 1

cdf = cdf_60(10)
###
list_dist = []
for i in range(10000):
    random_num = np.random.uniform(0, cdf[59])
    list_dist.append(prob_pos(cdf, random_num))
hist_dist_bins = list(set(list_dist))
plt.hist(list_dist, bins = len(hist_dist_bins))
plt.show()
### The above used to generate histogram
sum = [0]*100
for j in range(100):
    for i in range(2000):
        random_num = np.random.uniform(0, cdf[59])
        if (prob_pos(cdf, random_num) == 60):
            sum[j] = i+1
            break
print(sum)
print("The mean is: " + str(np.mean(sum)))
print("The variance is: " + str(np.var(sum)))
sum_hst = list(set(sum))
plt.hist(sum, bins = len(sum_hst))
plt.show()
            




