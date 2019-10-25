import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.special import comb

def error(y,x):
    y = np.array(y)
    x = np.array(x)
    error = ((y - x)**2).sum()
    return error

N = 100
trans_matrix = np.zeros((2*N + 1,2*N + 1))
for i in range (2*N+1):
    for j in range (2*N+1):
        trans_matrix[i][j] = comb(2*N, j) * (i/(2*N))**j * (1-i/(2*N))**(2*N-j)
trans_matrix = np.mat(trans_matrix)
print("eigenvalues are: ", np.linalg.eigvals(trans_matrix))

initial_state = [0]*(2*N+1)
initial_state [2*N] = 0.49
initial_state [0] = 0.5
initial_state [N-1] = 0.01
initial_state = np.mat(initial_state)
#while error_sum > 0.000000001:
#    k = initial_state
#    initial_state = initial_state * trans_matrix
#    error_sum = error(k, initial_state)
#    i += 1
#
#print(i)
variance = []
for i in range(1000):
    initial_state = initial_state * trans_matrix
    variance.append(np.var(initial_state))
print(initial_state)
x = np.linspace(1, 1000, 1000)
plt.plot(x, variance)
plt.xlabel("Times of experiment")
plt.ylabel("Variance")
plt.show()

    


