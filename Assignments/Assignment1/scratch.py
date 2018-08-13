import numpy as np
import random

def do_bernoulli_event(p=0.5):
    '''
    The functions executes a Bernoulli Event with probability p for 1
    p : Probability P for generating a 1
    returns : The event 1 or 0
    '''
    if random.random() <= p:
        return 1
    else:
        return 0

exp = 10
iter = int(1e7)
for e in range(exp):
    results = []

    for i in range(iter):
        results.append(do_bernoulli_event(0.8))

    print("P = {}".format(np.sum(results)/iter))
