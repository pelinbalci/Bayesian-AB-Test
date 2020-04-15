## BAYESIAN A/B TESTING

### Multi - Armed Bandit Problem 

"In probability theory, the multi-armed bandit problem (sometimes called the K- or N-armed bandit problem) is a 
problem in which a fixed limited set of resources must be allocated between competing (alternative) choices in a way 
that maximizes their expected gain, when each choice's properties are only partially known at the time of allocation, 
and may become better understood as time passes or by allocating resources to the choice. This is a classic 
reinforcement learning problem that exemplifies the exploration–exploitation tradeoff dilemma. 

The name comes from imagining a gambler at a row of slot machines (sometimes known as "one-armed bandits"), 
who has to decide which machines to play, how many times to play each machine and in which order to play them, 
and whether to continue with the current machine or try a different machine. 

The multi-armed bandit problem also falls into the broad category of stochastic 
scheduling." (https://en.wikipedia.org/wiki/Multi-armed_bandit)


If you teach a machine to play this game, it will models the rewards of each machine. And these calculated rewards come 
from its actions. After collecting a lot of data, reward estimations will be accurate. Data collection is expensive in 
the mean of time and money. 


Here comes the dilemma. 

        > Exploration: 
        We must play all the machines to collect enough data to be confident about win (or reward) rates.
        Think about an A/B test for your website between current design and new design. One of them would get 
        higher CTR. However, while collecting the data you show the suboptimal design to too many customers. 
         
        > Explotation:
         We want to play only the machine to maximize our winnings. But you don't know the best machine unless collecting 
        a lot of data.

Adaptive methods of solving the Explore & Exploit Dilemma:

        > Epsilon Greedy Algorithm 
        > UCB1 (Upper Confidence Bound) Algorithm 
        
        
### Epsilon Greeedy Algorithm

You will not blindly serve A and B to the equal number of times. For example if performs better, show it more. That means
you will adapt the data you've collected so far. 

You can still perform traditional A/B testing after collecting the data in this way. As you remember Chi Square Test 
supports the different numbers of observations. 

Pseudo Code: 

        epsilon = 0.1
        
        if rand() < epsilon:
            "explore" --> show random ad. 
        
        else:
            "exploit" --> show the ad which has max ctr. 
            
            
Check this to see a better code:) 
(https://github.com/lilianweng/multi-armed-bandit/blob/master/solvers.py#L48)


### UCB1 Algorithm 

Find upper bounds with Chernoff - Hoeffding Bound:

&epsilon; >0

P(&mu;<sup>*</sup> < &mu; - &epsilon;) <= exp(-2&epsilon;<sup>2</sup>N)

P(|&mu;<sup>*</sup> - &mu;| <= - &epsilon;) > 1-  2exp(-2&epsilon;<sup>2</sup>N)

j<sup>*</sup>  = argmax(&mu; <sub>j</sub> + sqrt(2ln N / N<sub>j</sub>))

- If &mu; <sub>j</sub> is high; exploit j more often. 
- If N is high but  N<sub>j</sub> is low, then continue to explore. 
- While N --> infinity lnN / N<sub>j</sub> --> 0. Then we use only &mu; <sub>j</sub>. 

Check this code: 
(https://github.com/lilianweng/multi-armed-bandit/blob/master/solvers.py#L79)


## Conjugate Priors

When we use frequentist approach; we measure parameters like mean or CTR --> these are point estimates. 

But this doesn't take into account that how certain we were about this estimation. The solution is by using CLT 
be sure that Confidence Interval is gaussian. Then we get the lower and upper bounds in %95 area. What we are doing is 
solving a maximum likelihood problem, finding the paramaters which maximizes the likelihood of the data: 

maximum likelihood => &theta;<sup>*</sup> = argmax<sub>&theta;</sub>P(X|&theta;)


Bayesian Statistics treat &theta; as a random variable; it has its own distribution and shape of this distribution tells
us how confident we are of any value of the parameter.

P(&theta; | X) = P(X | &theta;) * P(&theta;) / P(X)   
- P(&theta;) -> prior probability(old beliefs about params)
- P(X | &theta;) -> likelihood of the data
- P(&theta; | X) -> posterior probability (new beliefs about params after seeing the data)
 
### CTR example:
       
CTR --> P(X | &theta;) distribution is bernoulli.

distribution of P(X | &theta;) --> &Pi; &theta; <sup>Xi</sup> (1- &theta; <sup>1-Xi</sup>)
 
&theta; is probaility of getting click [0,1] Beta distribution gives the value between 0 and 1. 

Below you can find the Beta Distribution and its relation with Gamma function:

Beta(a, b) = &theta;<sup>a-1</sup> (1- &theta;<sup>b-1</sup>) / B(a,b)

B(a,b) = &Gamma;(a)&Gamma;(b) / &Gamma;(a+b)

&Gamma;(a) = (a-1)!

How can we find the distribution of P(&theta; | X) ? We can use the bayesian formula and ignore the denominator (P(X)) 
partcsince it doesn't depend on &theta;.

P(&theta; | X) ~ P(X | &theta;) * P(&theta;)

P(&theta; | X)  ~ (&Pi; &theta; <sup>Xi</sup> (1- &theta; <sup>1-Xi</sup>)) &theta;<sup>a-1</sup> (1- &theta;<sup>b-1</sup>)

P(&theta; | X) ~&theta;<sup>a-1 + &Sum; Xi</sup> (1- &theta;<sup>b-1 + &Sum; (1-Xi) </sup>)

P(&theta; | X) = Beta (a<sup>'</sup>, b<sup>'</sup> )
P(&theta; | X) has a Beta distribution which has parameters: 

- a<sup>'</sup> = a + &Sum; Xi (a + sum of clicks)
- b<sup>'</sup> = b + &Sum; 1- Xi ( b+ sum of no clicks)


How to set a and b? 

If a = 1 and b=1 then beta --> uniform 
If we don't know anything at first all CTR are equally probable (non informative prior)


For more details: https://en.wikipedia.org/wiki/Conjugate_prior
