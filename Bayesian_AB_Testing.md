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
         We want to play only the machine to maximize our winnings. But you don't the best machine unless collecting 
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



        
 

