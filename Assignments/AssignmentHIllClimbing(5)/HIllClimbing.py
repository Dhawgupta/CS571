# author. : dhawal gupta
# input is working
# this contains more verbose as well outputs statement for debugging
# make this code presentable

import random
import numpy as np
from make_puzzle import generate_puzzle
import sys
from queue import PriorityQueue
from copy import deepcopy

class Puzzle8:
    def __init__(self, puzzle_config, g, h):
        self.puzzle_config = puzzle_config
        self.g = g
        self.h = h

    def __lt__(self, other):
        if ( self.h == other.h):
            if self.g == other.g:
                return self.convert_state_to_string(self.puzzle_config) < self.convert_state_to_string(other.puzzle_config)
            return (self.g < other.g)
        return (self.h) <= ( other.h)
    def convert_state_to_string(self, state):
        state = state.astype(int)
        str1 = ""
        for i in range(len(state)):
            for j in range(len(state[0])):
                str1 = str1 + str(int(state[i][j]))
        return str1

class A_star:
    '''
    This object will contain all the infromation required to represent the search that will be returned by the run_experimetn
    '''

    def __init__(self,  success, start_state, goal_state, parents, h_function, h_func_no,
                 iterations, open_list, closed_list, all_state_hash, current_state = None):
        self.current_state = current_state
        self.success = success
        self.start_state = start_state  # the start state
        self.goal_state = goal_state  # the goal state
        self.parents = parents  # the parents
        self.h_function = h_function
        self.h_func_no = h_func_no
        self.iterations = iterations
        self.open_list = open_list
        self.closed_list = closed_list
        self.all_state_hash = all_state_hash

    def convert_state_to_string(self, state):
        state = state.astype(int)
        str1 = ""
        for i in range(len(state)):
            for j in range(len(state[0])):
                str1 = str1 + str(int(state[i][j]))
        return str1

    def convert_string_to_state(self, String):
        rows = int(np.sqrt(len(String)))
        cols = int(len(String) / rows)
        state = np.zeros((rows, cols))

        state = state.astype(int)
        for i in range(rows):
            for j in range(cols):
                state[i][j] = int(String[rows * i + j])
        return state

    def print_results(self):
        '''
        This will print the required results
        '''
        print("The Heursitic Function  : {}".format(heuristics[self.h_function]))
        if self.success:
            print ("Success Found Path")
            print("The Start State :\n{}".format(self.start_state))
            print("The Goal State : \n{}".format(self.goal_state))
            print("States Explored : {}\nIterations Requried to Reach Success : {}\n".format(len(self.closed_list),
                                                                                             self.iterations))
            print("Total Number of States on Path : {}".format(
                self.all_state_hash[self.convert_state_to_string(self.goal_state)]))
            print("Optimal Path ")
            self.print_path()
        # print("Optimal Cost of the Path , Same as Depth : {}".format(self.depth[self.goal_no]))
        else:
            print ("Failure Path Not Found")
            print("The Start State :\n{}".format(self.start_state))
            print("The Goal State : \n{}".format(self.goal_state))
            print("The State agent is stuck in : \n{}\nWith Cost : {}".format(self.current_state,self.closed_list[convert_state_to_string(self.current_state)] ))

            print("States Explored : {}\nIterations Requried : {}\n".format(len(self.closed_list), self.iterations))
            print("The Path : ")
            self.print_path(c_state=self.current_state)


    def print_path(self, c_state = None):
        '''
        This functino will be used to print the path
        :return:
        '''
        if c_state is None:
            self.print_path_recursive(self.convert_state_to_string(self.goal_state))
        else:
            self.print_path_recursive(self.convert_state_to_string(self.current_state))


    def print_path_recursive(self, string_state):
        if string_state == "000000000":
            return
        self.print_path_recursive(self.parents[string_state])
        print("{}\n".format(self.convert_string_to_state(string_state)))


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
            current_hash[current[row][col]] = [row, col]
    goal_hash = dict()
    for row in range(len(goal)):
        for col in range(len(goal[0])):
            goal_hash[goal[row][col]] = [row, col]
    if list(current_hash[0]) == list(goal_hash[0]):
        pass
    else:
        cost = cost - 1
    return cost


