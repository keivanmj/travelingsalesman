import numpy as np
from queue import Queue, LifoQueue, PriorityQueue
import time
import functions.functions as f

def AStar(matrix) :

    """This is a Uniform-cost search algorithm that returns the shortest path from start point to any other points of the matrix
    """
    start = time.time()
    pq = PriorityQueue()
    path = ""
    pq.put((f.heuristic(matrix, path) + f.calculate_cost(), path))
    visited = set()
    visited_items = ""
    while not pq.empty():
        cost, path = pq.get()
        if f.is_job_done(matrix, path):
            f.print_matrix(matrix)
            return ((500 - f.calculate_cost(matrix, path)), path, (time.time() - start))
        i, j = f.find_location(matrix, path)
        if (i, j, visited_items) in visited:
            continue
        visited_items += f.item_check(matrix, path)
        visited.add((i, j, visited_items))
        for move in ["L", "R", "U", "D"]:
            newpath = path + move
            if move in f.find_successors(matrix, f.find_location(matrix, path)):
                pq.put(((f.heuristic(matrix, newpath)) + f.calculate_cost(), newpath))
    end = time.time()
    return "No routes found!"