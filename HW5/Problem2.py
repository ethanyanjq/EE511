import numpy as np
import math
import matplotlib.pyplot as plt

r_dest = 0.5
def func(p, total_time):
    st_queue = []
    nd_queue = []
    st_state = []
    nd_state = []
    num = []
    for i in range (total_time):
        if(len(st_queue)!=0 and len(nd_queue)!=0):
            if (st_queue[0] == nd_queue[0]):
                if(np.random.rand()<=0.5):
                    st_queue.pop(0)
                else:
                    nd_queue.pop(0)
                num.append(1)
            else:
                st_queue.pop(0)
                nd_queue.pop(0)
                num.append(2)
        elif (len(st_queue) != 0):
            st_queue.pop(0)
            num.append(1)
        elif (len(nd_queue) != 0):
            nd_queue.pop(0)
            num.append(1)
        else :
            num.append(0)
        
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
#    return (np.mean(st_state), np.mean(nd_state))
    return (np.mean(num))

p = np.linspace(0,1,101)
x1 = []
for i in range(100):
    temp = func(0.5, 1000)
    x1.append(temp)
print(np.percentile(x1, 0.025), np.percentile(x1, 0.975))

#p = np.linspace(0,1,101)
#x1 = []
#for i in range(len(p)):
#    temp = func(p[i], 1000)
#    x1.append(temp)
#plt.plot(p, x1)
#plt.xlabel("Value of p")
#plt.ylabel("Mean of packets processed")
#plt.show()

#p = np.linspace(0,1,101)
#x1 = []
#x2 = []
#for i in range(len(p)):
#    temp = func(p[i], 1000)
#    x1.append(temp[0])
#    x2.append(temp[1])
#plt.plot(p, x1)
#plt.plot(p, x2)
#plt.xlabel("Value of p")
#plt.ylabel("Expected number of packets in buffer")
#plt.show()


