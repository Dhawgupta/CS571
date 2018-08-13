import numpy as np
import random

import matplotlib.pyplot as plt
# p, p1, p2 are the 3 variables
def do_bernoulli_event(p = 0.5):
    '''
    The functions executes a Bernoulli Event with probability p for 1
    p : Probability P for generating a 1
    returns : The event 1 or 0
    '''
    if random.random() <= p:
        return 1
    else:
        return 0 
    
def generate_data(p = 0.7, p1 = 0.6, p2 = 0.3, samples = 1000):
    '''
    p : Probability of Choosing Coin 1
    p1 : Probability of getting heads in Coin 1
    p2 : Probability of getting heads in Coin 2
    return : A list of Heads and Tails in 1,0 format
    '''
    experiments = []
    for i in range(samples):
        if do_bernoulli_event(p) == 1:
            # coin1 
            experiments.append(do_bernoulli_event(p1))
        else:
            # coin 2
            experiments.append(do_bernoulli_event(p2))
    return experiments

def E(xi, p = 0.7, p1 = 0.6, p2 = 0.3 ):
    '''
    Return E(zi)
    '''
    return ( p*(p1**xi)*((1-p1)**(1-xi)) ) /( p*(p1**xi)*((1-p1)**(1-xi)) + (1-p)*(p2**xi)*((1-p2)**(1-xi)) )
    
# till here data is generated
# p_real  = 0.7
# p1_real = 0.8
# p2_real = 0.2

p_real  = 0.7
p1_real = 0.6
p2_real = 0.3
data = generate_data(p = p_real, p1 = p1_real, p2 = p2_real, samples = int(1e6))
experiments = 10

print("The real Parameters P:{}, P1:{}, P2:{}".format(p_real, p1_real, p2_real))
for exp in range(experiments):
    print("Experiment Number : {}".format(exp))
    p = random.random()
    p1 = random.random()
    p2 = random.random()
    # p = 0.7
    # p1 = 0.8
    # p2 = 0.7
    # starting with the max entropy state
    print("Starting Params P:{}, P1:{}, P2:{}".format(p, p1, p2))
    # Initlializing values of p ,  p1,p2

    # print(np.sum(data))
    # print(Es)

    # Repeat till convergence
    ps = [p]
    p1s = [p1]
    p2s = [p2]
    iter = 10
    for n in range(iter):
        # Expectation Step  (E)
        # Over here we will calculate the list of expecatation for the sampels
        # print ("The Values : P : {}, P1 : {} , P2 : {}".format(p,p1,p2))

        Es = []
        # Can be too time consuming
        # Es = [E(xi, p=p, p1=p1, p2=p2) for xi in data]

        E_hash = [0,0]
        # We can also hash the values of E to make it faster
        E_hash[0] = E(0,p=p,p1=p1, p2=p2)
        E_hash[1] = E(1, p=p, p1=p1, p2=p2)

        Es = [E_hash[xi] for xi in data]
        # Maximization step
        p = np.sum(Es)/len(Es)
        # heads from 1
        n_head = np.sum(data)
        n_heads_c1 = np.sum([data[i]*Es[i] for i in range(len(data))])
        n_c1 = np.sum(Es)
        p1 = n_heads_c1/n_c1
        p2 = ( n_head - n_heads_c1 )/( len(data) - n_c1)
        # print("Number Head : {}\nNumber of Heads from C1 : {}\nExperiments : {}".format(n_head, n_heads_c1, len(data)))
        ps.append(p)
        p1s.append(p1)
        p2s.append(p2)
    # we will see the probability of heads occuring from the old paramneters and the new
    # parameters we estimated
    print("Experiment Number : {}, Having results : p : {}, p1 : {}, p2 : {}".format(exp, p, p1, p2))

    print("Ending the Experiment\nOld : {} \nEstimated: {}".format(p_real*p1_real + (1-p_real)*(p2_real), p*p1 + (1-p)*p2))
# Uncomment the below lines to plot the convergence
# plt.figure(figsize = (20,20))
# plt.subplot(3,1,1)
# plt.plot(range(len(ps)), ps)
# plt.plot(range(len(ps)), [p_real for i in range(len(ps))])
#
# plt.subplot(3,1,2)
# plt.plot(range(len(ps)), p1s)
# plt.plot(range(len(ps)), [p1_real for i in range(len(ps))])
#
# plt.subplot(3,1,3)
# plt.plot(range(len(ps)), p2s)
# plt.plot(range(len(ps)), [p2_real for i in range(len(ps))])
# plt.show()




