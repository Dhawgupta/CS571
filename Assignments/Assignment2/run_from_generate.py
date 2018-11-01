'''
Author : dhawal gupta
This is supposed to run the with the start state from a script which is entered thorught the command line

'''

import random
import numpy as np
import pickle as pkl
# import random
from make_puzzle import generate_puzzle
from Final import *





end_state = 'end.txt'

if len(sys.argv) > 2:
    end_state = sys.argv[2]


state = np.zeros((3,3)).astype(int)
goal =  np.zeros((3,3)).astype(int)



with open(end_state) as fil:
    # read the goal state
    row = 0 # the currebt row
    line = fil.readline()
    while line:
        for col,no in enumerate(line.split()):
            goal[row][col] = no
        line = fil.readline()
        row = row + 1

state = generate_puzzle(goal, steps = 60)
print(state)

searchObject = run_experiment(start_state = state, goal_state = goal, h_function=h3)

searchObject.print_results()