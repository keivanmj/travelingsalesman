import numpy as np
import queue



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
    for step in range(len(path)):
        i, j = find_location(maze, path[0:step+1])
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



def breadthFirstSearch(matrix):
    """This is a Breadth-first search algorithm that returns the shortest path from start point to any other points of the matrix
    """
    size = matrix.shape[0]*matrix.shape[1] - np.count_nonzero(matrix == 'X')
    q = queue.Queue()
    q.put("")
    path = ""
    best_valid_path = set()
    while len(path) < size-1:
        path = q.get()
        for move in ["L", "R", "U", "D"]:
            newpath = path + move
            if move in find_successors(matrix, find_location(matrix, path)):
                print(newpath)
                if is_job_done(matrix, newpath):
                    if best_valid_path == set():
                        best_valid_path = (newpath, calculate_cost(matrix, newpath))
                    else:
                        if calculate_cost(matrix, newpath) < calculate_cost(matrix, best_valid_path):
                            best_valid_path = (newpath, calculate_cost(matrix, newpath))
                else:
                    q.put(newpath)
    print_matrix(matrix, best_valid_path[0])
    print(best_valid_path)



#Rows = int(input("Give the number of rows:"))
#Columns = int(input("Give the number of columns:"))
#matrix = np.array([list(map(str, input().split())) for _ in range(Rows)])
#print(matrix)

#cost_matrix = list(map(lambda row: list(map(add_free_items, row)), matrix))
#print(cost_matrix)

#matrix = np.array([["5", "2T", "1"], ["2R", "5", "5"], ["4C", "3T", "7I"]])
#matrix = np.array([["5", "3C", "9I", "25", "1"], ["2R", "X", "3T", "X", "5T"], ["4C", "4", "2", "3", "7I"]])
matrix = np.array([["1R", "1", "1", "5", "5", "4", "2C", "1", "15", "1B"], ["1", "1", "5", "3", "5", "5", "4", "5", "X", "X"]
                 , ["5", "1I", "1", "6", "2", "2", "2", "1", "1", "1T"], ["X", "X", "1", "6", "5", "5", "2", "1", "1", "X"]
                 , ["X", "X", "1", "X", "X", "50", "2", "1C", "1", "X"], ["1", "1", "1", "2", "2", "2T", "2", "1", "1", "1"]])

#print(matrix)
#print(cost(matrix))
#print(find_start_point(matrix))
#print(find_goal_points(matrix))
#print_matrix(matrix)
#print(find_successors(matrix, (1, 0)))
#print(is_job_done(matrix, ""))
breadthFirstSearch(matrix)
#print(find_successors(matrix, find_location(matrix, "D")))
#print(matrix[1, 2])
#print(is_job_done(matrix, "DRRU"))
