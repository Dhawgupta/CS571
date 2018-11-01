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

state = generate_puzzle(goal, steps = 100)
print(state)
searchObjecth4 = []
searchObjecth3 = []
while True:
    searchObjecth3 = run_experiment(start_state = state, goal_state = goal, h_function=h3)
    searchObjecth4 = run_experiment(start_state = state, goal_state = goal, h_function=h4)
    if searchObjecth3.depth[searchObjecth3.goal_no] < searchObjecth4.depth[searchObjecth4.goal_no]:
        break
    state = generate_puzzle(goal, steps=100)
print("Found")
print(searchObjecth4.print_results())
print(searchObjecth3.print_results())

'''
[[0 3 8]
 [6 1 7]
 [2 5 4]]
Success Found Path
The Start State :
[[5 2 3]
 [7 6 0]
 [1 8 4]]
The Goal State : 
[[1 2 3]
 [4 5 6]
 [7 8 0]]
States Explored : 1529
Iterations Requried to Reach Success : 964

Total Number of States on Path : 21
Optimal Path 
[[5 2 3]
 [7 6 0]
 [1 8 4]]

[[5 2 3]
 [7 0 6]
 [1 8 4]]

[[5 2 3]
 [0 7 6]
 [1 8 4]]

[[0 2 3]
 [5 7 6]
 [1 8 4]]

[[2 0 3]
 [5 7 6]
 [1 8 4]]

[[2 3 0]
 [5 7 6]
 [1 8 4]]

[[2 3 6]
 [5 7 0]
 [1 8 4]]

[[2 3 6]
 [5 7 4]
 [1 8 0]]

[[2 3 6]
 [5 7 4]
 [1 0 8]]

[[2 3 6]
 [5 0 4]
 [1 7 8]]

[[2 3 6]
 [0 5 4]
 [1 7 8]]

[[2 3 6]
 [1 5 4]
 [0 7 8]]

[[2 3 6]
 [1 5 4]
 [7 0 8]]

[[2 3 6]
 [1 0 4]
 [7 5 8]]

[[2 3 6]
 [1 4 0]
 [7 5 8]]

[[2 3 0]
 [1 4 6]
 [7 5 8]]

[[2 0 3]
 [1 4 6]
 [7 5 8]]

[[0 2 3]
 [1 4 6]
 [7 5 8]]

[[1 2 3]
 [0 4 6]
 [7 5 8]]

[[1 2 3]
 [4 0 6]
 [7 5 8]]

[[1 2 3]
 [4 5 6]
 [7 0 8]]

[[1 2 3]
 [4 5 6]
 [7 8 0]]

Optimal Cost of the Path , Same as Depth : 21
None
Success Found Path
The Start State :
[[5 2 3]
 [7 6 0]
 [1 8 4]]
The Goal State : 
[[1 2 3]
 [4 5 6]
 [7 8 0]]
States Explored : 693
Iterations Requried to Reach Success : 432

Total Number of States on Path : 19
Optimal Path 
[[5 2 3]
 [7 6 0]
 [1 8 4]]

[[5 2 3]
 [7 0 6]
 [1 8 4]]

[[5 2 3]
 [0 7 6]
 [1 8 4]]

[[5 2 3]
 [1 7 6]
 [0 8 4]]

[[5 2 3]
 [1 7 6]
 [8 0 4]]

[[5 2 3]
 [1 7 6]
 [8 4 0]]

[[5 2 3]
 [1 7 0]
 [8 4 6]]

[[5 2 0]
 [1 7 3]
 [8 4 6]]

[[5 0 2]
 [1 7 3]
 [8 4 6]]

[[0 5 2]
 [1 7 3]
 [8 4 6]]

[[1 5 2]
 [0 7 3]
 [8 4 6]]

[[1 5 2]
 [7 0 3]
 [8 4 6]]

[[1 5 2]
 [7 4 3]
 [8 0 6]]

[[1 5 2]
 [7 4 3]
 [0 8 6]]

[[1 5 2]
 [0 4 3]
 [7 8 6]]

[[1 5 2]
 [4 0 3]
 [7 8 6]]

[[1 0 2]
 [4 5 3]
 [7 8 6]]

[[1 2 0]
 [4 5 3]
 [7 8 6]]

[[1 2 3]
 [4 5 0]
 [7 8 6]]

[[1 2 3]
 [4 5 6]
 [7 8 0]]

Optimal Cost of the Path , Same as Depth : 19
None
[dhawal.cs15@cseresearch Assignment2]$ 

'''