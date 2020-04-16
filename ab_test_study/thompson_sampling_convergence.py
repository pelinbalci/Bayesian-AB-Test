import matplotlib.pyplot as plt
import numpy as np
from ab_test_study.bayesian_bandit import Bandit

def run_experiment(p1, p2, p3, N):

    bandits = Bandit(p1), Bandit(p2), Bandit(p3)

    data = np.empty(N)

    for i in range(N):
        j = np.argmax([bandit.sample_from_beta() for bandit in bandits]) # j is the bandit which gives max from the sample
        x = bandits[j].random_output() # x is the value of 1 or 0 when j is played.
        bandits[j].update_params(x) # j's params (a or b) are updated.

        data[i] = x

    cumulative_average_ctr = np.cumsum(data) / (np.arange(N) + 1)

    plt.plot(cumulative_average_ctr)
    plt.plot(np.ones(N) * p1)
    plt.plot(np.ones(N) * p2)
    plt.plot(np.ones(N) * p3)
    plt.ylim((0,1))
    plt.xscale('log')

    plt.show()


run_experiment(0.3, 0.35, 0.4, 100000)


