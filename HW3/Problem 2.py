import random
import numpy as np
from matplotlib import pyplot as plt


total_slots = 60*60*2
def n_bernoulli(n):
    occur_sum = []*n #sum of occurances in n experiments
    for j in range(n):
        counter = 0
        for i in range(total_slots):
            random_num = np.random.random(1)
            if (random_num <= (120/total_slots)):
                counter += 1
        occur_sum.append(counter)
    return occur_sum

occur_sum = n_bernoulli(200)
occur_sum_norep = list(set(occur_sum))
plt.hist(occur_sum, range=(0, 175), bins=len(occur_sum_norep))
plt.show()
