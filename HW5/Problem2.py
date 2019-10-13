import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.special import comb

r_dest = 0.25
def func(p, total_time):
    st_queue = []
    nd_queue = []
    st_state = []
    nd_state = []
    for i in range (total_time):
        if(len(st_queue)!=0 and len(nd_queue)!=0):
            if (st_queue[0] == nd_queue[0]):
                if(np.random.rand()<=0.5):
                    st_queue.pop(0)
                else:
                    nd_queue.pop(0)
            else:
                st_queue.pop(0)
                nd_queue.pop(0)
        elif (len(st_queue) != 0):
            st_queue.pop(0)
        elif (len(nd_queue) != 0):
            nd_queue.pop(0)
        
        rand_gen = np.random.rand(2, 2)
        if (rand_gen[0][0]<= p):
            if (rand_gen[0][1]<=r_dest):
                st_queue.append(1)
            else:
                st_queue.append(2)
        if (rand_gen[1][0]<= p):
            if (rand_gen[1][1]<=r_dest):
                nd_queue.append(1)
            else:
                nd_queue.append(2)
        st_state.append(len(st_queue))
        nd_state.append(len(nd_queue))
    return (np.mean(st_state), np.mean(nd_state))
    
a = func(0.99, 1000)
print(a)
