import pickle as pkl
import random
from Final import *

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

# with open('mypickle.pickle') as f:
#     loaded_obj = pickle.load(f)
fil1 = 'step_list.pkl'
fil2 = 'start_state_list.pkl'

with open(fil1, 'r') as f:
    step_list = pkl.load(f)

with open(fil2, 'r') as f:
    start_state_list = pkl.load(f)

filename = 'results_h3.pkl'


# what all do we need to store
results = dict() # this will contain the number of expplored states and the number of iterations
for step in step_list:
    results[step] = run_experiment(start_state_list[step], goal, h3)
    print("saving")
    with open(filename, 'wb') as f:
        pkl.dump(results, f)
    print("Done saving")


