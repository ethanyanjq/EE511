import numpy as np


def vector_generate(mu, sigma, n):
    cho_dec = np.linalg.cholesky(sigma)
    vector = []
    for i in range(n):
        temp = np.array(np.random.rand(3))
        temp = np.dot(cho_dec, temp.T)
        vector.append(temp.tolist())
    return vector


mu = np.array([1, 2, 3])
sigma = np.array([[3, -1, 1], [-1, 5, 3], [1, 3, 4]])

a = vector_generate(mu, sigma, 10)
print(a)
