import phase2.Stack as s1
import phase1.successor as p1
import numpy as np
import queue
import time
from queue import LifoQueue

def calculate_cost(matrix, path):
    maze = np.copy(matrix)
    def check_item(old_item):
        """this function will add the free items in matrix
    Args:
        old_item (str): matrix items with letters
    Returns:
        int: cost matrix items
    """
        Coffee = 10
        Biscuit = 5
        Ice_cream = 12

        if "C" == old_item[-1]:
            return (old_item[:-1], str(int(old_item[:-1]) - Coffee))
        elif "B" == old_item[-1]:
            return (old_item[:-1], str(int(old_item[:-1]) - Biscuit))
        elif "I" == old_item[-1]:
            return (old_item[:-1], str(int(old_item[:-1]) - Ice_cream))
        elif "R" == old_item[-1]:
            return (old_item, str(old_item[:-1]))
        elif "T" == old_item[-1]:
            return (old_item, str(old_item[:-1]))
        else:
            return (old_item, old_item)
    cost = 0
    for step in range(len(path)+1):
        i, j = find_location(maze, path[0:step])
        maze[i, j], cost_item = check_item(maze[i, j])
        cost += int(cost_item)
    return cost

def find_location(matrix, path):
    """Finds the location of a path on the matrix
    Args:
    matrix (list): The matrix to search through
    path (str): The path that we are looking for it's position
    Returns:
    tuple: A tuple containing the x and y coordinates of the item or None if it is not found
    """
    i, j = find_start_point(matrix)
    for move in path:
        if move == "L":
            j -= 1
        elif move == "R":
            j += 1
        elif move == "U":
            i -= 1
        elif move == "D":
            i += 1
    return (i, j)



def find_start_point(matrix):
    """This function will return the start point
    Args:
        matrix (nd.array): the cost matrix
    Returns:
        _type_: start point
    """
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if "R" in matrix[i, j]:
                return (i, j)
    return None



def find_goal_points(matrix):
    """This function will return the goal points
    Args:
        matrix (nd.array): the cost matrix
    Returns:
        _type_: a list of goal points
    """
    goal_points = set()
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if "T" in matrix[i, j]:
                goal_points.add((i, j))
    return goal_points



def find_successors(matrix, position):
    """This function will return the possible movement for next move
    Args:
        matrix (nd.array): the cost matrix
        position (set): start position for next move
    Returns:
        _type_: a list of possible moves
    """
    positions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    moves = ["L", "R", "U", "D"]
    successors = []
    for direction, pos in enumerate(positions):
        new_x, new_y = position[0] + pos[0], position[1] + pos[1]
        if 0 <= new_x < matrix.shape[0] and 0 <= new_y < matrix.shape[1] and matrix[new_x, new_y] != "X":
            successors.append(moves[direction])
    return successors



def is_job_done(matrix, moves):
    """This function will return the job done message
    Returns:
        boolean: returns is the job done or not
    """
    i, j = find_start_point(matrix)
    visited_goals = set()
    for move in moves:
        if move == "L":
            j -= 1
        elif move == "R":
            j += 1
        elif move == "U":
            i -= 1
        elif move == "D":
            i += 1
        #print(f"({i}, {j})")
        #print(matrix[i, j])
        if (i, j) in find_goal_points(matrix):
            visited_goals.add((i, j))
    if visited_goals == find_goal_points(matrix):
        return True
    else:
        return False



def print_matrix(matrix, moves=""):
    """This function will print the matrix with moves
    Args:
        matrix (nd.array): the org matrix
        moves (list): the path to the goal
    """
    i, j = find_start_point(matrix)
    pos = set()
    for move in moves:
        if move == "L":
            j -= 1
        elif move == "R":
            j += 1
        elif move == "U":
            i -= 1
        elif move == "D":
            i += 1
        pos.add((i, j))    #  '─', '│', '┌', '│', '└', '│', '├', '─', '─', '┐', '┬', '┘', '┴', '┤', '┼'
    print("┌" + "─────┬"*len(matrix[0]))
    for i, row in enumerate(matrix):
        print("│", end="")
        for j, val in enumerate(row):
            if (i, j) in pos:
                print("{:^5}".format("+"), end = "│")
            else:
                print("{:^5}".format(val), end = "│")
        print("\n├" + "─────┼"*len(matrix[0]))

def depthFirstSearch(matrix):
    """This is a Depth-first search algorithm that returns the shortest path from start point to any other points of the matrix
        """
    start = time.time()
    stack = s1.create_stack()
    #q = queue.Queue()
    s1.push(stack, "")
    #q.put("")
    path = ""
    print_matrix(matrix)
    while not (is_job_done(matrix, path)):
        # path = q.get()
        path = s1.pop(stack)
        # print("path is " + path)
        for move in ["L", "R", "U", "D"]:
            newpath = path + move
            # print("new path is " + newpath)
            if move in find_successors(matrix, find_location(matrix, path)):
                #q.put(newpath)
                print("new path is " + newpath)
                s1.push(stack, newpath)
                # print(s1)
    end = time.time()
    # print_matrix(matrix)
    return ( (490 - calculate_cost(matrix, path)), "path is " + path, (end - start))

# matrix = np.array([["4", "2C", "1", "15", "1B"], ["5", "4", "5", "X", "X"]
#                     , ["2", "2", "1", "1R", "1T"], ["5", "2", "1", "1", "X"]
#                     , ["50", "2", "1C", "1", "X"], ["2T", "2", "1", "1", "1"]])
#
# print(depthFirstSearch(matrix))



# choise = str(input("Do you want to enter the matrix manually(True) or use the samples(False)?"))
# if choise == "True":
#     Rows = int(input("Give the number of rows:"))
#     Columns = int(input("Give the number of columns:"))
#     matrix = np.array([list(map(str, input().split())) for _ in range(Rows)])
# elif choise == "False":
#     sample_number = int(input("(3, 3) -> 0\n(3, 5) -> 1\n(6, 5) -> 2\nchoose one of those samples:"))
#     if sample_number == 0:
#         matrix = np.array([["5", "2T", "1"], ["2R", "5", "5"], ["4C", "3T", "7I"]])
#     elif sample_number == 1:
#         matrix = np.array([["5", "3C", "9I", "25", "1"], ["2R", "X", "3T", "X", "5T"], ["4C", "4", "2", "3", "7I"]])
#     elif sample_number == 2:
#         matrix = np.array([["4", "2C", "1", "15", "1B"], ["5", "4", "5", "X", "X"]
#                          , ["2", "2", "1", "1R", "1T"], ["5", "2", "1", "1", "X"]
#                          , ["50", "2", "1C", "1", "X"], ["2T", "2", "1", "1", "1"]])
#
# print(breadthFirstSearch(matrix))