Notes from Bayesian Machine Learning in Python: A/B Testing by Lazy Programmer- Udemy

Let's model the height of the student in a class as gaussian. We must find the mean and the variance. 

There are two approach for modeling a dataset:
The Frequestist Approach:
- Collect the data. 
- Find the params ( mu, sigma square) which maximize the likelihood of the dataset. 

The bayesian Approach:
- We don't solve for mean and variance. Instead, we find the distribution --> P(mean & variance given dataset) 


Statistics Route spends a lot of time with sampling. Sampling is a numerical approach of integral. 
In ML route, we will look at Bayesian perspective. A simple example: We will not focus the numeric value of w but the distribution of w in simple linear regression problem --> y = W.T * x


Let's model the CTR values with frequestist approach:

We've collected the dataset and calculated the mean of CTR of our customer. Central Limit Theorem says the sum of IID (Independent, Identically Distributed) random variables tends to Gaussian distribution. And as we collect more data, mean of CTR will become more accurate since the variance decrease.
Now, we want to know how accurate that estimate of CTR is. We will use Confidence Interval method which is a method of dealsing with uncertainty of measurements of parameters to calculate accuracy.

The key point here is estimated CTR is a distribution, estimated mean is around a variable since it is sum of IID random variables. Estimated CTR has a gaussian distribution due to CLT. 


Frequentist Statistics:
- paramters of distributions are set, we don't know them yet. Data is randomly generated via those distributions/parameters. 
We can model param = argmax param P(data | param)

Bayesian Statistics:
- parameters are random variables that have distributions. Data is fixed. 
We can model P(param | data)


Another explanation: 
(https://math.stackexchange.com/questions/2126662/what-do-the-two-things-such-that-data-is-fixed-and-parameters-vary-in-bayesi)

"Under a frequentist point of view you might have an unknown parameter, say 𝜃, that you want to estimate based on some data you have collected. You assume that this true and unknown parameter is fixed. Your data are expressed through a random variable, say 𝑋. So, for example you are interested in maximizing a likelihood based on the probability density function 𝑓(𝑋∣𝜃). This means that you model your collected data under a belief that the probability function of your data depends on that unknown parameter. You then can estimate that parameter say by maximizing the likelihood of the data (i.e. you consider the data random, in a sense that there are a random realization of the population that you study).

Under a bayesian point of view things are a bit reversed. You do not view the parameter 𝜃 as an unknown constant, i.e. fixed at some value, that you try to estimate. You rather consider that the parameter itself has a marginal distribution 𝑓(𝜃) which is called a prior. This expresses you prior beliefs regarding the parameter which now is viewed as a random variable since it follows a distribution. Under such a framework you might be interested in modelling 𝑓(𝜃∣𝑋), namely update your knowledge for 𝜃 GIVEN the data you have collected. Since now the data are given, they are not random hence the "data is fixed" that your lecturer mentioned."
