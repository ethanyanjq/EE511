import numpy as np
from matplotlib import pyplot as plt

accepted = []
auxi_dis = [0.05]*20 
c = 1 #c is the scalar of the auxiliary distribution
dis = [0.06]*5 +[0.15, 0.13, 0.14, 0.15, 0.13]+[0]*10

def sample(n): #n stands for the iterations of sampling
    for i in range(n):
        num = np.random.randint(20)
        u = np.random.uniform()
        if (u <= (dis[num]/(c*auxi_dis[num]))):
            accepted.append(num)
            
sample(10000)
print("The efficiency is: " + str(len(accepted)/10000))
plt.hist(accepted, density = 1)
x = np.linspace(0, 20, 20)
plt.bar(x, dis, color = 'r', alpha = 0.2, width = 0.8)
plt.show()
   
