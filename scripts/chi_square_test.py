import os
import pandas as pd
import numpy as np
from scipy.stats import chi2

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

T = np.zeros((2, 2)).astype(np.float32)
T[0, 0] = control_sum
T[0, 1] = control_obs - control_sum

T[1, 0] = test_sum
T[1, 1] = test_obs - test_sum

det = T[0, 0]*T[1, 1] - T[0, 1]*T[1, 0]
c2 = float(det) / T[0].sum() * det / T[1].sum() * T.sum() / T[:,0].sum() / T[:,1].sum()
p = 1 - chi2.cdf(x=c2, df=1)


print('number of observations in control:', len(control))
print('number of observations in test:', len(test))

print('sum of control:', control.action.sum())
print('sum of test:', test.action.sum())

print('mean of control:', control.action.mean())
print('mean of test:', test.action.mean())

print('std of control:', control.action.std())
print('std of test:', test.action.std())
print("p = {:.6f}".format(p))
