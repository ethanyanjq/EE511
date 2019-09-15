import math
import numpy as np
from matplotlib import pyplot as plt

def sample_sum(n):
    n_seq = []
    for i in range(n):
        sum = 0
        k = 0
        while (sum<=4):
            temp = np.random.rand()
            sum += temp
            k += 1
        n_seq.append(k)
    return n_seq
    
a = sample_sum(10000)
print(np.mean(a))
plt.hist(a)
plt.show()


