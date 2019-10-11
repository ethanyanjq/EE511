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
  
exp_lambda = 25 #Service Time
def main_func(arrival_seq):
    lower_pointer = 0
    higher_pointer = 0 #0.3 * np.random.rand()
    interval = []
    while(higher_pointer < math.ceil(arrival_seq[-1])): 
        higher_pointer += 0.3 * np.random.rand()
        arrival_num = len(list(x for x in arrival_seq if lower_pointer< x <= higher_pointer))
        if (arrival_num != 0): #判断区间内是否有到达的工作，如果有，服务器会在这次休息结束之后处理
            interval.append(higher_pointer - lower_pointer)
            for i in range(arrival_num):
                higher_pointer += float(np.random.exponential(1/exp_lambda, 1)) #增加指数分布的处理时间
                if (len(list(x for x in arrival_seq if lower_pointer< x <= higher_pointer)) != 0): #如果在处理时间内又来新的了，则任务数再加一
                    arrival_num += len(list(x for x in arrival_seq if lower_pointer< x <= higher_pointer))
            lower_pointer = higher_pointer
    return interval

break_time = []
for i in range(10):
    x = arrival_generate(10)
    break_time.append(sum(main_func(x)))
y = np.linspace(1, len(x), num=len(x))
plt.step(x, y)
plt.show()
print(sum(break_time)/len(break_time))


