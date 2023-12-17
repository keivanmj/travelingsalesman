import numpy as np
from queue import Queue, LifoQueue, PriorityQueue
import time



def calculate_cost(matrix, path):
    """calculates the cost of a move in matrix

    Args:
        matrix (_type_):
        path (_type_):

    Returns:
        _type_: cost
    """
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



def calculate_heuristic(matrix, path):
    """calculates the sum of heuristic distances between current place and all goal points using manhattan distance

    Args:
        matrix (_type_):
        path (_type_):
    Returns:
        int: heuristic distance
    """
    def visited_goals(matrix, path):
        """shows reached goals in a path

        Args:
            matrix (_type_):
            path (_type_):

        Returns:
            _type_: returns all goals that were visited
        """
        goals = find_goal_points(matrix)
        return set(find_location(matrix, path[0:step]) for step in range(len(path)+1) if find_location(matrix, path[0:step]) in goals)
    
    heuristic = 0
    ip, jp = find_location(matrix, path)
    goal_points = find_goal_points(matrix) - visited_goals(matrix, path)
    for _ in find_goal_points(matrix):
        distances = set()
        min_dist = 0
        for goal_point in goal_points:
            distances.add((goal_point[0], goal_point[1], (abs(ip - goal_point[0]) + abs(jp - goal_point[1]))))
        if distances != set():
            min_dist = min(distances, key=lambda x: x[2])
            heuristic += min_dist[2]
            ip, jp = min_dist[0], min_dist[1]
            if goal_points:
                goal_points.remove((ip, jp))
    return heuristic



