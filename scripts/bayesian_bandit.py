import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import beta

'''
Ref: https://github.com/lazyprogrammer/machine_learning_examples/blob/master/ab_testing/bayesian_bandit.py

Explanation: 

You have three bandits, each of them has different probabilities (variable: bandit_prob) 
These probabilities have beta distribution. 

Select a random variable from beta distribution for each bandit and select the maximum one which is best_bandit. 

Play for this bandit. 

You can either win or loose. Function random_output will be used for win or loose state. 
If x =1 (win), then increase the value of 'a' by 1, else, increase the value of 'b' by 1. 

After 2000 trials, you will see from the plot that the best machine has lowest variance and exploited a lot.

'''

num_trials = 2000
bandit_prob = [0.2, 0.5, 0.75]


class Bandit(object):

    def __init__(self, p):
        self.p = p
        self.a = 1
        self.b = 1

    def random_output(self):
        return np.random.random() < self.p

    def sample_from_beta(self):
        return np.random.beta(self.a, self.b)

    def update_params(self, x):
        self.a += x
        self.b += 1-x


def plot_bandit(bandits, trial):
    x = np.linspace(0, 1, 200)
    for b in bandits:
        y = beta.pdf(x, b.a, b.b)
        plt.plot(x, y, label="real p: %.4f"%b.p)

    plt.title("Bandit distributions after %s trials" % trial)
    plt.legend()
    plt.show()


def experiment():
    bandits = [Bandit(p) for p in bandit_prob]
    trial_numbers = [5,10,20,50,100,200,500,1000,1500,1999]

    for i in range(num_trials):
        best_bandit = None
        max_sample = -1
        all_samples = []
        for bandit in bandits:
            sample = bandit.sample_from_beta()
            all_samples.append(sample)

            if sample > max_sample:
                max_sample = sample
                best_bandit = bandit

        if i in trial_numbers:
            print("current_samples: %s " % all_samples)
            plot_bandit(bandits, i)

        x = best_bandit.random_output()
        best_bandit.update_params(x)


if __name__ == '__main__':
    experiment()
