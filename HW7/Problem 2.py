import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm


def one_dim_gmm(alpha1, alpha2, mu, sigma, n):
    series = []
    for i in range(int(n / 10)):
        series = series + np.random.normal(mu[0], sigma[0], int(alpha1 * 10)).tolist()
        series = series + np.random.normal(mu[1], sigma[1], int(alpha2 * 10)).tolist()
    return series


x = np.linspace(-5, 5, 100)
y1 = np.array(norm(-1, 1).pdf(x))
y2 = np.array(norm(1, 1).pdf(x))
y = 0.4 * y1 + 0.6 * y2
plt.plot(x, y.tolist(), 'r-', lw = 2, label="Theoretical pdf")
plt.legend()
a = one_dim_gmm(0.4, 0.6, [-1, 1], [1, 1], 1000)
plt.hist(a, bins=50, density=1)
plt.show()
