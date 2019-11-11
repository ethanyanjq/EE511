import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal


def contour_graph(x, y, alpha, var1, var2):
    p = []
    for i in range(len(x)):
        for j in range(len(y)):
            p.append(alpha[0] * var1.pdf([x[i], y[j]]) + alpha[1] * var2.pdf([x[i], y[j]]))
    p = np.array(p)
    p = p.reshape((len(x), -1))
    return p.T


def gaussian(x, mean, cov):
    d = len(x)
    x1 = np.array(x) - np.array(mean)
    x1_T = x1.T
    x1_T = x1_T.tolist()
    x1 = x1.tolist()
    inv = np.linalg.inv(cov)
    temp1 = np.dot(x1, inv)
    return (1 / (np.sqrt((2 * np.pi) ** d * np.linalg.det(cov))) *
            np.exp(-np.dot(temp1, x1_T) / 2))


def init_params(data, k):
    """初始化参数
    输入:data表示待估计的样本，k代表类别数
    alpha:类型是一维数组，每个元素对应相应模型的权重值
    mu:类型是二维数组，每一行对应相应模型的均值
    sigma:类型是三维数组，每个二维数组对应其模型的协方差矩阵
    """
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
    """多维高斯分布概率密度函数
    输入:x表示样本，mu表示均值，sigma表示协方差矩阵
    """
    d = np.shape(x)[1] / 2.0
    coefficent = 1 / (np.power(np.pi, d) * np.sqrt(np.linalg.det(sigma)))
    sigma_inverse = np.linalg.pinv(sigma)
    coefficent *= np.exp(-0.5 * np.sum(np.dot((x - mu), sigma_inverse) * (x - mu), axis=1))
    return coefficent


def gmm_em(data, k, alpha, mu, sigma):
    """高斯混合模型期望最大算法(GMM-EM)
    """
    guass_array = np.empty_like(data)  # 存储每个样本对每个模型的响应度
    while True:
        # temp_alpha = alpha.copy()
        # temp_mu = mu.copy()
        temp_sigma = sigma.copy()  # 用于判定是否可以跳出循环
        # E-Step:计算每个样本对每个模型的响应度，对应《统计学习方法》里的$gam_{jk}$
        for num in range(K):
            guass_array[:, num] = guassian(data, mu[num, :], sigma[num, :, :])
        guass_array = guass_array * alpha
        guass_array_sum = (np.sum(guass_array, axis=1)).reshape(len(guass_array), 1)
        guass_array = guass_array / guass_array_sum
        # M-Step:迭代模型参数，对应《统计学习方法》里的$alpha_{k},mu_{k},sigma_{k}$
        for row in range(K):
            temp = 0
            alpha[row] = np.sum(guass_array[:, row]) / len(data)
            mu[row, :] = np.sum(guass_array[:, row].reshape(len(guass_array), 1) * data, axis=0) / np.sum(
                guass_array[:, row])
            for num in range(len(data)):
                temp += guass_array[num, row] * np.dot((data[num, :] - mu[row, :]).reshape(len(mu[row, :]), 1),
                                                       (data[num, :] - mu[row, :]).reshape(1, len(mu[row, :])))
                sigma[row, :, :] = temp / np.sum(guass_array[:, row])

        if (abs(sigma - temp_sigma) < 1e-10).all():
            break
    return alpha, mu, sigma


if __name__ == "__main__":
    cov1 = np.mat("0 0.2;0.2 0.1")
    cov2 = np.mat("0.3 0.1;0.1 0.2")
    mu1 = np.array([0.3, 0.5])
    mu2 = np.array([1, -0.5])

    sample = np.zeros((100, 2))
    sample[:50, :] = np.random.multivariate_normal(mean=mu1, cov=cov1, size=50)
    sample[35:, :] = np.random.multivariate_normal(mean=mu2, cov=cov2, size=65)
    np.savetxt("data.txt", sample)
    data = np.loadtxt("data.txt")  # 导入样本

    plt.subplot(2, 1, 1)
    plt.title("GMM Clustering")
    plt.plot(sample[:50, 0], sample[:50, 1], "bo", label="alpha = 0.35, mean = (0.3,0.5)")
    plt.plot(sample[35:, 0], sample[35:, 1], "ro", label="alpha = 0.65, mean = (1,-0.5)")
    plt.legend()
    plt.xlim(-1, 4)
    plt.ylim(-2, 2)

    K = 2  # 类别数
    init_alpha, init_mu, init_sigma = init_params(data, K)
    alpha, mu, sigma = gmm_em(data, K, init_alpha, init_mu, init_sigma)

    for num in range(K):
        print("第 %d 个模型的权重系数为:%.3f, 其均值为:%s, 协方差矩阵为:\n%r" % (num + 1, alpha[num], mu[num], sigma[num]))
    n = 100
    x = np.linspace(-1, 3, n)
    y = np.linspace(-2, 2, n)
    var1 = multivariate_normal(mean=mu[0], cov=sigma[0])
    var2 = multivariate_normal(mean=mu[1], cov=sigma[1])

    plt.subplot(2, 1, 2)
    plt.plot(data[:, 0], data[:, 1], "ro")
    p = contour_graph(x, y, alpha, var1, var2)
    plt.contourf(x, y, p, 20, alpha=.75)
    plt.colorbar()
    plt.show()