def h3(current, goal, current_hash=None, goal_hash=None):
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
                current_hash[current[row][col]] = [row, col]
    goal_hash = dict()
    for row in range(len(goal)):
        for col in range(len(goal[0])):
            goal_hash[goal[row][col]] = [row, col]
    for row in range(len(current)):
        for col in range(len(current[0])):
            # here we will accouting the distance for the blank as well

            x, y = goal_hash[current[row][col]]
            # we will take the abs of both
            if current[row][col] == 0:
                pass
            else:
                cost = cost + abs(row - x) + abs(col - y)
    return cost

def h2_plus_h3(current, goal):
    return h2(current, goal) + h3(current, goal)

def h2_mult_h3(current, goal):
    return h2(current, goal)*h3(current, goal)



def h2_with_blank(current, goal):
    # compute the h2 score of the current and teh goal state which is the number
    # h2 = number of displaced tiles
    cost = np.sum(~(goal == current))
    current = current.astype(int)
    goal = goal.astype(int)
    current_hash = dict()
    for row in range(len(goal)):
        for col in range(len(goal[0])):
            current_hash[current[row][col]] = [row, col]
    goal_hash = dict()
    for row in range(len(goal)):
        for col in range(len(goal[0])):
            goal_hash[goal[row][col]] = [row, col]
    # if list(current_hash[0]) == list(goal_hash[0]):
    #     pass
    # else:
    #     cost = cost - 1
    return cost


def h3_with_blank(current, goal, current_hash=None, goal_hash=None):
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
                current_hash[current[row][col]] = [row, col]
    goal_hash = dict()
    for row in range(len(goal)):
        for col in range(len(goal[0])):
            goal_hash[goal[row][col]] = [row, col]
    for row in range(len(current)):
        for col in range(len(current[0])):
            # here we will accouting the distance for the blank as well

            x, y = goal_hash[current[row][col]]
            # we will take the abs of both
            # if current[row][col] == 0:
            #     pass
            # else:
            #     cost = cost + abs(row - x) + abs(col - y)
            cost = cost + abs(row - x) + abs(col - y)
    return cost

heuristics = dict()
heuristics[h1] = "The zero heursitic"
heuristics[h2] = "Displaced Tiles Heurisitc"
heuristics[h3] = "Manhattan Heursitisc"
heuristics[h2_plus_h3] = "Displaced Tiles + Manhattam Heursitic"
heuristics[h2_mult_h3] = "Displaced Tiles * Manhattam Heuristic"
heuristics[h2_with_blank] = "Displaced Tile Including the Blank Tile"
heuristics[h3_with_blank] = "Manhattan includeing the blank tile"
def h4(current, goal):
    '''
    This will be a non admissble heursitic for the function
    Assumptions : That the goal state is has no non inverted state i.e. is of th efrom
    1 2 3
    4 5 6
    7 8 0
    :param current: The current state
    :param goal:  The goal state
    :return:  The inversion required
    '''

    cost = 0
    current = current.astype(int)
    goal = goal.astype(int)

    # hash is not required
    # current_hash = dict()
    # for row in range(len(goal)):
    # 	for col in range(len(goal[0])):
    # 		current_hash[current[row][col]] = [row, col]
    # goal_hash = dict()
    # for row in range(len(goal)):
    # 	for col in range(len(goal[0])):
    # 		goal_hash[goal[row][col]] = [row, col]

    # get a list of the ellemtn s
    list_ = []
    for row in range(len(current)):
        for col in range(len(current[0])):
            if current[row][col] == 0:
                continue
            else:
                list_.append(current[row][col])
    # now we will check the number of inverted entires in the list_
    for i, ele in enumerate(list_):
        j = i
        while j < len(list_):
            if ele > list_[j]:
                cost += 1
            j += 1

    return cost


def valid_action(state, action,
                 state_hash=None):  # state hash is not very useful but keeping oit to make it eacy tpt worj 2ith
    # check the validity of the action
    # we have to invert x, y positino as row represent the y coordinte and the col represents the x coordinate
    if state_hash == None:
        # if the state_hash is none the create the same
        state_hash = dict()
        for row in range(len(state)):
            for col in range(len(state[0])):
                state_hash[state[row][col]] = [row, col]

    r, c = state.shape
    y, x = state_hash[0]  # get the position of the blank
    if action == 0:
        if y == 0:  # blank already in the first line
            return False
    if action == 1:  # left valid_action
        if x == 0:
            return False
    if action == 2:  # right valid_act
        if x == c - 1:
            return False
    if action == 3:
        if y == r - 1:
            return False
    return True


