import os
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'advertisement_clicks.csv')
df = pd.read_csv(path)
control = df[df.advertisement_id == 'A']
test = df[df.advertisement_id == 'B']

control_obs = len(control)
test_obs = len(test)

control_sum = control.action.sum()
test_sum = test.action.sum()

control_mean = control.action.mean()
test_mean = test.action.mean()

control_std = control.action.std()
test_std = test.action.std()

# Standard t test
t1, p1 = stats.ttest_ind(control.action, test.action)

# Welch's t test
t2, p2 = stats.ttest_ind(control.action, test.action, equal_var=False)

# Proportions z test
count = np.array([control_sum, test_sum])
nobs = np.array([control_obs, test_obs])
stat, pval = proportions_ztest(count, nobs)


print('number of observations in control:', len(control))
print('number of observations in test:', len(test))

print('sum of control:', control.action.sum())
print('sum of test:', test.action.sum())

print('mean of control:', control.action.mean())
print('mean of test:', test.action.mean())

print('std of control:', control.action.std())
print('std of test:', test.action.std())

print("standart ttest", "t = {:.10f}".format(t1), "p = {:.6f}".format(p1))
print("welch's ttest", "t = {:.10f}".format(t2), "p = {:.6f}".format(p2))
print('proportions z test p = {0:0.6f}'.format(pval))




