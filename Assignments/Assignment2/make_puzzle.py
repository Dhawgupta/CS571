
# author. : dhawal gupta
# input is working

import random
import numpy as np
'''
check points

'''


def h1(current_state, goal_state):
	# COmpute the h1 score which is 0 for the current approach
	return 0
	# pass

def h2(current, goal):
	# compute the h2 score of the current and teh goal state which is the number
	# h2 = number of displaced tiles
	cost = np.sum(~(goal == current))
	return cost

def h3(current, goal, current_hash = None, goal_hash = None):
	'''
	Current : THe current state in an numpy array
	Goal : The current goal numpy array
	current_hash :  The hash of the current state
	goal_hash : The hash of the goal state
	return : THe h3 (manhattan based distance)
	'''
	# this will take the min steps required to move the blocks form the current positino to the goal positin
	cost = 0
	if current_hash == None:
		current_hash = dict()
		# if the state_hash is none the create the same
		current_hash = dict()
		for row in range(len(goal_hash)):
			for col in range(len(goal_hash[0])):
				current_hash[state[row][col]] = [row,col]
	if goal_hash == None:
		goal_hash = dict()
		# if the state_hash is none the create the same
		state_hash = dict()
		for row in range(len(goal_hash)):
			for col in range(len(goal_hash[0])):
				goal_hash[state[row][col]] = [row,col]
	# now we will compute the score for the states
	for row in range(len(current)):
		for col in range(len(current[0])):
			# here we will accouting the distance for the blank as well
			x,y = goal_hash[current[row][col]]
			# we will take the abs of both
			cost = cost + abs(row -  x  ) + abs(col - y)
	return cost

def h4(current, goal):
	# this will implement the upper bound on the h* function
	pass


def valid_action(state, action, state_hash = None): # state hash is not very useful but keeping oit to make it eacy tpt worj 2ith
	# check the validity of the action
	# we have to invert x, y positino as row represent the y coordinte and the col represents the x coordinate
	if state_hash == None:
		# if the state_hash is none the create the same
		state_hash = dict()
		for row in range(len(state)):
			for col in range(len(state[0])):
				state_hash[state[row][col]] = [row,col]

	r,c = state.shape
	y,x = state_hash[0] # get the position of the blank
	if action == 0:
		if y == 0 : # blank already in the first line
			return False
	if action == 1:  # left valid_action
		if x == 0:
			return False
	if action == 2: # right valid_act
		if x == c-1:
			return False
	if action == 3:
		if y == r-1:
			return False
	return True


def execute_action(state,action , state_hash = None):
	'''
	state : the state onto which action has to be executed
	state_hash : THe hash of the state
	action : The action that has to be execute " action are U, L, R, D - up (0), left (1), right (2), down (3)"
	return  : state, state_hash , if the action is not valid state is note changed
	'''
	if state_hash == None:
		# if the state_hash is none the create the same
		state_hash = dict()
		for row in range(len(state)):
			for col in range(len(state[0])):
				state_hash[state[row][col]] = [row,col]

	# get the blank coordinate
	r,c = state.shape # the size of the game
	y,x = state_hash[0] # the blank coordinate
	# now execute the action and send the update states
	# print "Blank Position {}, {}".format(x,y)

	x_new, y_new = [0,0]
	if valid_action(state,action, state_hash):
		# if the given action is valud
		if action == 0:
			x_new = x
			y_new = y - 1
		if action == 1:  # left valid_action
			x_new = x-1
			y_new = y
		if action == 2: # right valid_act
			x_new = x + 1
			y_new = y
		if action == 3:
			x_new = x
			y_new = y + 1
		# getting the new position of the blank we will move the blank to the
		# and the element from that position to the blank position
		tile = state[y_new][x_new]
		state_hash[tile] = [y,x] # modify the position of the tile to the position of the blank
		state_hash[0] = [y_new, x_new]
		new_state = state.copy()

		new_state[y_new, x_new ] = 0
		new_state[y,x] = tile
		return (new_state,state_hash)
	else:
		print ("Action not valid")

		# move blank up

def arreq_in_list(myarr, list_arrays):
	# funtion to check if the myarr exists in the liust_arraus
    return next((True for elem in list_arrays if np.array_equal(elem, myarr)), False)



# first we will read the input  from the file
start_state = "start.txt" # this will contain the start the state of the agnet
end_state = "end.txt" # this file will contain the end or goal state of the agent

# assumong the puzzle is only 3x3 and no bigger
state = np.zeros((3,3))
goal =  np.zeros((3,3))
state_hash = dict()
goal_hash = dict()


# we will represent the blank state as 0 for out case

with open(start_state) as fil:
	# read the fule
	row = 0 # the currebt row
	line = fil.readline()
	while line:
		for col,no in enumerate(line.split()):
			state[row][col] = no
		line = fil.readline()
		row = row + 1


	# pass

with open(end_state) as fil:
	# read the goal state
	row = 0 # the currebt row
	line = fil.readline()
	while line:
		for col,no in enumerate(line.split()):
			goal[row][col] = no
		line = fil.readline()
		row = row + 1
	# pass

# Fill the goal and state hashed to make operations faster

for row in range(len(state)):
	for col in range(len(state[0])):
		goal_hash[goal[row][col]] = [row,col]
		state_hash[state[row][col]] = [row,col]


def generate_puzzle(goal,steps = 1000):
	'''
	:param goal: The goal state from which we have to produce the puzzle
	:para steps: The number of random action to be taken
	:return: Return the puzzled matrix
	'''
	puzzle = goal.copy()
	print(valid_action(puzzle, 0))
	shuffle = int(steps)
	action = 0
	for step in range(shuffle):
		action = random.randint(0, 3)
		# print(type(action))
		if valid_action(puzzle, action):  # if the action is vald
			puzzle = execute_action(puzzle, action)[0]
	return puzzle


if __name__ == "__main__":
	puzzle = goal.copy()
	print(valid_action(puzzle, 0))
	shuffle = int(1e4)
	action = 0
	for step in range(shuffle):
		action = random.randint(0,3)
		# print(type(action))
		if valid_action(puzzle, action) : # if the action is vald
			puzzle = execute_action(puzzle, action)[0]
	print(puzzle)