def execute_action(state, action, state_hash=None):
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
                state_hash[state[row][col]] = [row, col]

    # get the blank coordinate
    r, c = state.shape  # the size of the game
    y, x = state_hash[0]  # the blank coordinate
    # now execute the action and send the update states
    # print "Blank Position {}, {}".format(x,y)

    x_new, y_new = [0, 0]
    if valid_action(state, action, state_hash):
        # if the given action is valud
        if action == 0:
            x_new = x
            y_new = y - 1
        if action == 1:  # left valid_action
            x_new = x - 1
            y_new = y
        if action == 2:  # right valid_act
            x_new = x + 1
            y_new = y
        if action == 3:
            x_new = x
            y_new = y + 1
        # getting the new position of the blank we will move the blank to the
        # and the element from that position to the blank position
        tile = state[y_new][x_new]
        state_hash[tile] = [y, x]  # modify the position of the tile to the position of the blank
        state_hash[0] = [y_new, x_new]
        new_state = state.copy()

        new_state[y_new, x_new] = 0
        new_state[y, x] = tile
        return (new_state, state_hash)
    else:
        raise Exception("Action not valid")


# move blank up


def print_path(all_states, parent, parent_index):
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


def convert_state_to_string(state):
    state = state.astype(int)
    str1 = ""
    for i in range(len(state)):
        for j in range(len(state[0])):
            str1 = str1 + str(int(state[i][j]))
    return str1


def convert_string_to_state(String):
    rows = int(np.sqrt(len(String)))
    cols = int(len(String) / rows)
    state = np.zeros((rows, cols))

    state = state.astype(int)
    for i in range(rows):
        for j in range(cols):
            state[i][j] = int(String[rows * i + j])
    return state


def state_found(all_state_hash, state):
    '''
    :param all_state_hash:  ' The string hash of the state
    :param state:
    :return:
    '''
    if convert_state_to_string(state) in all_state_hash:
        return True
    else:
        False

def find_neighbours(current_state):
    '''
    Input is assumed to be  a 2D matrix
    :param current_state:  Assumed to be a 2 D matrix
    :return:
    '''
    neghbor = []
    row,col = 0,0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] == 0:
                row, col = i,j
                break
    if row + 1 < 3:
        s_ = deepcopy(current_state)
        s_,_  = execute_action(s_, 3)
        neghbor.append(s_)
    if row - 1 > -1:
        s_ = deepcopy(current_state)
        s_,_  = execute_action(s_, 0)
        neghbor.append(s_)
    if col + 1 < 3:
        s_ = deepcopy(current_state)
        s_,_  = execute_action(s_, 2)
        neghbor.append(s_)
    if col - 1 > -1:
        s_ = deepcopy(current_state)
        s_,_  = execute_action(s_, 1)
        neghbor.append(s_)
    return neghbor


