import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from k_means import *


def contour_plot(x, y, alpha, var1, var2):
    p = []
    for i in range(len(x)):
        for j in range(len(y)):
            p.append(alpha[0] * var1.pdf([x[i], y[j]]) + alpha[1] * var2.pdf([x[i], y[j]]))
    p = np.array(p)
    p = p.reshape((len(x), -1))
    return p.T


def init(data, k):
    dim = np.shape(data)[1]
    alpha = np.ones(k)
    sigma = np.zeros((k, dim, dim))
    for num in range(k):
        alpha[num] = 1.0 / float(k)
        sigma[num, :, :] = np.identity(dim)
    mu = np.array(main_func())
    return alpha, mu, sigma


def guassian(x, mu, sigma):
    d = np.shape(x)[1] / 2.0
    coefficent = 1 / (np.power(np.pi, d) * np.sqrt(np.linalg.det(sigma)))
    sigma_inverse = np.linalg.pinv(sigma)
    coefficent *= np.exp(-0.5 * np.sum(np.dot((x - mu), sigma_inverse) * (x - mu), axis=1))
    return coefficent


def EM_Algorithm(data, weight, mu, sigma):
    series = np.empty_like(data)
    while True:
        temp_sigma = sigma.copy()
        for num in range(2):
            series[:, num] = guassian(data, mu[num, :], sigma[num, :, :])
        series = series * weight
        guass_array_sum = (np.sum(series, axis=1)).reshape(len(series), 1)
        series = series / guass_array_sum
        for row in range(2):
            temp = 0
            weight[row] = np.sum(series[:, row]) / len(data)
            mu[row, :] = np.sum(series[:, row].reshape(len(series), 1) * data, axis=0) / np.sum(
                series[:, row])
            for num in range(len(data)):
                temp += series[num, row] * np.dot((data[num, :] - mu[row, :]).reshape(len(mu[row, :]), 1),
                                                  (data[num, :] - mu[row, :]).reshape(1, len(mu[row, :])))
                sigma[row, :, :] = temp / np.sum(series[:, row])
        if (abs(sigma - temp_sigma) < 1e-8).all():break
    return weight, mu, sigma

cov1 = np.mat("0 0.2;0.2 0.1")
cov2 = np.mat("0.3 0.1;0.1 0.2")
mu1 = np.array([0.3, 0.5])
mu2 = np.array([1, -0.5])

data = np.loadtxt("original_data.txt")
init_alpha, init_mu, init_sigma = init(data, 2)
alpha, mu, sigma = EM_Algorithm(data, init_alpha, init_mu, init_sigma)

for num in range(2):
    print("The weight of model %d is: %.3f, mean is :%s,\n cov is :\n%r" % (num + 1, alpha[num], mu[num], sigma[num]))
n = 100
x = np.linspace(1, 5.5, n)
y = np.linspace(38, 100, n)
var1 = multivariate_normal(mean=mu[0], cov=sigma[0])
var2 = multivariate_normal(mean=mu[1], cov=sigma[1])

plt.plot(data[:, 0], data[:, 1], "ro")
p = contour_plot(x, y, alpha, var1, var2)
plt.contourf(x, y, p, 20, alpha=.75)
plt.colorbar()
plt.show()
