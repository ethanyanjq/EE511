import numpy as np
import math
import matplotlib.pyplot as plt
#import scipy.stats as stats

def arrival_generate(n):
    lambda_seq = [4, 7, 10, 13, 16, 19, 16, 13, 10, 7]
    arrival = []
    for i in range(n): #每个小循环为10个小时，这里表示一共10次大循环，总共100小时
        for j in range(10): #每个小循环里面的每一个小时
            k = i*10 + j  #这里将k初始化为每个小时的初始时间，k用于记录每一个小时内的到达时间（到达一次就累加间隔时间）
            while k < i*10 + j + 1 : #当上一次的k小于当前小时加1小时，也就是下一小时的时候
                x = np.log(1 - np.random.rand())/(-1 * lambda_seq[j])
                k += x
                arrival.append(k)
            arrival.pop() #如果跳出循环证明上一个到达时间已经大于下一小时并且已经被加到arrival里，所以要把上次到达删掉
    return arrival
  
def main_func(arrival_seq):
    lower_pointer = 0
    higher_pointer = 0.3 * np.random.rand()
    interval = []
    index = []
    while(higher_pointer < ceil(arrival_seq[-1])):
        interval_count = len(list(x for x in arrival_seq if lower_pointer< x <= higher_pointer))
        if 
 
x = arrival_generate(10)
print(x)
y = np.linspace(1, len(x), num=len(x))
plt.step(x, y)
plt.show()


