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


def init_params(data, k):
    dim = np.shape(data)[1]
    min_num = np.min(data)
    max_num = np.max(data)
    alpha = np.ones(k)
    mu = np.zeros((k, dim))
    sigma = np.zeros((k, dim, dim))
    for num in range(k):
        alpha[num] = 1.0 / float(k)
        mu[num, :] = np.random.uniform(min_num, max_num, dim)
        sigma[num, :, :] = np.identity(dim)
    return alpha, mu, sigma


def guassian(x, mu, sigma):
    d = np.shape(x)[1] / 2.0
    coefficent = 1 / (np.power(np.pi, d) * np.sqrt(np.linalg.det(sigma)))
    sigma_inverse = np.linalg.pinv(sigma)
    coefficent *= np.exp(-0.5 * np.sum(np.dot((x - mu), sigma_inverse) * (x - mu), axis=1))
    return coefficent


def gmm_em(data, k, alpha, mu, sigma):
    guass_array = np.empty_like(data)
    while True:
        temp_sigma = sigma.copy()
        for num in range(K):
            guass_array[:, num] = guassian(data, mu[num, :], sigma[num, :, :])
        guass_array = guass_array * alpha
        guass_array_sum = (np.sum(guass_array, axis=1)).reshape(len(guass_array), 1)
        guass_array = guass_array / guass_array_sum
        for row in range(K):
            temp = 0
            alpha[row] = np.sum(guass_array[:, row]) / len(data)
            mu[row, :] = np.sum(guass_array[:, row].reshape(len(guass_array), 1) * data, axis=0) / np.sum(
                guass_array[:, row])
            for num in range(len(data)):
                temp += guass_array[num, row] * np.dot((data[num, :] - mu[row, :]).reshape(len(mu[row, :]), 1),
                                                       (data[num, :] - mu[row, :]).reshape(1, len(mu[row, :])))
                sigma[row, :, :] = temp / np.sum(guass_array[:, row])

        if (abs(sigma - temp_sigma) < 1e-8).all():
            break
    return alpha, mu, sigma


cov1 = np.mat("0 0.2;0.2 0.1")
cov2 = np.mat("0.3 0.1;0.1 0.2")
mu1 = np.array([0.3, 0.5])
mu2 = np.array([1, -0.5])

sample = np.zeros((100, 2))
sample[:50, :] = np.random.multivariate_normal(mean=mu1, cov=cov1, size=50)
sample[35:, :] = np.random.multivariate_normal(mean=mu2, cov=cov2, size=65)
np.savetxt("data.txt", sample)
data = np.loadtxt("data.txt")

plt.subplot(2, 1, 1)
plt.title("GMM Clustering")
plt.plot(sample[:50, 0], sample[:50, 1], "bo", label="alpha = 0.35, mean = (0.3,0.5)")
plt.plot(sample[35:, 0], sample[35:, 1], "ro", label="alpha = 0.65, mean = (1,-0.5)")
plt.legend()
plt.xlim(-1, 4)
plt.ylim(-2, 2)

K = 2
init_alpha, init_mu, init_sigma = init_params(data, K)
alpha, mu, sigma = gmm_em(data, K, init_alpha, init_mu, init_sigma)

for num in range(K):
    print("The weight of model %d is: %.3f, mean is :%s,\n cov is :\n%r" % (num + 1, alpha[num], mu[num], sigma[num]))
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