def run_experiment(start_state, goal_state, h_function):
    '''
        start_state : The starting state for our A* implmementation
        goal_state : The GOal state for our alogrithm
        h_function  : THe function caller for our h)function
        return : Return a tuple containing states explored and iterations required
        '''
    # print("Chckpt 1")
    state = start_state

    goal = goal_state
    state.astype(int)
    goal.astype(int)
    start_state_string = convert_state_to_string(state)
    goal_string = convert_state_to_string(goal)
    state_hash = dict()
    goal_hash = dict()

    open_list = PriorityQueue()
    close_list = dict()
    parent = dict()

    all_states = []  # a list which will store all the states and we will use the index as a hash value for index of the lists
    all_state_hash = dict()
    iterations = 0  # the g(n) cost encountered till now
    depth = dict()  # analogous to real cost
    parent[start_state_string] = "000000000"  # parent string of start state
    # parents.append(-1)
    open_list.put(Puzzle8(puzzle_config=state, g=0, h=h_function(current=state, goal=goal)))  # cost initially
    success = False
    goal_index = 0  # not required at the moment
    all_state_hash[start_state_string] = 0
    open_list_len = 1
    current_state = state
    while not open_list.empty():  # empty dictionaries evaluate to False
        # print("Chckpt 2")

        obj = open_list.get() # get the element from open list
        open_list_len -= 1
        # sno = min(open_list, key=open_list.get)  # state no with the lowest cost
        state_string = convert_state_to_string(obj.puzzle_config)
        current_state = obj.puzzle_config
        iterations = iterations + 1
        close_list[convert_state_to_string(obj.puzzle_config)] = obj.g  # get the real cost of the state
        if (state_string == goal_string):
            success = True
            break
        # print("Chckpt 3")

        new_states = []
        for action in range(4):  # for all possible actions
            # print("Chckpt 4")
            if valid_action(current_state, action):  # check if the action is valid or not
                new_states.append(execute_action(current_state, action)[0].astype(int))
                # print("New STate : {}".format(new_states[-1],h_function(new_states[-1], goal)))
        best_state_cost_h = 10000000
        best_state_cost_g = 10000000
        best_state = []
        for s in new_states:

            sts_string = convert_state_to_string(s)
            if sts_string not in close_list:
                g_cost = obj.g + 1
                h_cost = h_function(current=s, goal=goal)  # heuristic cost
                # print("State : {}, Cost : {}".format(s, h_cost))
                # print("Chckpt 5")

                if best_state_cost_h > h_cost:
                    best_state_cost_h = h_cost
                    best_state_cost_g = g_cost
                    best_state = s
                # print("The Best State : {}, Cost : {}".format(best_state, best_state_cost_h))
                # open_list.put(Puzzle8(puzzle_config=s, g=g_cost, h=h_cost))
                parent[sts_string] = state_string
                all_state_hash[sts_string] = g_cost
                # open_list_len += 1
        if best_state_cost_h < obj.h:
            # make the move
            open_list.put(Puzzle8(puzzle_config=best_state, g=best_state_cost_g, h=best_state_cost_h))  # cost initially
            current_state = best_state
            parent[convert_state_to_string(best_state)] = state_string
            # all_state_hash[convert_state_to_string(best_state)] = g_cost
            # print("Chckpt 6")

        else:
            success = False
            break

        # print("Chckpt 7")

        if iterations % 10000 == 0:
            print("Len : {}".format(open_list_len))
            print("Iter : {}".format(iterations))

    searchObject = []
    if success:
        searchObject = A_star(success=True, start_state=start_state, goal_state=goal_state,
                              parents=parent, h_function=h_function, h_func_no=None,
                              iterations=iterations, open_list=open_list, closed_list=close_list,
                              all_state_hash=all_state_hash, current_state= current_state)
        # self, success, start_state, goal_state, parents, h_function, h_func_no,
        # iterations, open_list, closed_list, all_state_hash):
    else:
        searchObject = A_star(success=False, start_state=start_state, goal_state=goal_state,
                              parents=parent, h_function=h_function, h_func_no=None, open_list=open_list,
                              closed_list=close_list, all_state_hash=all_state_hash, iterations = iterations,
                              current_state= current_state)
    print("Chckpt 8")

    return searchObject


