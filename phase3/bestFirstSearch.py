import numpy as np
from queue import Queue, LifoQueue, PriorityQueue
import time
import functions.functions as f

def bestFirstSearch(matrix) :
    Start = PriorityQueue()
    End = set()
    start = time.time()
    s = LifoQueue()
    path = ""
    s.put(path)
    visited = set()
    visited_items = ""
    while not (f.is_job_done(matrix, path)):
        path = s.get()
        i, j = f.find_location(matrix, path)
        if (i, j, visited_items) in visited:
            continue
        visited_items += f.item_check(matrix, path)
        visited.add((i, j, visited_items))
        for move in ["L", "R", "U", "D"]:
            newpath = path + move
            if move in f.find_successors(matrix, f.find_location(matrix, path)):
                s.put(newpath)
    end = time.time()
    f.print_matrix(matrix)
    return ( (500 - f.calculate_cost(matrix, path)), path, (end - start))