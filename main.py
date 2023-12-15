import numpy as np
import queue



def cost(matrix):
    """This function will return the cost matrix
    Args:
        matrix (nd.array): the org matrix
    Returns:
        _type_: cost matrix
    """
    def add_free_items(old_item):
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
            return str(int(old_item[:-1]) - Coffee)
        elif "B" == old_item[-1]:
            return str(int(old_item[:-1]) - Biscuit)
        elif "I" == old_item[-1]:
            return str(int(old_item[:-1]) - Ice_cream)
        elif "R" == old_item[-1]:
            return str(old_item[:-1])
        elif "T" == old_item[-1]:
            return str(old_item[:-1])
        else:
            return old_item
    return list(map(lambda row: list(map(add_free_items, row)), matrix))



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
    goal_points = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if "T" in matrix[i, j]:
                goal_points.append((i, j))
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
    visited_goals = []
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
            visited_goals.append((i, j))
    if len(visited_goals) == len(find_goal_points(matrix)):
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
    print("┌" + "─────┬"*len(cost(matrix)[0]))
    for i, row in enumerate(cost(matrix)):
        print("│", end="")
        for j, val in enumerate(row):
            if (i, j) in pos:
                print("{:^5}".format("+"), end = "│")
            else:
                print("{:^5}".format(val), end = "│")
        print("\n├" + "─────┼"*len(cost(matrix)[0]))



def breadthFirstSearch(matrix):
    """This is a Breadth-first search algorithm that returns the shortest path from start point to any other points of the matrix
    """
    q = queue.Queue()
    q.put("")
    path = ""
    valid_paths = []
    visited = [find_location(matrix, "")]
    c=0
    while not(c == 100):
        path = q.get()
        c+=1
        print(f"###{c}")
        for move in ["L", "R", "U", "D"]:
            newpath = path + move
            if move in find_successors(matrix, find_location(matrix, path)):
                if find_location(matrix, newpath) not in visited:
                    visited.append(find_location(matrix, newpath))
                    print(newpath)
                    print(visited)
                    if is_job_done(matrix, newpath):
                        valid_paths.append(newpath)
                        visited = [find_location(matrix, "")]
                        for part in range(len(newpath)-1):
                            #print(newpath[0:part+1])
                            visited.append(find_location(matrix, newpath[0:part+1]))
                    else:
                        q.put(newpath)
    print(f"###{valid_paths}")
    #print_matrix(matrix, valid_paths[0])
        



#Rows = int(input("Give the number of rows:"))
#Columns = int(input("Give the number of columns:"))
#matrix = np.array([list(map(str, input().split())) for _ in range(Rows)])
#print(matrix)

#cost_matrix = list(map(lambda row: list(map(add_free_items, row)), matrix))
#print(cost_matrix)

matrix = np.array([["5", "25", "1"], ["2R", "X", "5"], ["4C", "3T", "7I"]])
#matrix = np.array([["5", "3C", "9I", "25", "1"], ["2R", "X", "3T", "X", "5T"], ["4C", "4", "2", "3", "7I"]])

#print(matrix)
#print(cost(matrix))
#print(find_start_point(matrix))
#print(find_goal_points(matrix))
print_matrix(matrix)
#print(find_successors(matrix, (1, 0)))
#print(is_job_done(matrix, ""))
breadthFirstSearch(matrix)
#print(find_successors(matrix, find_location(matrix, "D")))
#print(matrix[1, 2])
#print(is_job_done(matrix, "DRRU"))
