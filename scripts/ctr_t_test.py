import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("/Users/pelin.balci/PycharmProjects/Bayesian-AB-Test/scripts/advertisement_clicks.csv", sep = ",")
control = df[df.advertisement_id == 'A']
test = df[df.advertisement_id == 'B']

print(control.head())

print('number of observations in control:', len(control))
print('number of observations in test:', len(test))

control_obs = len(control)
test_obs = len(test)

control_sum = control.action.sum()
test_sum = test.action.sum()

control_mean = control.action.mean()
test_mean = test.action.mean()

control_std = control.action.std()
test_std = test.action.std()


print('sum of control:', control.action.sum())
print('sum of test:', test.action.sum())

print('mean of control:', control.action.mean())
print('mean of test:', test.action.mean())

print('std of control:', control.action.std())
print('std of test:', test.action.std())

t1, p1 = stats.ttest_ind(control.action, test.action)
print("standart ttest", "t1 = {:.10f}".format(t1), "p1 = {:.6f}".format(p1))


t2, p2 = stats.ttest_ind(control.action, test.action, equal_var=False)
print("welch's ttest", "t2 = {:.10f}".format(t2), "p2 = {:.6f}".format(p2))

import numpy as np
from statsmodels.stats.proportion import proportions_ztest
count = np.array([control_sum, test_sum])
nobs = np.array([control_obs, test_obs])
stat, pval = proportions_ztest(count, nobs)
print('{0:0.6f}'.format(pval))




