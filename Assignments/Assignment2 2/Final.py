
# author. : dhawal gupta
# input is working
# this contains more verbose as well outputs statement for debugging
# make this code presentable

import random
import numpy as np
from make_puzzle import generate_puzzle
import sys

def h1(current, goal):
	# COmpute the h1 score which is 0 for the current approach
	return 0
	# pass

def h2(current, goal):
	# compute the h2 score of the current and teh goal state which is the number
	# h2 = number of displaced tiles
	cost = np.sum(~(goal == current))
	current = current.astype(int)
	goal = goal.astype(int)
	current_hash = dict()
	for row in range(len(goal)):
		for col in range(len(goal[0])):
			current_hash[current[row][col]] = [row,col]
	goal_hash = dict()
	for row in range(len(goal)):
		for col in range(len(goal[0])):
			goal_hash[goal[row][col]] = [row,col]
	if list(current_hash[0]) == list(goal_hash[0]):
		pass
	else:
		cost = cost - 1
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
	current = current.astype(int)
	goal = goal.astype(int)
	if current_hash == None:
		current_hash = dict()
		for row in range(len(goal)):
			for col in range(len(goal[0])):
				current_hash[current[row][col]] = [row,col]
	goal_hash = dict()
	for row in range(len(goal)):
		for col in range(len(goal[0])):
			goal_hash[goal[row][col]] = [row,col]
	for row in range(len(current)):
		for col in range(len(current[0])):
			# here we will accouting the distance for the blank as well

			x,y = goal_hash[current[row][col]]
			# we will take the abs of both
			if current[row][col] == 0:
				pass
			else:
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
		raise Exception("Action not valid")

		# move blank up

def print_path(all_states , parent, parent_index):
	'''
	parent : It is the dictionary containing index and parents
	parent_index :  teh dindex of the p[arent]
	'''
	if parent_index == -1:
		return
	print_path(all_states, parent, parent[parent_index])
	print("{}\n".format(all_states[parent_index]))

def arreq_in_list(myarr, list_arrays):
	# funtion to check if the myarr exists in the liust_arraus
	return next((True for elem in list_arrays if np.array_equal(elem, myarr)), False)



def run_experiment(start_state, goal_state , h_function):
	'''
	start_state : The starting state for our A* implmementation
	goal_state : The GOal state for our alogrithm
	h_function  : THe function caller for our h)function
    return : Return a tuple containing states explored and iterations required
	'''
	# start_state = start_state.astpye(int)
	# goal_state = goal_state.astype(int)
	state = start_state
	goal =  goal_state
	state.astype(int)
	goal.astype(int)
	state_hash = dict()
	goal_hash = dict()
	open_list = dict()
	close_list = dict()
	all_states = [] # a list which will store all the states and we will use the index as a hash value for index of the lists
	iterations = 0 # the g(n) cost encountered till now
	depth = dict() # analogous to real cost
	parents = []
	parent = dict()
	# randomly procude the start state
	all_states.append(state)
	depth[0] = 0
	parent[0] = -1
	parents.append(-1)
	open_list[0] = 0 # cost initially
	success = False
	goal_index = 0
	while bool(open_list): # empty dictionaries evaluate to False
		# print(depth)
		sno = min(open_list, key=open_list.get)  # state no with the lowest cost
		current_state = all_states[sno] # get the current state

		del open_list[sno]
		iterations = iterations + 1
		close_list[sno] = depth[sno] # get the real cost of the state
		real_cost = depth[sno] + 1
		if (current_state == goal).all():
			goal_index = sno
			success = True
			break
		new_states = []
		for action in range(4): # for all possible actions
			if valid_action(current_state, action): # check if the action is valid or not
				new_states.append(execute_action(current_state, action)[0].astype(int))
		for s in new_states:
			if not arreq_in_list(s, all_states) :
				index = len(all_states)  # len will be one greater than the last value index
				# print(index)
				depth[index] = real_cost
				all_states.append(s)
				g_cost = real_cost
				h_cost = h_function(current = s, goal = goal)# heuristic cost
				open_list[index] = g_cost + h_cost
				parents.append(sno)
				parent[index] = sno
	if success:
		print ("Success Found Path")
		# print_path(all_states, parent, goal_index)
		print("States Explored : {}\nIterations Requried to Reach Success : {}\n".format(len(all_states), iterations))
        return [len(all_states), iterations]
	print("Path Not Found")
if __name__ == "__main__":
	# first we will read the input  from the file
	start_state = "start.txt" # this will contain the start the state of the agnet
	end_state = "end.txt" # this file will contain the end or goal state of the agent

	# assumong the puzzle is only 3x3 and no bigger
	state = np.zeros((3,3))
	goal =  np.zeros((3,3))
	state.astype(int)
	goal.astype(int)
	state_hash = dict()
	goal_hash = dict()



	# to read the starting state of the game
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

	# to read the goal state of the game
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

	print(goal_hash)

	open_list = dict()
	close_list = dict()
	all_states = [] # a list which will store all the states and we will use the index as a hash value for index of the lists
	iterations = 0 # the g(n) cost encountered till now
	depth = dict() # analogous to real cost
	parents = []
	parent = dict()
	# randomly procude the start state
	state = generate_puzzle(goal, steps = 200).astype(int)
	print("The start state : \n{}\nThe Goal state is : \n{}".format(state, goal))

	all_states.append(state)
	depth[0] = 0
	parent[0] = -1
	parents.append(-1)
	open_list[0] = 0 # cost initially
	success = False
	goal_index = 0
	while bool(open_list): # empty dictionaries evaluate to False
		# print(depth)
		sno = min(open_list, key=open_list.get)  # state no with the lowest cost
		current_state = all_states[sno] # get the current state

		del open_list[sno]
		iterations = iterations + 1
		close_list[sno] = depth[sno] # get the real cost of the state
		real_cost = depth[sno] + 1
		if (current_state == goal).all():
			goal_index = sno
			success = True
			break
		new_states = []
		for action in range(4): # for all possible actions
			if valid_action(current_state, action): # check if the action is valid or not
				new_states.append(execute_action(current_state, action)[0].astype(int))
		for s in new_states:
			if not arreq_in_list(s, all_states) :
				index = len(all_states)  # len will be one greater than the last value index
				# print(index)
				depth[index] = real_cost
				all_states.append(s)
				g_cost = real_cost
				h_cost = h3(current = s, goal = goal)# heuristic cost
				open_list[index] = g_cost + h_cost
				parents.append(sno)
				parent[index] = sno
		if iterations%100 == 0:
			print("Len : {}".format(len(open_list)))
			print("Cost/Iter : {}".format(iterations))


	if success:
		print ("Success Found Path")
		# print_path(all_states, parent, goal_index)
		print("States Explored : {}\nIterations Requried to Reach Success : {}\n".format(len(all_states), iterations))
	else:
		print ("Path not found")
