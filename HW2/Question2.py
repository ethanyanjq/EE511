import numpy as np
from numpy import random as nr
from matplotlib import pyplot as plt

N = 1000
uni_seq1 = nr.rand(N)
uni_seq2 = nr.rand(N)
seq_cov = np.cov(uni_seq1, uni_seq2)
print("Cov of seq1 and seq2 is:" + str(seq_cov[0][1]))

seq_y = [0]*N
seq_y[0] = uni_seq1[0]
seq_y[1] = uni_seq1[1] - 2*uni_seq1[0]
seq_y[2] = uni_seq1[2] - 2*uni_seq1[1] + 0.5*uni_seq1[0]

for i in range(3, N):
    seq_y[i] = uni_seq1[i] - 2*uni_seq1[i-1] + 0.5*uni_seq1[i-2] - uni_seq1[i-3]
xy_cov = np.cov(uni_seq1, seq_y)
print("Cov of X and Y is:" + str(xy_cov[0][1]))
    

uni_seq1 = nr.rand(N)
uni_seq2 = nr.rand(N)
seq_cov = np.cov(uni_seq1, uni_seq2)
print("Cov of seq1 and seq2 is:" + str(seq_cov[0][1]))

seq_y = [0]*N
seq_y[0] = uni_seq1[0]
seq_y[1] = uni_seq1[1] - 2*uni_seq1[0]
seq_y[2] = uni_seq1[2] - 2*uni_seq1[1] + 0.5*uni_seq1[0]

for i in range(3, N):
    seq_y[i] = uni_seq1[i] - 2*uni_seq1[i-1] + 0.5*uni_seq1[i-2] - uni_seq1[i-3]
xy_cov = np.cov(uni_seq1, seq_y)
print("Cov of X and Y is:" + str(xy_cov[0][1]))

uni_seq1 = nr.rand(N)
uni_seq2 = nr.rand(N)
seq_cov = np.cov(uni_seq1, uni_seq2)
print("Cov of seq1 and seq2 is:" + str(seq_cov[0][1]))

seq_y = [0]*N
seq_y[0] = uni_seq1[0]
seq_y[1] = uni_seq1[1] - 2*uni_seq1[0]
seq_y[2] = uni_seq1[2] - 2*uni_seq1[1] + 0.5*uni_seq1[0]

for i in range(3, N):
    seq_y[i] = uni_seq1[i] - 2*uni_seq1[i-1] + 0.5*uni_seq1[i-2] - uni_seq1[i-3]
xy_cov = np.cov(uni_seq1, seq_y)
print("Cov of X and Y is:" + str(xy_cov[0][1]))

uni_seq1 = nr.rand(N)
uni_seq2 = nr.rand(N)
seq_cov = np.cov(uni_seq1, uni_seq2)
print("Cov of seq1 and seq2 is:" + str(seq_cov[0][1]))

seq_y = [0]*N
seq_y[0] = uni_seq1[0]
seq_y[1] = uni_seq1[1] - 2*uni_seq1[0]
seq_y[2] = uni_seq1[2] - 2*uni_seq1[1] + 0.5*uni_seq1[0]

for i in range(3, N):
    seq_y[i] = uni_seq1[i] - 2*uni_seq1[i-1] + 0.5*uni_seq1[i-2] - uni_seq1[i-3]
xy_cov = np.cov(uni_seq1, seq_y)
print("Cov of X and Y is:" + str(xy_cov[0][1]))
