import pickle as pkl
import random
from Final import *
import time
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

filename = 'results_h1_5.pkl'
filename2 = 'results_h1_time5.pkl'

# what all do we need to store
results = dict() # this will contain the number of expplored states and the number of iterations
times = dict()
for step in step_list:
    start_time = time.time()
    results[step] = run_experiment(start_state_list[step], goal, h1)
    end_time = time.time()
    times[step] = end_time - start_time
    print("The time taken (sec) {}".format(times[step]))

    print("saving")
    with open(filename, 'wb') as f:
        pkl.dump(results, f)
    with open(filename2, 'wb') as f:
        pkl.dump(times, f)

    print("Done saving")


