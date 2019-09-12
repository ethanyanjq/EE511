import numpy as np
from numpy import random as nr
from matplotlib import pyplot as plt

def bs_resample(data, alpha):
    Nk = 500 #resample times
    length = len(data)
    bs_mean = []
    bs_var = []
    for i in range(Nk):
        new_seq = []
        for j in range(length):
            num = nr.randint(0, length)
            new_seq.append(data[num])
        bs_mean.append(np.mean(new_seq))
        bs_var.append(np.var(new_seq))
    bs_mean = np.sort(bs_mean)
    bs_var = np.sort(bs_var)
    y = np.linspace(0, 50, 50)
    x2 = [bs_var[int((alpha/2)*Nk)]]*50
    x1 = [bs_var[int((1-alpha/2)*Nk)]]*50
    plt.hist(bs_var, bins=50)
    plt.plot(x1,y)
    plt.plot(x2,y)
    plt.show()
    #return (bs_mean[int((alpha/2)*Nk)], bs_mean[int((1-alpha/2)*Nk)], bs_var[int((alpha/2)*Nk)], bs_var[int((1-alpha/2)*Nk)])
    return (bs_mean[int((alpha/2)*Nk)], bs_mean[int((1-alpha/2)*Nk)], bs_var[int((alpha/2)*Nk)], bs_var[int((1-alpha/2)*Nk)])

N = 1000
uni_seq = nr.rand(N)*5 - 3
average = float(sum(uni_seq))/len(uni_seq)
print("The sample mean is:" + str(average))
sum = 0
for data in uni_seq:
    sum += (data - average) ** 2
stdvar = np.sqrt(sum/(N-1))
print("The sample variance is "+ str(stdvar**2))

result = bs_resample(uni_seq, 0.05)
print("The upper 0.05 threshold for sample mean is: " + str(result[1]))
print("The lower 0.05 threshold for sample mean is: " + str(result[0]))
print("The upper 0.05 threshold for sample variance is: " + str(result[3]))
print("The lower 0.05 threshold for sample variance is: " + str(result[2]))
#plt.hist(uni_seq,bins=50)
#plt.show()
