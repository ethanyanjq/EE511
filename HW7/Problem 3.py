#Inspired with https://github.com/liloganle/GMM-EM.git
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal


def contour_plot(x, y, alpha, var1, var2):
    p = []
    for i in range(len(x)):
        for j in range(len(y)):
            p.append(alpha[0] * var1.pdf([x[i], y[j]]) + alpha[1] * var2.pdf([x[i], y[j]]))
    p = np.array(p)
    p = p.reshape((len(x), -1))
    return p.T

def init(data, k):
    dig = np.shape(data)[1]
    alpha = np.ones(k)
    mu = np.zeros((k, dig))
    sigma = np.zeros((k, dig, dig))
    for num in range(k):
        alpha[num] = 1.0 / float(k)
        mu[num, :] = np.random.uniform(np.min(data), np.max(data), dig)
        sigma[num, :, :] = np.identity(dig)
    return alpha, mu, sigma

def EM_Algorithm(data, weight, mu, sigma):
    series = np.empty_like(data)
    while 1:
        temp_1 = sigma.copy()
        for num in range(2):
            d = np.shape(data)[1] / 2.0
            para = 1 / (np.power(np.pi, d) * np.sqrt(np.linalg.det(sigma[num, :, :])))
            sigma_prime = np.linalg.pinv(sigma[num, :, :])
            para = para * np.exp(-0.5 * np.sum(np.dot((data - mu[num, :]), sigma_prime) * (data - mu[num, :]), axis=1))
            series[:, num] = para
        series = series / (np.sum(series * weight, axis=1)).reshape(len(series * weight), 1)
        for row in range(2):
            temp = 0
            weight[row] = np.sum(series[:, row]) / len(data)
            mu[row, :] = np.sum(series[:, row].reshape(len(series), 1) * data, axis=0) / np.sum(series[:, row])
            for num in range(len(data)):
                temp += series[num, row] * np.dot((data[num, :] - mu[row, :]).reshape(len(mu[row, :]), 1),(data[num, :] - mu[row, :]).reshape(1, len(mu[row, :])))
                sigma[row, :, :] = temp / np.sum(series[:, row])
        if (abs(sigma - temp_1) < 1e-8).all(): break
    return weight, mu, sigma


cov1 = np.mat("0 0.2;0.2 0")
cov2 = np.mat("0.3 0;0 0.3")
mu1 = np.array([0.3, 0.5])
mu2 = np.array([1, -0.5])

sample = np.zeros((100, 2))
sample[:50, :] = np.random.multivariate_normal(mean=mu1, cov=cov1, size=50)
sample[50:, :] = np.random.multivariate_normal(mean=mu2, cov=cov2, size=50)
np.savetxt("data.txt", sample)
data = np.loadtxt("data.txt")

plt.subplot(2, 1, 1)
plt.title("GMM Clustering")
plt.plot(sample[:50, 0], sample[:50, 1], "bo", label="alpha = 0.5, mean = (0.3,0.5)")
plt.plot(sample[50:, 0], sample[50:, 1], "ro", label="alpha = 0.5, mean = (1,-0.5)")
plt.legend()
plt.xlim(-1, 4)
plt.ylim(-2, 2)

init_alpha, init_mu, init_sigma = init(data, 2)
alpha, mu, sigma = EM_Algorithm(data, init_alpha, init_mu, init_sigma)

for num in range(2):
    print("The weight of model %d is: %.3f, \n mean is :%s,\n cov is :%r" % (num + 1, alpha[num], mu[num], sigma[num]))
n = 100
x = np.linspace(-1, 3, n)
y = np.linspace(-2, 2, n)
var1 = multivariate_normal(mean=mu[0], cov=sigma[0])
var2 = multivariate_normal(mean=mu[1], cov=sigma[1])

plt.subplot(2, 1, 2)
plt.plot(data[:, 0], data[:, 1], "ro")
p = contour_plot(x, y, alpha, var1, var2)
plt.contourf(x, y, p, 20, alpha=.75)
plt.colorbar()
plt.show()
