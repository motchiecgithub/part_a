# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion
MAX_DISTANCE = 12
HEX_NEIGHBORS = [(0,1), (-1,1), (-1, 0), (0, -1), (1, -1), (1,0)]
import math
from .utils import render_board

def linear_distance(goal, start):
    distance = max(abs(goal[0] - start[0]), abs(goal[1] - start[1]), abs(goal[0] + goal[1] - start[0] - start[1]))
    return distance

def distance(goal: tuple, point: tuple):
    min_distance = MAX_DISTANCE
    for i in [-7, 0, 7]:
        for j in [-7, 0, 7]:
            coordinate = [goal[0] + i, goal[1] + j]
            # print("coordinate: " + str(coordinate))
            # print(linear_distance(point, coordinate))
            if (min_distance > linear_distance(point, coordinate)):
                min_distance =  linear_distance(point, coordinate)
    return min_distance

def move():
    pass
def extend():
    pass
def kill():
    pass
    
        
        
                


def minimum_heuristic_cost(point: list[tuple], goal: dict[tuple, tuple]):
    return None

def generating_node(points: dict[tuple, tuple]):
    result = []
    for point in points:
        for element in HEX_NEIGHBORS:
            for i in range(1, points[point][1] + 1):
                new_point = ((point[0] + element[0] * i) % 7, (point[1] + element[1] * i) % 7)
                result.append(new_point)
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
    print(render_board(input, ansi=False))
    
    # Here we're returning "hardcoded" actions for the given test.csv file.
    # Of course, you'll need to replace this with an actual solution...
    
    # code start
    
    starts = {}
    goals = {}
    for element in input:
        if (input[element][0] == 'b'):
            goals[element] = input[element]
        else:
            starts[element] = input[element]
    min = 12
    point = []
    for start in starts:
        for goal in goals:
            if (distance(goal, start) < min):
                min = distance(goal, start)
                point = goal
    lst = generating_node({(5,6): ('r',2)})
    print(lst)
    # code end 
    
    return [
        (5, 6, -1, 1),
        (3, 1, 0, 1),
        (3, 2, -1, 1),
        (1, 4, 0, -1),
        (1, 3, 0, -1)
    ]
