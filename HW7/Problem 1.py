import numpy as np 
import matplotlib.pyplot as plt

def gaussian(x, mean, cov):
    d = len(x)
    x1 = np.array(x) - np.array(mean)
    x1_T = x1.T
    x1_T = x1_T.tolist()
    x1 = x1.tolist()
    inv = np.linalg.inv(cov)
    temp1 = np.dot(x1, inv)
    return (1/ (np.sqrt((2*np.pi)**d*np.linalg.det(cov)))* 
            np.exp(-np.dot(temp1, x1_T)/2))
            
mean = [1, 2, 3]
cov = [[3, -1, 1], [-1, 5, 3], [1, 3, 4]]
vector_list = []
for i in range(100):
        a = 20*np.random.rand(3) - 10
        if ( gaussian(a, mean, cov) <  1/(20*20*20)):
            vector_list.append(a.tolist())
print(vector_list)
        


