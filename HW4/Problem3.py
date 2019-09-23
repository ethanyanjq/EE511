import numpy as np
import math
import xlrd
import matplotlib.pyplot as plt

def bs_resample(data):
    Nk = 1000 #resample times
    length = len(data)
    bs_mean = []
    bs_var = []
    alpha = 0.95
    for i in range(Nk):
        new_seq = []
        for j in range(length):
            num = np.random.randint(0, length)
            new_seq.append(data[num])
        bs_mean.append(np.mean(new_seq))
    bs_mean = np.sort(bs_mean)
    return (bs_mean[int((alpha/2)*Nk)], bs_mean[int((1-alpha/2)*Nk)])

workbook = xlrd.open_workbook(r'data.xlsx')
sheet = workbook.sheet_by_index(0)
duration = sheet.col_values(1)
waiting = sheet.col_values(2)

duration_15 = duration[:15]
waiting_15 = waiting[:15]
waiting_list = list(set(waiting))
plt.hist(waiting, bins = len(waiting_list))
plt.show()

std_dev = np.std(waiting_15, ddof = 1)
mean = np.mean(waiting_15)
t = 2.1448
upper_bound = mean + (std_dev/math.sqrt(15))*t
lower_bound = mean - (std_dev/math.sqrt(15))*t
print(upper_bound, lower_bound)
bs_result = bs_resample(waiting_15)
print(bs_result[0], bs_result[1])

std_dev = np.std(waiting, ddof = 1)
mean = np.mean(waiting)
t = 1.960
upper_bound = mean + (std_dev/math.sqrt(15))*t
lower_bound = mean - (std_dev/math.sqrt(15))*t
print(upper_bound, lower_bound)
bs_result = bs_resample(waiting)
print(bs_result[0], bs_result[1])

