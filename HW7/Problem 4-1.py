import numpy as np 
import matplotlib.pyplot as plt
import xlrd
import random
import math

def scatter_plot(sheet):
    scatter_data = sheet.col_values(0) + sheet.col_values(1)
    scatter_data = np.array(scatter_data)
    scatter_data = scatter_data.reshape(2, -1)
    plt.scatter(scatter_data[0, :], scatter_data[1, :])
    plt.show()
    
def init_center(data, dim):
    return np.array(random.sample(data, dim))
    
def eucilid_dist(dot1, dot2):
    dist = math.sqrt((dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2)
    return dist

def dot2center(dots, centers):
    dist_list = []
    for dot in dots:
        dot2center = []
        for center in centers:
            dot2center.append(eucilid_dist(dot, center))
        dist_list.append(dot2center)
    return dist_list

def classify(dots_dist):
    classify = []
    for i in range(len(dots_dist)):
        if (dots_dist[i][0] <= dots_dist[i][1]):classify.append(0)
        else: classify.append(1)
    return classify
    
def center_update(dots, classify):
    new_centers = []
    sum_0_x = 0
    sum_0_y = 0
    sum_1_x = 0
    sum_1_y = 0
    count_0 = 0
    count_1 = 0
    for i in range(len(classify)):
        if (classify[i] == 0):
            sum_0_x += dots[i][0]
            sum_0_y += dots[i][1]
            count_0 += 1
        else:
            sum_1_x += dots[i][0]
            sum_1_y += dots[i][1]
            count_1 += 1
    return [[sum_0_x/count_0, sum_0_y/count_0], [sum_1_x/count_1, sum_1_y/count_1]]
        
workbook = xlrd.open_workbook(r'data.xlsx')
sheet = workbook.sheet_by_index(1)
data = []
for i in range(sheet.nrows):
    data.append(sheet.row_values(i))
    
init_center = init_center(data, 2)
print(init_center)

for i in range(100):
    a = dot2center(data, init_center)
    b = classify(a)
    init_center = center_update(data, b)
print(init_center)   

class0_x = []
class0_y = []
class1_x = []
class1_y = []
for i in range(len(data)):
    if (b[i] == 0):
        class0_x.append(data[i][0])
        class0_y.append(data[i][1])
    else:
        class1_x.append(data[i][0])
        class1_y.append(data[i][1])
plt.scatter(class0_x, class0_y)
plt.scatter(class1_x, class1_y)
plt.show()

    







