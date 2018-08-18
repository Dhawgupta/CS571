from make_puzzle import generate_puzzle
import pickle as pkl
import numpy as np

max_steps = 70
start_steps = 10
step_list = []
start_state_list = dict()
end_state = 'end.txt'
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

while start_steps <= max_steps:
    state = generate_puzzle(goal = goal, steps = start_steps)
    step_list.append(start_steps)
    start_state_list[start_steps] = state
    start_steps += 2

fil1 = "step_list.pkl"
fil2 = "start_state_list.pkl"

with open(fil1, 'wb') as f:
    pkl.dump(step_list, f)

with open(fil2,'wb') as f:
    pkl.dump(start_state_list, f)



