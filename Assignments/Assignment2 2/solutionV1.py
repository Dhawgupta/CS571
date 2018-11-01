
# author. : dhawal gupta
# input is working
# this contains more verbose as well outputs statement for debugging
# make this code presentable

import random
import numpy as np
from make_puzzle import generate_puzzle
import sys

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


# print "Start state :\n {}\nThe end state : \n {}".format(state, goal)
#
# print "Hash \n {}".format(state_hash)
# # do an action on the state
# (state, state_hash) = execute_action(state, state_hash, 0) # UP action
#
# print "State after up action \n{} \n with the hash \n{}\n".format(state , state_hash)
#
# (state, state_hash) = execute_action(state, state_hash, 2) # Right action
#
# print "State after up action \n{} \n with the hash \n{}\n".format(state , state_hash)
# (state, state_hash) = execute_action(state, state_hash, 3) # Down Action
#
# print "State after up action \n{} \n with the hash \n{}\n".format(state , state_hash)
#
# (state, state_hash) = execute_action(state, state_hash, 1) # LEft ACtion
#
# print "State after up action \n{} \n with the hash \n{}".format(state , state_hash)

# the above code is to check the action correctness
open_list = dict()
close_list = dict()
all_states = [] # a list which will store all the states and we will use the index as a hash value for index of the lists
real_cost = 0 # the g(n) cost encountered till now


# this is the open , we start with state and insert it into the open open_list
all_states.append(state)
open_list[0] = 0 # cost initially
success = False
while bool(open_list): # empty dictionaries evaluate to False
	# print(open_list)
	# print(all_states)
	# while the open list is not empty
	# we will use bytes tro store the string
	sno = min(open_list, key=open_list.get)  # state no with the lowest cost
	# print("The state Number : {}".format(sno))
	# print("Real Cost: {}".format(real_cost))
	current_state = all_states[sno] # get the current state
	# check if the popped state is goal state
	# print (current_state)
	if (current_state == goal).all():
		# print "Success"
		success = True
		break
	new_states = []
	# expand the node from this point on
	for action in range(4): # for all possible actions
		# check if the action is valid for state or not
		# print("Action : {}".format(action))
		if valid_action(current_state, action): # check if the action is valid or not
			new_states.append(execute_action(current_state, action)[0])
			# print(new_states[-1])
	# print("New states having len {}  \n   {} ".format(len(new_states), new_states))
	# move the old state to the close list
	del open_list[sno]
	close_list[sno] = real_cost # get the real cost of the state

	# increment the real cost
	real_cost = real_cost + 1

	# now we will check if the new_state are actually new or not
	for s in new_states:
		# print(s)
		# print(all_states)
		# print(arreq_in_list(s, all_states))
		if not arreq_in_list(s, all_states) :
			# not exist add the element to the open list and calulcate the g and h cost
			# print("Adding Element")
			index = len(all_states)  # len will be one greater than the last value index
			all_states.append(s)
			g_cost = real_cost
			h_cost = h2(s, goal)# heuristic cost
			# add the cost and to the open list
			open_list[index] = g_cost + h_cost
	if real_cost%100 == 0:
		print("Len : {}".format(len(open_list)))
		print("Cost/Iter : {}".format(real_cost))


if success:
	print ("Success Found Path")
else:
	print ("Path not found")
