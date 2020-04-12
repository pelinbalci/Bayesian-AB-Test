## Bayesian vs Frequentist Approach

Let's model the height of the student in a class as gaussian. We must find the mean and the variance. 

There are two approach for modeling a dataset:
The Frequestist Approach:
- Collect the data. 
- Find the params ( mu, sigma square) which maximize the likelihood of the dataset. 

The Bayesian Approach:
- We don't solve for mean and variance. Instead, we find the distribution --> P(mean & variance given dataset) 


Statistics Route spends a lot of time with sampling. Sampling is a numerical approach of integral. 
In ML route, we will look at Bayesian perspective. A simple example: We will not focus the numeric value of w but the 
distribution of w in simple linear regression problem --> y = W.T * x


Let's model the CTR values with frequestist approach:

We've collected the dataset and calculated the mean of CTR of our customer. Central Limit Theorem says the sum of IID 
(Independent, Identically Distributed) random variables tends to Gaussian distribution. And as we collect more data, 
mean of CTR will become more accurate since the variance decrease.
Now, we want to know how accurate that estimate of CTR is. We will use Confidence Interval method which is a method of 
deasing with uncertainty of measurements of parameters to calculate accuracy.

The key point here is estimated CTR is a distribution, estimated mean is around a variable since it is sum of IID 
random variables. Estimated CTR has a gaussian distribution due to CLT. 


Frequentist Statistics:
- paramters of distributions are set, we don't know them yet. Data is randomly generated via those 
distributions/parameters. 

        We can model param = argmax param P(data | param)

Bayesian Statistics:
- parameters are random variables that have distributions. Data is fixed. 
    
        We can model P(param | data)


Another explanation: 
(https://math.stackexchange.com/questions/2126662/what-do-the-two-things-such-that-data-is-fixed-and-parameters-vary-in-bayesi)

"Under a frequentist point of view you might have an unknown parameter, say 𝜃, that you want to estimate based on some 
data you have collected. You assume that this true and unknown parameter is fixed. Your data are expressed through 
a random variable, say 𝑋. So, for example you are interested in maximizing a likelihood based on the probability 
density function 𝑓(𝑋∣𝜃). This means that you model your collected data under a belief that the probability function 
of your data depends on that unknown parameter. You then can estimate that parameter say by maximizing the likelihood 
of the data (i.e. you consider the data random, in a sense that there are a random realization of the population that 
you study).

Under a bayesian point of view things are a bit reversed. You do not view the parameter 𝜃 as an unknown constant, i.e. 
fixed at some value, that you try to estimate. You rather consider that the parameter itself has a marginal distribution
𝑓(𝜃) which is called a prior. This expresses you prior beliefs regarding the parameter which now is viewed as a random 
variable since it follows a distribution. Under such a framework you might be interested in modelling 𝑓(𝜃∣𝑋), 
namely update your knowledge for 𝜃 GIVEN the data you have collected. Since now the data are given, they are not 
random hence the "data is fixed" that your lecturer mentioned."

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










