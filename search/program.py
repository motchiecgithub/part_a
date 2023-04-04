# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion

from .utils import render_board
from queue import PriorityQueue
MAX_DISTANCE = 12
MAX_HEURISTIC = 50
HEX_NEIGHBORS = [(0,1), (-1,1), (-1, 0), (0, -1), (1, -1), (1,0)]
def linear_distance(goal, start):
    distance = max(abs(goal[0] - start[0]), abs(goal[1] - start[1]), abs(goal[0] + goal[1] - start[0] - start[1]))
    return distance

def distance(goal: tuple, point: tuple):
    min_distance = MAX_DISTANCE
    for i in [-7, 0, 7]:
        for j in [-7, 0, 7]:
            coordinate = [goal[0] + i, goal[1] + j]
            if (min_distance > linear_distance(point, coordinate)):
                min_distance =  linear_distance(point, coordinate)
    return min_distance

def heuristic(start, goals):
    result = 0
    for goal in goals:
        result = result + distance(goal, start)
    return result

def expand(start, power):
    result = [] 
    for item in HEX_NEIGHBORS:
        children = []
        for i in range(1, power + 1):
            children.append(((start[0] + item[0] * i) % 7, (start[1] + item[1] * i) % 7))
        result.append(children)
    return result

def track(parent, node):
    result = []
    while parent.get(node):
        result.append(parent.get(node))
        node = parent[node]
    return result 

def search(input: dict[tuple, tuple]) -> list[tuple]:
    """
    This is the entry point for your submission. The input is a dictionary
    of board cell states, where the keys are tuples of (r, q) coordinates, and
    the values are tuples of (p, k) cell states. The output should be a list of 
    actions, where each action is a tuple of (r, q, dr, dq) coordinates.

    See the specification document for more details.
    """

    # The render_board function is useful for debugging -- it will print out a 
    # board state in a human-readable format. Try changing the ansi argument 
    # to True to see a colour-coded version (if your terminal supports it).
    
    reds = {}
    blues = {}
    parent = {}
    cost = {}
    for item in input:
        if input[item][0] == 'b':
            blues[item] = input[item]
        else:
            reds[item] = input[item]
            parent[item] = None
            cost[item] = 0
    
    open_lst = PriorityQueue()
    for red in reds:
        open_lst.put((heuristic(red, blues), red))
    
    direction = []
    # start loop 
    result_coordinate = []
    while blues:
        curr = open_lst.get()
        result_coordinate.append(curr[1])
        # generate neighbors
        neighbors = expand(curr[1], reds[curr[1]][1])
        reds.pop(curr[1])
        min_h = MAX_HEURISTIC
        next_move = []
        reach = {}

        # choose best move between neighbours 
        for move in neighbors:
            for node in move:
                if blues.get(node) and blues.get(node)[1] != 6:
                    reach[node] = 1
                else:
                    reach[node] = 0
                    h = heuristic(node, blues)
                    if min_h > h:
                        min_h = h
                        next_move = move
        reachable = 0
        for move in neighbors:
            sum = 0
            for node in move: 
                sum += reach[node]
            if sum > reachable:
                reachable = sum
                next_move = move
        
        # update reds 
        for item in next_move:
            if blues.get(item):
                test = blues.pop(item)
                if test[1] != 6:
                    reds[item] = ('r', 1 + test[1])
            else: 
                reds[item] = ('r', 1)
            parent[item] = curr[1]
            open_lst.put((heuristic(item, blues), item))
        direction.append(HEX_NEIGHBORS[neighbors.index(next_move)])
    result = []
    for i in range(0, len(result_coordinate)):
        result.append((result_coordinate[i][0], result_coordinate[i][1], direction[i][0], direction[i][1]))
    # Here we're returning "hardcoded" actions for the given test.csv file.
    # Of course, you'll need to replace this with an actual solution...
    return result
