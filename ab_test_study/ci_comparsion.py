import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta, norm


T = 501
true_ctr = 0.5
a, b = 1, 1,
plot_indices = [10, 20, 30, 50, 100, 200, 500]

data = np.empty(T)
for i in range(T):
    x = 1 if np.random.random() < true_ctr else 0
    data[i] = x

    a += x
    b += 1-x

    if i in plot_indices:
        p = data[:i].mean()
        n = i+1
        std = np.sqrt(p*(1-p) / n)

        # plot the gaussian
        x = np.linspace(0, 1, 200)

        gaussian = norm.pdf(x, loc = p, scale = std)
        plt.plot(x, gaussian, label = 'gaussian approx')

        posterior = beta.pdf(x, a=a, b=b)
        plt.plot(x, posterior, label = 'beta posterior')

        plt.legend()
        plt.title('N = %s' % n)
        plt.show()