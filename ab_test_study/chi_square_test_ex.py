
'''
This file aims to explain Chi Square test.
Let's say there are two different websites, A and B. We've collected the number of clicks and impression values.
non-click = imp -click

Create the contingency (two-way) table:


|    | click  | noclick  | total  |
|--- |------- |----------|------- |
|A   | a      | c        |        |
|B   | b      | d        |        |
|--- |------- |----------|--------|
total|        |          |        |


* One way to calculate the chi-square value is using the click and non_click values and apply them to the formula below:
chi_square = (ad - bc)^2 (a+b+c+d) / (a+b)(b+c)(a+c)(b+d)

* The other method is using the chi_square formula. We need to calculate expected values of each cell.
chi square = sum [(observed value - expected value)**2 / expected_value]



All calculations below are using this raw table:
|   | click | noclick  | impression  | CTR  |
|---|-------|----------|------------ |      |
|A  | 36    | 14       |  50         | 0.72 |
|B  | 30    | 25       |  55         | 0.54 |
|---|-------|----------|-------------|      |
|   |66     | 39       | 105         | 0.63 |

'''

from scipy.stats import chi2, chi2_contingency
import numpy as np

click_A = 36
non_click_A = 14
impression_A = 50
CTR_A = click_A / impression_A

click_B = 30
non_click_B = 25
impression_B = 55
CTR_B = click_B / impression_B

click_all = 66
non_click_all = 39
impression_all = 105
CTR_all = click_all / impression_all
non_click_ratio_all = non_click_all / impression_all


# Expected values:
expected_click_A = impression_A * CTR_all
expected_non_click_A = impression_A * non_click_ratio_all

expected_click_B = impression_B * CTR_all
expected_non_click_B = impression_B * non_click_ratio_all

'''
Expected values result:
|   | click  | noclick  | impression  | CTR  |
|---|------- |----------|------------ |      |
|A  | 31.429 | 18.571   |  50         | 0.63 |
|B  | 34.571 | 20.428   |  55         | 0.63 |
|---|------- |----------|-------------|      | 
|   |66      | 39       | 105         | 0.63 |
'''

# First method: calculate chi_square using raw values:
chi_square_1 = ((click_A * non_click_B - non_click_A * click_B)**2 * impression_all) / \
              (click_all * non_click_all * impression_A * impression_B)

p_value_1 = 1 - chi2.cdf(x=chi_square_1, df=1)


# Second method: calculate chi_square using the raw values as a table:
T = np.zeros((2, 2)).astype(np.float32)
T[0, 0] = click_A
T[0, 1] = non_click_A

T[1, 0] = click_B
T[1, 1] = non_click_B

det = T[0, 0] * T[1, 1] - T[0, 1] * T[1, 0]
chi_square_2 = float(det) / T[0].sum() * det / T[1].sum() * T.sum() / T[:, 0].sum() / T[:, 1].sum()
p_value_2 = 1 - chi2.cdf(x=chi_square_2, df=1)


# Third method: calculate chi_square using the raw values as a table with packages:
chi_square_3, p_value_3, _, _ = chi2_contingency(T, correction=False)


# Fourth method: calculate chi_square using  expected values:
chi_square_4 = (click_A - expected_click_A)**2 / expected_click_A + \
             (click_B - expected_click_B)**2 / expected_click_B + \
             (non_click_A - expected_non_click_A)**2 / expected_non_click_A + \
             (non_click_B - expected_non_click_B)**2 / expected_non_click_B

p_value_4 = 1 - chi2.cdf(x=chi_square_4, df=1)




