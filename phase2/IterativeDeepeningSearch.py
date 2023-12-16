import phase1.successor as p1
import numpy as np
from queue import LifoQueue
import time



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



def item_check(matrix, path):
    """this function will add the free items in matrix
    Args:
        old_item (str): matrix items with letters
    Returns:
        int: cost matrix items
    """

    i, j = find_location(matrix, path)
    if "C" in matrix[i, j]:
        return "C"
    elif "B" in matrix[i, j]:
        return "B"
    elif "I" in matrix[i, j]:
        return "I"
    elif "T" in matrix[i, j]:
        return "T"
    else:
        return ""



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



def IterativeDeepeningSearch(matrix):
    """This is a Depth-first search algorithm that returns the shortest path from start point to any other points of the matrix
        """
    start = time.time()
    s = LifoQueue()
    path = ""
    s.put(path)
    visited = set()
    visited_items = ""
    c = 0
    while not (is_job_done(matrix, path)):
        path = s.get()
        print(path)
        if (len(path) == 0) :
            c = c + 1
            s.put("")
        print("c is: " + str(c))
        # i, j = find_location(matrix, path)
        # if (i, j, visited_items) in visited:
        #     continue
        # visited_items += item_check(matrix, path)
        # visited.add((i, j, visited_items))
        if (len(path) < c) :
            for move in ["L", "R", "U", "D"]:
                newpath = path + move
                if move in p1.find_successors(matrix, find_location(matrix, path)):
                    s.put(newpath)
    end = time.time()
    print_matrix(matrix)
    return ( (500 - calculate_cost(matrix, path)), path, (end - start))



choise = str(input("Do you want to enter the matrix manually(True) or use the samples(False)?"))
if choise == "True":
    Rows = int(input("Give the number of rows:"))
    Columns = int(input("Give the number of columns:"))
    matrix = np.array([list(map(str, input().split())) for _ in range(Rows)])
elif choise == "False":
    sample_number = int(input("(3, 3) -> 0\n(3, 5) -> 1\n(6, 5) -> 2\nchoose one of those samples:"))
    if sample_number == 0:
        matrix = np.array([["5", "2T", "1"], ["2R", "5", "X"], ["4C", "3T", "7I"]])
    elif sample_number == 1:
        matrix = np.array([["5", "3C", "9I", "25", "1"], ["2R", "X", "3T", "X", "5T"], ["4C", "4", "2", "3", "7I"]])
    elif sample_number == 2:
        matrix = np.array([["4", "2C", "1", "15", "1B"], ["5", "4", "5", "X", "X"]
                         , ["2", "2", "1", "1R", "1T"], ["5", "2", "1", "1", "X"]
                         , ["50", "2", "1C", "1", "X"], ["2T", "2", "1", "1", "1"]])

print(IterativeDeepeningSearch(matrix))