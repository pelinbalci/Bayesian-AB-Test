## Frequentist A/B Testing

p value = the probability of obtaining a result under the null hypothesis is true. 

example question: Is the difference in mean height between men and women statistically significant of significance 
level alpha? 


### T Statistics

X1 = mean of 1st group
X2 = mean of 2nd group
pool_std = pool standart deviation
N = Sample size 

- If the sample sizes of the two groups are the same and the standart deviation of two group is the same and the 
assumed distribution is gaussian:

        t = (X1 - X2) / pool_std * sqrt(2/N)

- If the sample sizes of the two groups are different but the standart deviation of two group is the same and the 
assumed distribution is gaussian:

        t = (X1 - X2) / pool_std * sqrt(1/N1 + 1/N2)

- If the standart deviations of two groups are different but the assumed distribution is gaussian: 
        
        use Welch's t test. 

- If you don't want to assume a distribution you can use:

        - Kolmogorov Smirnov Test 
        - Kruskal Wallis Test
        - Mann Whitney U Test 
    
  These are distribution free/ non parametric tests.  
  
  The problem here is that less assumption means less power. You need more extreme difference to get statistically 
  significant p value. 
  
  
#### How t changes with sample size and standart deviation? 

    bigger N ---> bigger t ----> smaller p value 
    bigger pool_std ---> smaller t ---->  bigger p value 

t statistic depends on N. Therefore, it is not correct to say small values of N makes the finding false. 
If you are trying to find statistically significant difference you will need to collect more data and with more data 
the pooled standart deviation will become small. 


#### One sided or two sided t test? 

If you want to test a new drug's effect on people it is better (ethical) to use 2 sided t test, then you can mesaure 
if the effect of drug is better or worse.

But if you already have an effective drug and you want to test if a new drug is better, you can use 1 sided t test. 

#### Welch's t test 

stats.ttest_ind(control, test, equal_var = False)

### Chi Square Test

Chi Square is always positive (this is a one sided test)
        
    p value = 1- cdf(chi square value) 

That means we need a high chi square value to get a small p value. 

### More Than Two Groups 

Use Bonferroni Correction. 

alpha should be re-calculated with the number of tests. 

If you apply pairwise testing; alpha = alpha/ number of tests 

If you apply one vs the rest; alpha = alpha / N 

### Statistical Power 

|   | reject H0 (pred=1)  | not reject Ho (pred=0)  |
|---|---|---|
| Ho is true (disase = 0)  | FP  | TN  |  
| H1 is true (disase = 1) | TP  | FN  | 


        Sensitivity = TP / TP + FN
        Specifity = TN / TN + FP 
        Precision = TP / TP + FP 


#### Evaluation of Precision:

Ho: disease = 0  
H1: disease =1

TP shows that we reject the null hypothesis correctly (when disease actually exists, H1 is true) our prediction 
is disease exists. 

FP shows that we reject the null hypothesis mistakenly (when there is no disease, Ho is true) our prediction 
is disease exists. 

      Precision = TP / TP + FP 
                = P(pred = 1, disease =1) / P ( pred = 1) 
                = P( disease =1 | pred =1)
                = P(H1 is true | reject Ho)

Precision gives us the probability of disease when the prediction is 1.

#### When H1 is true, our decision can be TP or FN. 

    Beta = FN/ TP + FN 
    Sensitivity(Power) = TP / TP + FN
                       = 1- Beta
                       = P(pred = 1, disease =1) / P ( disease = 1)
                       = P( pred = 1| disease = 1)
                       = P(reject Ho | H1 is true)

Sensitivity shows that we reject the null hypothesis correctly.


Power Analysis can be used to determine the number of samples. 

#### todo: add more resource for power analysis. 


### Summary

- t test can be used for Gaussian distributed data. 

- There are other tests 'non-parametric' that don't make distribution assumptions. 

- Remember this: less assumptions ---> less power. 

Steps of t test:

- Define null and alternative hypothesis 
- Use means of two groups and pool standart deviation to calculte t value. 
- P value gives you the result, reject or do not reject the null hypothesis 
- If there is a difference between control and test group but you fail to reject the null may be you need more data. 
- If the variance is large you need more data again to detect the difference. 
- More data means more power. 


Don't forget:

- If you are doing repeated test, use Bonferroni correction.
- Don't stop test early (before the test duration), when you see a significant p value, it increases the chance of 
False Positive. 
