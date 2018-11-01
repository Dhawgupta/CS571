'''
Author : dhawal gupta
This is supposed to run the with the start state from a script which is entered thorught the command line

'''

import random
import numpy as np
import pickle as pkl
# import random
from Final import *


if len(sys.argv)  < 2:
    raise Exception("Enter the start file atleast")

start_file = sys.argv[1]


end_state = 'end.txt'

if len(sys.argv) > 2:
    end_state = sys.argv[2]


state = np.zeros((3,3)).astype(int)
goal =  np.zeros((3,3)).astype(int)

with open(start_file) as fil:
    # read the goal state
    row = 0 # the currebt row
    line = fil.readline()
    while line:
        for col,no in enumerate(line.split()):
            state[row][col] = no
        line = fil.readline()
        row = row + 1

with open(end_state) as fil:
    # read the goal state
    row = 0 # the currebt row
    line = fil.readline()
    while line:
        for col,no in enumerate(line.split()):
            goal[row][col] = no
        line = fil.readline()
        row = row + 1

searchObject = run_experiment(start_state = state, goal_state = goal, h_function=h3)

searchObject.print_results()