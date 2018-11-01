'''
Author : dhawal gupta
This is supposed to run the with the start state from a script which is entered thorught the command line

'''

import random
import numpy as np
import pickle as pkl
# import random
from Final import *
import time
from make_puzzle import generate_puzzle

state = np.zeros((3, 3)).astype(int)
goal = np.zeros((3, 3)).astype(int)
end_state = 'end.txt'
with open(end_state) as fil:
    # read the goal state
    row = 0  # the currebt row
    line = fil.readline()
    while line:
        for col, no in enumerate(line.split()):
            goal[row][col] = no
        line = fil.readline()
        row = row + 1

if len(sys.argv)  < 2:
    print("Start File not enterd hence generation it from random")
    # raise Exception("Enter the start file atleast")
    state = generate_puzzle(goal, steps = 50)
else:
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

timeh1 = 0
timeh2 = 0
timeh3 = 0
print("H3\n\n")
timeh3 = time.time()
objh3 = run_experiment_check_montonicity(start_state = state, goal_state = goal, h_function=h3_with_blank)
timeh3 = time.time() - timeh3
print("H2\n\n")
timeh2 = time.time()
objh2 = run_experiment_check_montonicity(start_state = state, goal_state = goal, h_function=h2_with_blank)
timeh2 = time.time() - timeh2
# timeh1 = time.time()
# objh1 = run_experiment_check_montonicity(start_state = state, goal_state = goal, h_function=h1)
# timeh1 = time.time() - timeh1

print("Time h1 : {}\nTime h2 : {}\nTime h3 : {}".format(timeh1, timeh2, timeh3))
# list1 = list(objh1.closed_list.keys())
list2 = list(objh2.closed_list.keys())
list3 = list(objh3.closed_list.keys())
# sets1 = set(list1)
sets2 = set(list2)
sets3 = set(list3)

# print(seth1)
# print(seth2)
# print(seth3)

val = sets3.issubset(sets2)
print(val)
if not val:
    print(sets3.difference(sets2))

# val = sets2.issubset(sets1)
# print(val)
# if not val:
#     print(sets2.difference(sets1))