# def run_experiment_(start_state, goal_state, h_function):
#     '''
#     start_state : The starting state for our A* implmementation
#     goal_state : The GOal state for our alogrithm
#     h_function  : THe function caller for our h)function
#     return : Return a tuple containing states explored and iterations required
#     '''
#     # start_state = start_state.astpye(int)
#     # goal_state = goal_state.astype(int)
#     state = start_state
#
#
#
#     goal = goal_state
#     state.astype(int)
#     goal.astype(int)
#     start_state_string = convert_state_to_string(state)
#     goal_string = convert_state_to_string(goal)
#     state_hash = dict()
#     goal_hash = dict()
#
#     open_list = PriorityQueue()
#     close_list = dict()
#     parent = dict()
#
#     all_states = []  # a list which will store all the states and we will use the index as a hash value for index of the lists
#     all_state_hash = dict()
#     iterations = 0  # the g(n) cost encountered till now
#     depth = dict()  # analogous to real cost
#
#     parent[start_state_string] = "000000000"  # parent string of start state
#     open_list.put(Puzzle8(puzzle_config=state, g=0, h=h_function(current=state, goal=goal)))  # cost initially
#     success = False
#     all_state_hash[start_state_string] = 0
#     open_list_len = 1
#     while True :  # empty dictionaries evaluate to False
#         print("Checkpt 1")
#         obj = open_list.get()
#         # print(obj.puzzle_config)
#         open_list_len -=1
#         # sno = min(open_list, key=open_list.get)  # state no with the lowest cost
#         state_string = convert_state_to_string(obj.puzzle_config)
#         current_state = obj.puzzle_config
#         iterations = iterations + 1
#         close_list[convert_state_to_string(obj.puzzle_config)] = obj.g  # get the real cost of the state
#         if (state_string == goal_string):
#             success = True
#             break
#         print("Checkpt 2")
#
#         new_states = []
#         for action in range(4):  # for all possible actions
#             if valid_action(current_state, action):  # check if the action is valid or not
#                 new_states.append(execute_action(current_state, action)[0].astype(int))
#         print("Checkpt 3")
#
#         for s in new_states:
#             sts_string = convert_state_to_string(s)
#             if sts_string not in close_list:
#                 g_cost = obj.g + 1
#                 h_cost = h_function(current=s, goal=goal)  # heuristic cost
#                 print("THe State : {}, THe Cost : {}".format(s, h_cost))
#                 open_list.put(Puzzle8(puzzle_config=s, g=g_cost, h=h_cost))
#                 parent[sts_string] = state_string
#                 all_state_hash[sts_string] = g_cost
#                 open_list_len += 1
#         if iterations % 10000 == 0:
#             print("Len : {}".format(open_list_len))
#             print("Iter : {}".format(iterations))
#
#         print("Checkpt 4")
#
#     searchObject = []
#     if success:
#         searchObject = A_star(success=True, start_state=start_state, goal_state=goal_state,
#                               parents=parent, h_function=h_function, h_func_no=None,
#                               iterations=iterations, open_list=open_list, closed_list=close_list,
#                               all_state_hash=all_state_hash)
#         # self, success, start_state, goal_state, parents, h_function, h_func_no,
#         # iterations, open_list, closed_list, all_state_hash):
#     else:
#         searchObject = A_star(success=False, start_state=start_state, goal_state=goal_state,
#                               parents=parent, h_function=h_function, h_func_no=None, open_list=open_list,
#                               closed_list=close_list, all_state_hash=all_state_hash, iterations = iterations)
#
#
#     print("Checkpt 1")
#
#     return searchObject


import time
if __name__ == "__main__":
    # first we will read the input  from the file
    start_state = "testcase4.txt"  # this will contain the start the state of the agnet
    end_state = "goal1.txt"  # this file will contain the end or goal state of the agent

    # assumong the puzzle is only 3x3 and no bigger
    state = np.zeros((3, 3))
    goal = np.zeros((3, 3))
    state.astype(int)
    goal.astype(int)
    state_hash = dict()
    goal_hash = dict()

    # to read the starting state of the game
    with open(start_state) as fil:
        # read the fule
        row = 0  # the currebt row
        line = fil.readline()
        while line:
            for col, no in enumerate(line.split()):
                state[row][col] = no
            line = fil.readline()
            row = row + 1

    # pass

    # to read the goal state of the game
    with open(end_state) as fil:
        # read the goal state
        row = 0  # the currebt row
        line = fil.readline()
        while line:
            for col, no in enumerate(line.split()):
                goal[row][col] = no
            line = fil.readline()
            row = row + 1
    # pass

    # Fill the goal and state hashed to make operations faster

    for row in range(len(state)):
        for col in range(len(state[0])):
            goal_hash[goal[row][col]] = [row, col]
            state_hash[state[row][col]] = [row, col]

    print(goal_hash)

    open_list = dict()
    close_list = dict()
    all_states = []  # a list which will store all the states and we will use the index as a hash value for index of the lists
    iterations = 0  # the g(n) cost encountered till now
    depth = dict()  # analogous to real cost
    parents = []
    parent = dict()
    # randomly procude the start state
    # state = generate_puzzle(goal, steps=200).astype(int)
    state = state.astype(int)
    # print("The start state : \n{}\nThe Goal state is : \n{}".format(state, goal))
    startTime = time.time()
    obj = run_experiment(state, goal, h3)
    endTime = time.time()
    print("Time to run : {}".format(endTime - startTime))
    obj.print_results()
