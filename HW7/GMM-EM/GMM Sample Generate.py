import numpy as np
import matplotlib.pyplot as plt

cov1 = np.mat("0.3 0;0 0.1")
cov2 = np.mat("0.2 0;0 0.3")
mu1 = np.array([0, 1])
mu2 = np.array([2, 1])

sample = np.zeros((100, 2))
print(sample)
sample[:60, :] = np.random.multivariate_normal(mean=mu1, cov=cov1, size=60)
sample[50:, :] = np.random.multivariate_normal(mean=mu2, cov=cov2, size=50)
np.savetxt("data.txt", sample)

plt.plot(sample[:30, 0], sample[:30, 1], "bo")
plt.plot(sample[30:, 0], sample[30:, 1], "rs")
plt.show()
