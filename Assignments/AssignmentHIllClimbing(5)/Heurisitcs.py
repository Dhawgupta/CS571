import numpy as np

def h1(current, goal):
    # COmpute the h1 score which is 0 for the current approach
    return 0


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