def item_check(matrix, path):
    """check for an item in a matrix block

    Args:
        matrix (_type_):
        path (_type_):

    Returns:
        _type_: returns the item
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
        pos.add((i, j))
    print("┼" + "─────┼"*len(matrix[0]))
    for i, row in enumerate(matrix):
        print("│", end="")
        for j, val in enumerate(row):
            if (i, j) in pos:
                print("{:^5}".format("+"), end = "│")
            else:
                print("{:^5}".format(val), end = "│")
        print("\n┼" + "─────┼"*len(matrix[0]))



def breadthFirstSearch(matrix):
    """This is a Breadth-first search algorithm that returns the shortest path from start point to any other points of the matrix
    """
    start_time = time.time()
    q = Queue()
    path = ""
    q.put(path)
    visited = set()
    visited_items = ""
    while not(is_job_done(matrix, path)) and not(q.empty()):
        path = q.get()
        i, j = find_location(matrix, path)
        if (i, j, visited_items) in visited:
            continue
        visited_items += item_check(matrix, path)
        visited.add((i, j, visited_items))
        for move in ["L", "R", "U", "D"]:
            newpath = path + move
            if move in find_successors(matrix, find_location(matrix, path)):
                q.put(newpath)
    print_matrix(matrix)
    if is_job_done(matrix, path):
        return ((500 - calculate_cost(matrix, path)), path, (time.time() - start_time))
    else:
        return "No routes found!"



def depthFirstSearch(matrix):
    """This is a Depth-first search algorithm that returns the shortest path from start point to any other points of the matrix
    """
    start_time = time.time()
    s = LifoQueue()
    path = ""
    s.put(path)
    visited = set()
    visited_items = ""
    while not(is_job_done(matrix, path)) and not(s.empty()):
        path = s.get()
        i, j = find_location(matrix, path)
        if (i, j, visited_items) in visited:
            continue
        visited_items += item_check(matrix, path)
        visited.add((i, j, visited_items))
        for move in ["L", "R", "U", "D"]:
            newpath = path + move
            if move in find_successors(matrix, find_location(matrix, path)):
                s.put(newpath)
        if (len(path) >= (matrix.shape[0] * matrix.shape[1])):
            print_matrix(matrix)
            return "No routes found!"
    print_matrix(matrix)
    if is_job_done(matrix, path):
        return ((500 - calculate_cost(matrix, path)), path, (time.time() - start_time))
    else:
        return "No routes found!"



def IterativeDeepeningSearch(matrix):
    """This is a Iterative-deepening search algorithm that returns the shortest path from start point to any other points of the matrix
    """
    start_time = time.time()
    s = LifoQueue()
    path = ""
    s.put(path)
    depth = 0
    while not(is_job_done(matrix, path)):
        path = s.get()
        if (len(path) == 0):
            depth += 1
            visited = set()
            visited_items = ""
            s.put("")
        i, j = find_location(matrix, path)
        if (i, j, visited_items) in visited:
            continue
        visited_items += item_check(matrix, path)
        visited.add((i, j, visited_items))
        if (len(path) < depth):
            for move in ["L", "R", "U", "D"]:
                newpath = path + move
                if move in find_successors(matrix, find_location(matrix, path)):
                    s.put(newpath)
        if (len(path) >= (matrix.shape[0] * matrix.shape[1])):
            print_matrix(matrix)
            return "No routes found!"
    print_matrix(matrix)
    if is_job_done(matrix, path):
        return ((500 - calculate_cost(matrix, path)), path, (time.time() - start_time))
    else:
        return "No routes found!"



def uniformCostSearch(matrix):
    """This is a Uniform-cost search algorithm that returns the shortest path from start point to any other points of the matrix
    """
    start_time = time.time()
    pq = PriorityQueue()
    path = ""
    pq.put((calculate_cost(matrix, path), path))
    visited = set()
    visited_items = ""
    while not pq.empty():
        cost, path = pq.get()
        if is_job_done(matrix, path):
            print_matrix(matrix)
            return ((500 - calculate_cost(matrix, path)), path, (time.time() - start_time))
        i, j = find_location(matrix, path)
        if (i, j, visited_items) in visited:
            continue
        visited_items += item_check(matrix, path)
        visited.add((i, j, visited_items))
        for move in ["L", "R", "U", "D"]:
            newpath = path + move
            if move in find_successors(matrix, find_location(matrix, path)):
                pq.put(((calculate_cost(matrix, newpath)), newpath))
    if not(is_job_done(matrix, path)):
        print_matrix(matrix)
        return "No routes found!"



def AStar(matrix):
    """This is a A-star algorithm that returns the shortest path from start point to any other points of the matrix
    """
    start_time = time.time()
    pq = PriorityQueue()
    path = ""
    pq.put(((calculate_heuristic(matrix, path) + calculate_cost(matrix, path)), path))
    visited = set()
    visited_items = ""
    while not pq.empty():
        cost, path = pq.get()
        if is_job_done(matrix, path):
            print_matrix(matrix)
            return ((500 - calculate_cost(matrix, path)), path, (time.time() - start_time))
        i, j = find_location(matrix, path)
        if (i, j, visited_items) in visited:
            continue
        visited_items += item_check(matrix, path)
        visited.add((i, j, visited_items))
        for move in ["L", "R", "U", "D"]:
            newpath = path + move
            if move in find_successors(matrix, find_location(matrix, path)):
                pq.put(((calculate_heuristic(matrix, newpath) + calculate_cost(matrix, newpath)), newpath))
    if not(is_job_done(matrix, path)):
        print_matrix(matrix)
        return "No routes found!"


def bestFirstSearch(matrix) :
    """This is a bestFirstSearch search algorithm that returns the shortest path from start point to any other points of the matrix
    """
    start_time = time.time()
    pq = PriorityQueue()
    pq_end = PriorityQueue()
    path = ""
    pq_end.put((calculate_heuristic(matrix, path), path))
    pq.put((calculate_heuristic(matrix, path), path))
    visited = set()
    visited_items = ""
    while pq_end.get() != 0:
        cost, path = pq.get()
        if is_job_done(matrix, path):
            print_matrix(matrix)
            return ((500 - calculate_cost(matrix, path)), path, (time.time() - start_time))
        i, j = find_location(matrix, path)
        if (i, j, visited_items) in visited:
            continue
        visited_items += item_check(matrix, path)
        visited.add((i, j, visited_items))
        for move in ["L", "R", "U", "D"]:
            newpath = path + move
            if move in find_successors(matrix, find_location(matrix, path)):
                pq.put(((calculate_heuristic(matrix, newpath)), newpath))
        pq_end.put(pq.queue[0])
    if not(is_job_done(matrix, path)):
        print_matrix(matrix)
        return "No routes found!"


while True:
    try:
        choice = str(input("Do you want to enter the matrix manually(M) or use the samples(S)?\nEnter (E) if you wanna exit."))
        if choice == "M":
            Rows = int(input("Give the number of rows:"))
            Columns = int(input("Give the number of columns:"))
            matrix = np.array([list(map(str, input().split())) for _ in range(Rows)])
        elif choice == "S":
            sample_number = int(input("(3, 3) -> 0\n(3, 5) -> 1\n(6, 5) -> 2\nchoose one of those samples:"))
            if sample_number == 0:
                matrix = np.array([["5", "2T", "1"], ["2R", "5", "X"], ["4C", "3T", "7I"]])
            elif sample_number == 1:
                matrix = np.array([["5", "3C", "9I", "25", "1"], ["2R", "X", "3T", "X", "5T"], ["4C", "4", "2", "3", "7I"]])
            elif sample_number == 2:
                matrix = np.array([["4", "2C", "1", "15", "1B"], ["5", "4", "5", "X", "X"]
                                , ["2", "2", "1", "1R", "1T"], ["5", "2", "1", "1", "X"]
                                , ["50", "2", "1C", "1", "X"], ["2T", "2", "1", "1", "1"]])
        elif choice == "E":
            break
        else:
            raise ValueError("Wrong input!\nTry again.")

        if find_start_point(matrix) == None:
            raise ValueError("There must be one 'R' point in matrix!")
        if find_goal_points(matrix) == set():
            raise ValueError("There must be at least one 'T' point in matrix!")
        

        print(breadthFirstSearch(matrix))
        print(depthFirstSearch(matrix))
        print(IterativeDeepeningSearch(matrix))
        print(uniformCostSearch(matrix))
        print(AStar(matrix))
        print(bestFirstSearch(matrix))
    except Exception as e:
        print(e)