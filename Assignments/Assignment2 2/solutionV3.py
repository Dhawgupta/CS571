import random
import numpy as np


class Puzzle8:
    def __init__(self, state = None, goal = None, h_cost_function = 0):
        self.row = 3
        self.col = 3
        self.goal = None
        self.state = None
        self.goal_hash = None
        self.state_hash = None
        # collection of all the visited states
        self.all_states = []
        # (key, value) where the key is the index of the state from all_Statea an d value is the f cost)
        self.open_list = dict()
        # (key, value) where key is index and value is the g cost
        self.closed_list = dict()
        # in one case the parent talbe is  hash table in the other case it is a list
        self.parent = dict() # the parents of the node i # expermenting 2 ways
        self.parents = []
        self.real_cost = 0 # the g for the current system
        self.h_funcs = [self.h1, self.h2, self.h3]
        self.h_cost_func = self.h_funcs[h_cost_function] # the cost function to be used for heuristics
        # init the open list etc
        # self.all_states.append(self.state)

        if state:
            self.state =state
            self.open_list[0] = self.real_cost + self.h_cost_func()
            self.all_states.append(self.state) # add the state to the all states list
            self.parents.append(-1) # no parent for the root state
            self.parent[0] = -1
            # init the open list as well
        if goal :
            self.goal = goal
        else:
            print("The first step you should do is initialize the goal state")

        # need to make ds for parents of the node





    # todo insert various inital condition in the fucntion like selecting h fucntion etc

    def reset(self, state = None, goal = None):
        '''
        Reset the environment
        :return:
        '''
        self.init_start(start_state = state)





    def read_goal_file(self,filename):
        '''
        Read goal from a file
        :param filename: The file to read the goal state form
        :return:
        '''
        with open(filename) as fil:
            # read the goal state
            row = 0  # the currebt row
            line = fil.readline()
            while line:
                for col, no in enumerate(line.split()):
                    self.goal[row][col] = no
                line = fil.readline()
                row = row + 1
    def init_goal(self, goal_state):
        '''
        Initialize the Goal state
        :param goal_state: The Goal state
        :return: bool
        '''
        pass
    def init_start(self, start_state = None, steps = 1000):
        '''
        Init a new manually entered start state
        :param start_state: The start state to be assigned if none, then one is randomly generated
        :return: None
        '''
        if start_state is None:
            self.state = start_state
            self.s_hash()
        else:
            puzzle = self.generate_puzzle(steps = steps)
            self.state = start_state
            self.s_hash()
        print("The new start state is  :\n {}".format(self.state))
        self.all_states = []
        self.all_states.append(self.state)
        self.parents = []
        self.parents.append(-1)
        self.parent = dict()
        self.parent[0] = -1
        self.open_list = dict()
        self.closed_list = dict()
        self.real_cost = 0


    def read_start_file(self,file):
        '''
        Read the start state from a file
        :param file: The filename to read the state from
        :return: None
        '''
        with open(file) as fil:
            # read the goal state
            row = 0  # the currebt row
            line = fil.readline()
            while line:
                for col, no in enumerate(line.split()):
                    self.state[row][col] = no
                line = fil.readline()
                row = row + 1
        self.s_hash()
        # when you read the new start state we need to initialize some internal valirables again
        # all_states
        # parents
        # parent
        # open_list
        # closed_list
        self.all_states = []
        self.all_states.append(self.state)
        self.parents = []
        self.parents.append(-1)
        self.parent = dict()
        self.parent[0] = -1
        self.open_list = dict()
        self.closed_list = dict()
        self.real_cost =0
    def arreq_in_list(self,  state):
        '''
        The function to check if the state has been yet discovered or not
        :param state: The state to check
        :return: Return bool if it exists
        '''
        # funtion to check if the myarr exists in the liust_arraus
        return next((True for elem in self.all_states if np.array_equal(elem, state)), False)

    def valid_action(self, action, state = None):
        '''
        Check if the action proposed is valid for state or not
        :param action: The action proposed 0 - up, 1 - left, 2 - right, 3 - down
        :return: returns bool value true, if the action is valid in the state, else return false if the action is invalid
        '''
        # check the validity of the action
        # we have to invert x, y positino as row represent the y coordinte and the col represents the x coordinate
        if state is None: # if no state entered to check the validity
            if self.state_hash == None:
                # if the state_hash is none the create the same
                self.state_hash = dict()
                for row in range(len(self.state)):
                    for col in range(len(self.state[0])):
                        self.state_hash[self.state[row][col]] = [row, col]

            r, c = self.state.shape
            y, x = self.state_hash[0]  # get the position of the blank
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
        else:
            # check the validity of teh netered state
            # if the state_hash is none the create the same
            state_hash = self.s_hash(state = state)
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

    def execute_action(self, action, state = None):
        '''
        Execute the action in return the modified state, doesnt modify the internal state
        :param action:  The action to be perfomred
        :return: Return the modifed staet
        '''
        if state is None : # i.e. want to check the current state of the system
            self.state_hash = self.s_hash()

            # get the blank coordinate
            r, c = self.state.shape  # the size of the game
            y, x = self.state_hash[0]  # the blank coordinate
            # now execute the action and send the update states
            # print "Blank Position {}, {}".format(x,y)

            x_new, y_new = [0, 0]
            if self.valid_action( action):
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
                tile = self.state[y_new][x_new]
                self.state_hash[tile] = [y, x]  # modify the position of the tile to the position of the blank
                self.state_hash[0] = [y_new, x_new]
                new_state = self.state.copy()

                new_state[y_new, x_new] = 0
                new_state[y, x] = tile
                return new_state
            else:
                raise Exception('Invalid action ')  # when the action is invalid
        else:# execute the action for the other state that id custom entered
            state_hash = self.s_hash(state = state)

            # get the blank coordinate
            r, c = state.shape  # the size of the game
            y, x = state_hash[0]  # the blank coordinate
            # now execute the action and send the update states
            # print "Blank Position {}, {}".format(x,y)

            x_new, y_new = [0, 0]
            if self.valid_action(action, state = state):
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
                return new_state
            else:
                raise Exception('Invalid action ')  # when the action is invalid



    def s_hash(self, state = None):
        '''
        Update the hash of the current  state and the goal dstate
        :return: hash_of the current state
        '''
        if state is None: # Means hash need not be calculate for the state
            self.state_hash = dict()
            for row in range(self.row):
                for col in range(self.col):
                    self.state_hash[self.state[row][col]] = [row, col]
            if self.goal_hash == None:
                self.goal_hash = dict()
                for row in range(self.row):
                    for col in range(self.col):
                        self.goal_hash[self.goal[row][col]] = [row, col]

            return self.state_hash
        else:
            state_hash = dict()
            for row in range(self.row):
                for col in range(self.col):
                    state_hash[state[row][col]] = [row, col]
            return state_hash

    def something(self):
        pass

    def h1(self, state = None):
        '''
        This is the plain heursitic with 0 return cose
        '''
        return 0

    def h2(self, state = None):
        # compute the h2 score of the current and teh goal state which is the number
        # h2 = number of displaced tiles
        if state is None:
            self.s_hash() # create the state hash
            cost = np.sum(~(self.goal == self.state))
            # check for the blank vblcok
            if list(self.state_hash[0]) == list(self.goal_hash[0]):
                pass
            else:
                cost  = cost - 1
            return cost
        else:
            state_hash = self.s_hash(state = state)
            cost = np.sum(~(self.goal == state))
            # check for the blank vblcok
            if list(state_hash[0]) == list(self.goal_hash[0]):
                pass
            else:
                cost = cost - 1
            return cost

    def h3(self, state = None):
        '''
        Calculate the h3 cost i.e. Manhattan Distance
        return : The Cost

        '''
        # this will take the min steps required to move the blocks form the current positino to the goal positin
        if state is None:
            cost = 0
            self.s_hash()
            # create the state hash
            # now we will compute the score for the states
            for row in range(self.row):
                for col in range(self.col):
                    # here we will accouting the distance for the blank as well
                    if self.state[row][col] == 0:
                        # not accounting for the blank tile
                        continue
                    x, y = self.goal_hash[self.state[row][col]]
                    # we will take the abs of both
                    cost = cost + abs(row - x) + abs(col - y)
            return cost
        else:
            cost = 0
            state_hash = self.s_hash(state = state)
            for row in range(self.row):
                for col in range(self.col):
                    # here we will accouting the distance for the blank as well
                    if state[row][col] == 0:
                        # not accounting for the blank tile
                        continue
                    x, y = self.goal_hash[state[row][col]]
                    # we will take the abs of both
                    cost = cost + abs(row - x) + abs(col - y)
            return cost
    def generate_puzzle(self, steps = 1000):
        '''
        This will generate a puzzle that can be solved in at max $ steps
        :param steps: The number of steps you want to shuffle the puzzle
        :return: the shuffled puzzle using the goal puzzle
        '''
        if self.goal is None:
            # if there is not goal state
            raise Exception("Goal state not exists")
        puzzle = self.goal.copy()
        shuffle = int(steps)
        action = 0
        for step in range(shuffle):
            action = random.randint(0, 3)
            # print(type(action))
            if self.valid_action(action = action, state = puzzle):  # if the action is vald
                puzzle = self.execute_action(action = action, state = puzzle)
        return puzzle
    def insert_state_open_list(self, state_to_insert, h_cost = 0):
        '''
        state_to_insert : Is the state to be inserted in teh open list
        h_cost : is the appropriate h cost of the system
        This function will insert the element in the open list
        :return: Return true on success and false if element already exisits in the tree
        '''
        if not self.arreq_in_list(state_to_insert):
            # state not in system
            index = len(self.all_states)
            self.all_states.append(state_to_insert)
            g_cost = self.real_cost
            self.open_list[index] = g_cost + h_cost
            return True
        else:
            return False

    def check_goal(self):
        '''
        Check if the current state is the goal state or not
        :return:
        '''
        if (self.state == self.goal).all():
            return True
        return False

    def step(self):
        '''
        This function will step one state forward in the 8 puzzle system with the A* methodolgoy

        :return: end = True or False basicallty bool(open_list)
        '''
        # get the current min valued state from the list
        sno = min(self.open_list, key = self.open_list.get)
        # get the state
        self.state = self.all_states[sno]
        new_states = [] # the new states that will be explored
        if self.check_goal(): # checkfor the gfoal state
            return True # reached the goal hence return True for end
        for action in range(4): # for all possible actions
            if self.valid_action(action  = action): # check if the action is valid for state or not
                new_states.append(self.execute_action(action = action))

        del self.open_list[sno]
        self.closed_list[sno] = self.real_cost
        self.real_cost += 1
        #self.h_cost_func() is the cost function for the currnet object
        self.h_cost_func() # this is the h cosr gunction
        for s in new_states:
            inserted = self.insert_state_open_list(s, self.h_cost_func(state = s))
            if inserted :
                # if inserted succesfully
                index = len(self.all_states) - 1 # the index of the inserted elemen
                # todo shift the parent assignment inside the insert open list function
                self.parent[index] = sno # assigning the parent of index to sno
                self.parents.append(sno) # inserting in the list

        return False






if __name__ == "__main__":
    # running the class
    pass