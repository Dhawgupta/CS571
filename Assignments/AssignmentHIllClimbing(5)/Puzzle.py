import random
import numpy as np
from make_puzzle import generate_puzzle
import sys
from queue import PriorityQueue


class Puzzle8:
    def __init__(self, puzzle_config, g, h):
        self.puzzle_config = puzzle_config
        self.g = g
        self.h = h

    def __lt__(self, other):
        if (self.g + self.h == other.g + other.h):
            if self.g == other.g:
                return self.convert_state_to_string(self.puzzle_config) < self.convert_state_to_string(other.puzzle_config)
            return (self.g < other.g)
        return (self.g + self.h) <= (other.g + other.h)
    def convert_state_to_string(self, state):
        state = state.astype(int)
        str1 = ""
        for i in range(len(state)):
            for j in range(len(state[0])):
                str1 = str1 + str(int(state[i][j]))
        return str1